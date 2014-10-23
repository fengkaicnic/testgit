'''
Created on 

@author: Administrator
'''

class A(object):
    def __init__(self):
        self.name = '2'
        

def main():

    ac = A()
    strss = getattr(ac, 'name', 1)
    strs1 = getattr(ac, 'name1', 5)
    print strss, strs1
    

if __name__ == '__main__':
    main()