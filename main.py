# testing1 with input number from keyboard
def testing1():
    number = int(input("Enter your number: "))
    assert number > 0, 'Number must be positive!'
    print('\n' + str(isPrime(number)))
    print("\nAll prime numbers to " + str(number) + " - " + str(list(primeGenerator(number))))
    print(multiplication(number))
    print('-'*50)


# testing2 with list of numbers
def testing2(*numbers):
    print('\n' + str(numbers) + ' - Prime numbers: ' + str(list(filter(Prime, numbers))))


# check number is prime or not
def Prime(numb):
    if numb < 1:
        return 0
    elif numb == 1:
        return numb
    for n in range(2, numb):
        if numb % n == 0:
            return 0
    return numb


# again check number is prime or not, but return string result
def isPrime(numb):
    if Prime(numb) == 0:
        return 'It`s NOT a PRIME NUMBER!'
    return 'It`s a PRIME NUMBER!'


# make range of prime numbers
def primeGenerator(numb):
    for n in range(int(numb + 1)):
        if isPrime(n) == "It`s a PRIME NUMBER!":
            yield n


# print all prime multipliers of number
def multiplication(numb):
    n = numb
    multipliers = []
    denominator = 2
    if numb == 1:
        return '1 = [1]'
    elif isPrime(numb) == 'It`s a PRIME NUMBER!':
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
testing2(4, 11, 176, 47, 29)
