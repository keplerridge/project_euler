##########################################
# Author: Kepler Ridge
# Date: 7/29/24
# Prompt: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.
# What is the 10001st prime number?
##########################################
#%%
def prime_check(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

found = False
tracker = 2
primes_list = []

#%%
while found is not True:
    if prime_check(tracker):
        primes_list.append(tracker)
        tracker += 1
        if len(primes_list) == 10001:
            final_prime = primes_list[-1]
            found = True
    else:
        tracker += 1

# Answer: 104743