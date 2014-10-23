def hf():
    print 'ehtoy'
    t = yield 1
    print t
    print 'wen chuan'
    m = yield 5
    print m
    d = yield 12
    print d
    print 'We are together'
    
if __name__ == '__main__':
    c = hf()
    print c.send(None)
    print c.send('Fighting!')
    print c.send('abcdefc')
