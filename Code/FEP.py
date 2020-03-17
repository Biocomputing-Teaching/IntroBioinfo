def function(n):
    """Print prime number up to n."""
    print 'prime numbers up to ', n
    i=0
    for x2 in range(-n, n+1):
        print x2,x2**2

def fib(n):    
    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    print '\nFibonacci serie up to ', n
    a, b = 0, 1
    while b<n:
        print b,
        a,b=b,a+b


n0 = int(raw_input("Please enter an integer: "))

if n0 < 0:
    n0 = abs(n0)
    print 'Negative changed to absolute value', x
function(n0)