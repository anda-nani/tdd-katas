def fizzbuzz(number: int) -> str:
    """Return 'Fizz' for multiples of 3, 'Buzz' for multiples of 5,
    'FizzBuzz' fo multiples of both 3 and 5, or the number itself otherwise.
    """
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)  