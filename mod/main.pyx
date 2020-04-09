
from . cimport mathic
from .mathic cimport plus
from .advancedmath import minus

from libcpp.map cimport map as hashmap

from math import pi


cdef hashmap[int, unsigned long long] memo 
cpdef unsigned long long fib(long n):
    if memo.find(n) != memo.end(): 
        print('found in memo!', n)
        return memo[n]
    if n <= 1:
        memo[n] = n
        return n
    memo[n] = plus( fib( minus(n,1) ), fib( minus(n,2) ))
    return memo[n]

cdef void hello(int i):
    print(i, end='HELLO HEHE')

print(fib(10), pi)
