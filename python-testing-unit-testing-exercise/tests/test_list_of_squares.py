from programs import list_of_squares


def test_list_of_squares():
    assert list_of_squares.list_of_squares(1)[1] == 1
    assert list_of_squares.list_of_squares(2)[2] == 4
    assert list_of_squares.list_of_squares(3)[3] == 9
    assert list_of_squares.list_of_squares(4)[4] == 16
    assert list_of_squares.list_of_squares(5)[5] == 25
    assert list_of_squares.list_of_squares(6)[6] == 36