def isPrime(number):
    if number < 1:
        return "It`s NOT a prime number!"
    elif number == 1:
        return "It`s a PRIME NUMBER!"
    for n in range(2, number):
        if number % n == 0:
            return "It`s NOT a prime number!"
    return "It`s a PRIME NUMBER!"

def primeGenerator(number):
    for n in range(int(number + 1)):
        if isPrime(n) == "It`s a PRIME NUMBER!":
            yield n

def Prime(number):
    if number < 1:
        return 0
    elif number == 1:
        return number
    for n in range(2, number):
        if number % n == 0:
            return 0
    return number

def multiplication(numb):
    multipliers = []
    denominator = 2
    number = numb
    if isPrime(numb) == 'It`s a PRIME NUMBER!':
        return '{} = {}'.format(numb, [1, numb])
    else:
        while denominator * denominator <= numb:
            if numb % denominator == 0:
                multipliers.append(denominator)
                numb //= denominator
            else:
                denominator += 1
        multipliers.append(numb)
        return '{} = {}'.format(number, multipliers)
            
number = int(input("Enter your number: ")) 
#numbers = [4, 11, 176, 22, 29]

print('\n' + str(isPrime(number)))
print("\nAll prime numbers to " + str(number) + " - " + str(list(primeGenerator(number))))
print('\n' + multiplication(number) + ' - all multipliers')
#print('\n' + str(numbers) + '\n\nPrime numbers are ' + str(list(filter(Prime, (numbers)))))