'''
Created on 

@author: Administrator
'''
from models import CONF

def main():
    print CONF
    
def whtest():
    abc = True
    while abc:
        vmstat = 'testwhle'
        abc = False
    if not abc:
        print 'this is abc'
    print vmstat
    
    
if __name__ == '__main__':
    
    for its in CONF.__dict__.iterkeys():
        print CONF.__dict__[its]
    
    whtest()