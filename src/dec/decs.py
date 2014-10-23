def spann(fn):
    def new(*kxc):
        print 'decorator new'
        print kxc
        fn(*kxc)
        print 'decorator end'
        print 'merge'
    return new
@spann
def meth1(a,b):
    print a
    print b
if __name__ == '__main__':
    meth1('1', 'd')

    