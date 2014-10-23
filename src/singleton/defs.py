from single import Singleton 

@Singleton
def testsig():
    print 'this is the testing'
    
    
if __name__ == '__main__':
    print 'this is the ts'
    testsig()
    
    