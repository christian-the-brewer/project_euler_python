# A palindromic number reads the same both ways. The largest palindrome made from the product of two -digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Attempt 1
# start from largest 3 digit numbers and work down
# product of odd/even numbers is always odd/even, could that help?

# define 3 digit numbers
MAX = 999
MIN = 100

# function to check is palindrome


def is_palindrome(num):
    reversed = str(num)[::-1]
    if str(num) == reversed:
        return True
    else:
        return False


# Could we check all numbers for palindrome from largest possible from two 3 digit numbers?
# No, because we would need to check all factors.

print(is_palindrome(101))
