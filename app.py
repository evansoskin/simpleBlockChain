from helpers import getCurrentDateTime
from Block import Block
from Blockchain import Blockchain
from BlockChainService import BlockchainService
from Transaction import Transaction
from ecdsa import SigningKey, VerifyingKey, SECP256k1
from flask import Flask, flash, redirect, render_template, request


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

BCI = BlockchainService()

@app.route("/")
def index():

    return render_template("blocks.html", BCI=BCI)

@app.route("/transactions",methods=["GET"])
def getTransactions():

    block = BCI.getBlockByHash(request.args.get("hash"))
    return render_template("transactions.html", block=block, BCI=BCI)

@app.route("/settings", methods=["GET", "POST"])
def settings():

    if request.method == "POST":
        difficulty = int(request.form.get("difficulty"))
        miningReward = int(request.form.get("miningReward"))

        BCI.blockchainInstance.difficulty = difficulty
        BCI.blockchainInstance.miningReward = miningReward

        #flash('Settings confirmed!')
        return redirect("/")
    else:
        return render_template("settings.html", BCI=BCI)

@app.route("/transactions/create", methods=["GET", "POST"])
def createTransaction():

    if request.method == "POST":
        fromAddress = VerifyingKey.from_string( bytearray.fromhex( BCI.walletKeys["publicKey"] ), curve=SECP256k1 )
        toAddress = VerifyingKey.from_string( bytearray.fromhex( request.form.get("toAddress") ), curve=SECP256k1 ) 
        amount = request.form.get("amount")

        tx = Transaction(fromAddress, toAddress, amount)
        tx.signTransaction( SigningKey.from_string(bytearray.fromhex(BCI.walletKeys["privateKey"]), curve=SECP256k1) )
        BCI.blockchainInstance.addTransaction(tx)

        return redirect("/transactions/pending")
    else:
        return render_template("createTransaction.html", BCI=BCI)

@app.route("/transactions/pending",methods=["GET","POST"])
def getPendingTransactions():

    if request.method == "POST":
        BCI.blockchainInstance.minePendingTransactions(VerifyingKey.from_string( bytearray.fromhex( BCI.walletKeys["publicKey"] ), curve=SECP256k1 ) )

        return redirect("/")
    else:
        pendingTransactions = BCI.blockchainInstance.pendingTransactions
        return render_template("pendingTransactions.html", pendingTransactions=pendingTransactions)