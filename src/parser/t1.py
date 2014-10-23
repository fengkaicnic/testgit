import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-echo", nargs='?', default='echo', const='foo')
print parser
args = parser.parse_args('-echo'.split())
print args