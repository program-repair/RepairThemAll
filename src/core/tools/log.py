
import datetime


def printlog(*args, **kwargs):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), end=' ')
    print(*args, **kwargs)
