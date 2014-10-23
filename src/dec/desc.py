def outer(f):
    print 'some message com from outer function'
    def inner(*arg):
        print 'before function'
       # f(3, 6)
        print 'after function'
    return inner

#
#
@outer
def func(a, b):
    print func.__name__
    print 'a = %s, b = %s' % (a, b)

if __name__=='__main__':
    print 'start'
    func()
    print 'end'