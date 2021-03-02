from datetime import datetime


# Returns current timestamp as string
def getCurrentDateTime():
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d %H:%M:%S.%f")[:-3]
    return timestamp