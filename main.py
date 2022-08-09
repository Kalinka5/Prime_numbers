# testing1 with input number from keyboard
def testing1():
    try:
        # check the integer positive number
        print('Test 1...\n')
        number = int(input("Enter your number: "))
        assert number > 0, 'Number must be positive!'
        print(is_prime(number))
        print(f"\nAll prime numbers to {number} - {list(prime_generator(number))}")
        print(multiplication(number))
    except ValueError:
        print('\nIt`s not an integer number!!!!!')
        print('Please enter integer number.')
    else:
        print('Test 1 completed...\n')
    print('-'*70)


# testing2 with list of numbers
def testing2(*numbers):
    print('\nTest 2...\n')
    print(f'{numbers}\nPrime numbers: {list(filter(prime, numbers))}')
    print('\nTest 2 completed...')
    

# check number is prime or not
def prime(numb):
    if numb < 1:
        return 0
    elif numb == 1:
        return numb
    for n in range(2, numb):
        if numb % n == 0:
            return 0
    return numb


# again check number is prime or not, but return string result
def is_prime(numb):
    if prime(numb) == 0:
        return 'It`s NOT a PRIME NUMBER!'
    return 'It`s a PRIME NUMBER!'


# make range of prime numbers
def prime_generator(numb):
    for n in range(numb + 1):
        if is_prime(n) == "It`s a PRIME NUMBER!":
            yield n


# print all prime multipliers of number
def multiplication(numb):
    n = numb
    multipliers = []
    denominator = 2
    if numb == 1:
        return '1 = [1]'
    elif is_prime(numb) == 'It`s a PRIME NUMBER!':
        return f'\n{numb} = {[1, numb]} - all multipliers\n'
    else:
        while denominator * denominator <= numb:
            if numb % denominator == 0:
                multipliers.append(denominator)
                numb //= denominator
            else:
                denominator += 1
        multipliers.append(numb)
        return f'\n{n} = {multipliers} - all multipliers\n'


# first testing
testing1()

# second testing
testing2(-17, 11, 176, 47, 29)
