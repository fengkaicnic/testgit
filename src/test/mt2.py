'''
Created on
@author: Administrator
'''

from models import CONF
import pdb
    
if __name__ == '__main__':
    CONF.address = 'mt2address'
    CONF.age = 27
    CONF.name = 'mt2name'
    for its in CONF.__dict__.iterkeys():
        print its
        print CONF.__dict__[its]
    print CONF.age