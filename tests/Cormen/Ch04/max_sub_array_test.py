import Cormen.Ch04.max_sub_array as algos

def test_find_max_subarray():
    test_array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    st_idx, end_idx, sum = algos.find_max_subarray(0,15, test_array)
    assert sum == 43


def test_find_max_subarray_brute_force():
    test_array = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    st_idx, end_idx , sum = algos.find_max_subarray_brute_force(0,15,test_array)
    assert st_idx == 7
    assert end_idx == 10
    assert sum == 43


def test_linear_max_subarray():
    test_array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    st_idx, end_idx, sum = algos.linear_max_subarray_solution(test_array)
    assert st_idx == 7
    assert end_idx == 10
    assert sum == 43


