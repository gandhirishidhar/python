"""
Calculate the sum of the first n natural numbers.

Examples:
	sum of n = 1 + 2 + 3 + ... + n
	sum of 1 = 1
	sum of 2 = 1 + 2
	sum of 3 = 1 + 2 + 3
	sum of 4 = 1 + 2 + 3 + 4
	sum of 5 = 1 + 2 + 3 + 4 + 5
	sum of 6 = 1 + 2 + 3 + 4 + 5 + 6
	sum(1) = 1
	sum(2) = 1 + 2
	sum(3) = 1 + 2 + 3
	sum(4) = 1 + 2 + 3 + 4
	sum(5) = 1 + 2 + 3 + 4 + 5
	sum(6) = 1 + 2 + 3 + 4 + 5 + 6
"""

def sum(n):
    if n == 1:
        return 1
    return sum(n-1) + n

print(sum(199))
