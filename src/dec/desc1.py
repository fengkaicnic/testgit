def deco(func):
    print 'hello'   
    def wrap(*args):
        print '123'
        print args
        print func  
    return wrap

@deco
def foo(acb='1234'):
    print 'Now in foo()'
    pass

if __name__ == '__main__':
    foo('1235')

#foo()
#foo()