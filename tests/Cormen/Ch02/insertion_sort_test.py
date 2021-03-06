import Cormen.Ch02.insertion_sort as algos
import random

def test_insertion_sort_desc_ex_2dot1_2():
    A = [5,3,4,2,1]
    B = algos.insertion_sort(A,1)
    result = [5,4,3,2,1]
    assert len(B) == len(result)
    assert B == result

def test_ex_2dot1_1():
    A = [31,41,59,26,41,58]
    B = algos.insertion_sort(A,0)
    result = [26,31,41,41,58,59]
    assert len(B) == len(result)
    assert B == result

def test_insertion_sort_2dot3_4():
    A = [random.randint(1,100) for i in range(500)]
    expected = sorted(A)
    B = algos.insertion_sort_2dot3_4(A)
    assert len(B) == len(expected)
    assert B == expected

