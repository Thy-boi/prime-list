# Establishing the lists and checker variable (used in the loop)
numbers = []
prime = []
checker = 0

# Starting off with a range loop that gets the range of numbers you want

num_range = int(input("What's the maximum range you would like to find prime numbers?\n"))

# With the range chosen, it loops through the numbers and appends them to a list, which gets the numbers in the range
for ee in range(1, num_range + 1):
    numbers.append(ee)


for number in numbers:
    # It gets a number, and since prime numbers are only divisible by themselves and 1, that means there are only 2 factors. All other operations should fail. So, I added a checker.
    checker = 0
    for x in range(1, number):
        if number % x != 0:
            # The checker adds 1 to itself every time the number fails the modulo operation (Which means it failed to cleanly divide)
            checker += 1


    if checker == (number - 2):
        #  If the checker equals the number (minus 2), then it will add it to the prime number list. If not, it resets when it gets a new number, and starts the process all over again.
        prime.append(number)

# From there, I print the prime numbers, then I added them together, and print the sum.

print(f"Prime numbers: {prime}")

print(f"Sum of numbers: {sum(prime)}")

