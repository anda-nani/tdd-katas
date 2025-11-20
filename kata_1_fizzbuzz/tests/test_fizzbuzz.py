import src.fizzbuzz as fizzbuzz

def test_returns_fizz_for_multiples_of_3():
    assert fizzbuzz.fizzbuzz(3) == 'Fizz'
    assert fizzbuzz.fizzbuzz(6) == 'Fizz'
    assert fizzbuzz.fizzbuzz(9) == 'Fizz'

def test_returns_for_multiples_of_5():
    assert fizzbuzz.fizzbuzz(5) == 'Buzz'
    assert fizzbuzz.fizzbuzz(10) == 'Buzz'
    assert fizzbuzz.fizzbuzz(25) == 'Buzz'

def test_returns_fizzbuzz_for_multiples_of_3_and_5():
    assert fizzbuzz.fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz.fizzbuzz(30) == 'FizzBuzz'
    assert fizzbuzz.fizzbuzz(45) == 'FizzBuzz'