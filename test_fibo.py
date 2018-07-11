import fibo


def test_fibo_10():
    result = fibo.fib2(10)
    expected_result = [0, 1, 1, 2, 3, 5, 8]
    assert result == expected_result


def test_fibo_0():
    result = fibo.fib2(0)
    expected_result = []
    assert result == expected_result


def test_fib_5():
    result = fibo.fib2(5)
    expected_result = [0, 1, 1, 2, 3]
    assert result == expected_result

    
def test_fib_type():
    result = fibo.fib2(5)
    assert type(result) == list
