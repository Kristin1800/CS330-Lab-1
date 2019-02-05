# Kristin Goselin - FizzBuzz Program

for num in range(1, 100):  # A loop that goes through numbers 1 - 100
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')  # if the numbers are divisible by three or five print out FizzBuzz
    elif num % 3 == 0:
        print('Fizz')  # if the numbers are divisible by three print out Fizz
    elif num % 5 == 0:
        print('Buzz')  # if the numbers are divisible by five print out Buzz
    else:
        print(num)  #otherwise print out the according number
