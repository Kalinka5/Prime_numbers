# check number is prime or not 
def isPrime(numb):
    if numb < 1:
        return "It`s NOT a prime number!"
    elif numb == 1:
        return "It`s a PRIME NUMBER!"
    for n in range(2, numb):
        if numb % n == 0:
            return "It`s NOT a prime number!"
    return "It`s a PRIME NUMBER!"

# make range of prime numbers
def primeGenerator(numb):
    for n in range(int(numb + 1)):
        if isPrime(n) == "It`s a PRIME NUMBER!":
            yield n
            
# again check number is prime or not, but return not string
def Prime(numb):
    if numb < 1:
        return 0
    elif numb == 1:
        return numb
    for n in range(2, numb):
        if numb % n == 0:
            return 0
    return numb

# print all prime multipliers of number
def multiplication(numb):
    multipliers = []
    denominator = 2
    if isPrime(numb) == 'It`s a PRIME NUMBER!':
        return (f'{numb} = {[1, numb]}')
    else:
        while denominator * denominator <= numb:
            if numb % denominator == 0:
                multipliers.append(denominator)
                numb //= denominator
            else:
                denominator += 1
        multipliers.append(numb)
        return (f'{number} = {multipliers}')

# first testing
number = int(input("Enter your number: "))
# second testing
numbers = [4, 11, 176, 22, 29]

# first testing
print('\n' + str(isPrime(number)))
print("\nAll prime numbers to " + str(number) + " - " + str(list(primeGenerator(number))))
print('\n' + multiplication(number) + ' - all multipliers')
print('---------------------------------------------------------')
# second testing
print('\n' + str(numbers) + ' - Prime numbers: ' + str(list(filter(Prime, (numbers)))))