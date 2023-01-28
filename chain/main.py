import sys 
from chain.checker import ChainChecker

if len(sys.argv) <= 1:
    print('Error: List of words must be provided')
    exit()

try:
    input = sys.argv[1]
    words = [w.strip() for w in input.split(',')]

    checker = ChainChecker()

    print(str(words))
    print('Input is Chain: {0}'.format(checker.list_is_chain(words)))
except Exception as ex:
    print('Error: {0}'.format(ex))



