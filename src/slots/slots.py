class base(object):
    v=1
    def __init__(self):
        pass
    

class base1(object):
    v=2
    
    __slots__='a'
    
    def __init__(self):
        pass
    
if __name__ == '__main__':
    b = base()
    b1 = base1()
    b.x = 3
#    b1.x = 5
    b1.a = 7
    
    print b.x
#    print b1.x
    print b1.a
    print b.__dict__
    b1.a = 8
    print b1.a
#    print b1.__dict__