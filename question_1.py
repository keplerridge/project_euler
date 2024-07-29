##########################################
# Author: Kepler Ridge
# Date: 7/29/24
# Prompt: If we list all the natural numbers below 10 that are multiples of 3, 5, 6, and 9.
# The sum of these multiples is 23. Find the sum of all multiples of 3 or 5 below 1000.
##########################################

#%%
def is_multiple(x):
    if x % 3 == 0 or x % 5 == 0:
        return True
    else:
        return False

total = 0

#%%
for num in range(1000):
    if is_multiple(num):
        total += num

print(total)

# Answer: 233168