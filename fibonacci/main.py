import sys
import time  
from fibonacci.calculator import FibonacciCalculator

if len(sys.argv) <= 1:
    print('Error: Index value must be provided')
    exit()

try:
    number = int(sys.argv[1])

    start = time.time()
    result = FibonacciCalculator.calculate(number)
    end = time.time()

    print('Result: {0}'.format(result))
    print('Obtained in {0} seconds'.format((end - start)))
except Exception as ex:
    print('Error: {0}'.format(ex))



