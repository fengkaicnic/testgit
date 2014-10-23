from single import Singleton

@Singleton
class Foo:
    def __init__(self, **kwargs):
        print 'Foo created'
        print kwargs
f = Foo() # Error, this isn't how you get the instance of a singleton

h = Foo.Instance() # Good. Being explicit is in line with the Python Zen
g = Foo.Instance() # Returns already created instance

print h is g # True
print id(f)
print id(h)
print id(g)