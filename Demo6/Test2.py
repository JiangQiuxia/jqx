import threading
from time import sleep,ctime

class MyThread(threading.Thread):
    def __init__(self,func,args,name=""):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name

    def run(self):
        self.func(*self.args)

def supper_Player(file_,time):
    for i in range(2):
        print("start playing %s! %s" %(file_,ctime()))
        sleep(time)

lists={"爱情买卖.mp3":3,"阿凡达.mp4":5,"我和你.mp3":4}

theads=[]
files=range(len(lists))

for file_,time in lists.items():
    t = MyThread(supper_Player,(file_,time),supper_Player.__name__)
    theads.append(t)

if __name__ == '__main__':
    for i in files:
        theads[i].start()
    for i in files:
        theads[i].join()

print("end:%s" %ctime())