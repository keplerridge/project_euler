##########################################
# Author: Kepler Ridge
# Date: 7/29/24
# Prompt: A palindrome number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
##########################################
#%%
def palindrome_check(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

palindrome_list = []

#%%
for i in range(100, 1000):
    print(i)
    for j in range(100, 1000):
        if palindrome_check(i * j):
            palindrome_list.append(i * j)

largest = max(palindrome_list)

# Answer: 906609
