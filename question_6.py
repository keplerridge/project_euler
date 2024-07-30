##########################################
# Author: Kepler Ridge
# Date: 7/29/24
# Prompt: The sum of the squares of the first ten natural numbers
# is 1^2 + 2^2 + ... + 10^2 = 385.
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first
# ten natural numbers and the square of the sum is
# 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first
# 100 natural numbers and the square of the sum.
##########################################
#%%
def sum_of_squares(num):
    sum = 0
    for i in range(0, num + 1):
        sum = sum + i**2
    return sum

def square_of_sums(num):
    sum = 0
    for i in range(0, num + 1):
        sum += i
    return sum**2

result = square_of_sums(100) - sum_of_squares(100)

# Answer: 25164150