##########################################
# Author: Kepler Ridge
# Date: 7/29/24
# Prompt: 2520 is the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20.
##########################################
#%%
def divisibility_check(num):
    if num % 2 == 0 and num % 3 == 0 and num % 4 == 0 and num % 5 == 0 and num % 6 == 0 and num % 7 == 0 and num % 8 == 0 and num % 9 == 0 and num % 10 == 0 and num % 11 == 0 and num % 12 == 0 and num % 13 == 0 and num % 14 == 0 and num % 15 == 0 and num % 16 == 0 and num % 17 == 0 and num % 18 == 0 and num % 19 == 0 and num % 20 == 0:
        return True
    return False

found = False

#%%
tracker = 20
while found is not True:
    if divisibility_check(tracker):
        print(tracker)
        found = True
    else:
        tracker += 20

# Answer: 232792560