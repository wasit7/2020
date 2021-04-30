import time

def x():
    tid=0
    while True:
        tid+=1
        time.sleep(1)
        #send to f(tid,ts)

def f(tid,ts):
    time.sleep(2)
    #send to streamer
    #streamer send to g(tid,ts)

def g(tid,ts):
    time.sleep(3)
    #send to y()

def y(tid,ts):
    #compute throughout
    #print(ts,tid)