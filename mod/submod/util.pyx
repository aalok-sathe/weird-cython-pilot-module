
from libcpp.vector cimport vector
from libcpp.string cimport string

cdef void imprint(list stuff):
    cdef object s
    for s in stuff:
        print(s, end=' . ')
    print()
