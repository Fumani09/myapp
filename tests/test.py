from myapp import myModule

def test_new_count():
        """
        Make sure your function is correct
        """

assert myModule.new_order([8,5,3]) == [3,5,8], 'incorrect'
assert myModule.new_order([87,9,112,33]) == [9,33,87,112], 'incorrect'
assert myModule.new_order([65,45,44,22]) == [22,44,45,65], 'incorrect'