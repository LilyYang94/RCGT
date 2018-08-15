#coding=utf-8
import threading
from time import sleep, ctime

loops = [4,2]

class ThreadFunc(object):
    def __init__(self,func,args,name=''):
        self.name=name
        self.func=func
        self.args=args

    def __call__(self):
        apply(self.func,self.args)

def loop(nloop,nsec):
    print "seart loop",nloop,'at:',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()

def main():
    print 'starting at:',ctime()
    threads=[]
    nloops = range(len(loops))
    for i in nloops:
        #调用 ThreadFunc 实例化的对象,创建所有线程
        t = threading.Thread(target=ThreadFunc(loop,(i,loops[i]),loop.__name__))
        threads.append(t)

    #开始线程
    for i in nloops:
        threads[i].start()
    
    #等待所有结束线程
    for i in nloops:
        threads[i].join()
    
    print 'all end:', ctime()

if __name__ == '__main__':
    main()
