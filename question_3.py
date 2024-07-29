##########################################
# Author: Kepler Ridge
# Date: 7/29/24
# Prompt: The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number 600851475143
##########################################
#%%
def largest_prime_factor(number):
    if number <= 1:
        return None

    largest_factor = None

    while number % 2 == 0:
        largest_factor = 2
        number //= 2

    factor = 3
    while factor * factor <= number:
        while number % factor == 0:
            largest_factor = factor
            number //= factor
        factor += 2

    if number > 2:
        largest_factor = number

    return largest_factor

factor = largest_prime_factor(600851475143)

# Answer: 6857