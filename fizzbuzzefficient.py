def divisible_by(numerator, denominator):   # Defining a modular operator
    if numerator % denominator == 0:
        return True


fizz_dict = {  # Creating a dictionary for all the fizzbuzz cases
    3: "Fizz",
    5: "Buzz",
    7: "Bang",
    11: "Bong",
    13: "Fezz"
}

current = []
limit = input('How many numbers would you like to go up to (non-inclusive)?:')

for i in range(1, int(limit)):              # Cycling over each number from 1 to our max
    for j in range(len(fizz_dict)):         # Cycling over each fizzbuzz case
        num = list(fizz_dict)[j]            # Checking if our number is divisible by each case
        if i % num == 0:
            current.append(fizz_dict[num])  # if it is, we append the key word to our list
        if i % 17 == 0:
            current.reverse()               # if divisible by 17 we reverse our list
    if not current:                         # if we had no cases, print regular number
        print(i)
    else:
        current = "".join(current)          # if we had some cases, turn list -> string and print
        print(current)
    current = []


