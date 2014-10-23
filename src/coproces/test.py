def coroutine(func):
    def ret():
        f = func()
        f.next()
        return f 
    return ret

@coroutine
def consumer():
    print 'waiting to get a task'
    while 1:
        n = (yield)
        print 'get %s' % n

import time
def producer():
    c = consumer()
    i = 1
    while 1:
        time.sleep(2)
        print 'send a task to consumer'
        c.send(i)
        i += 1
        
        
if __name__ == '__main__':
    producer()        