def foo():
    a = [1]
    def bar():
        a[0] = a[0]+1
        return a[0]
    print a[0]
    bar()
    print a[0]
    return bar()

ac = foo()
print ac
