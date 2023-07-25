from programs import factorial


def test_factorial():
    assert factorial.fact(0) == 1
    assert factorial.fact(2) == 2
    assert factorial.fact(5) == 120
    assert factorial.fact(10) == 3628800
    assert factorial.fact(20) == 2432902008176640000
