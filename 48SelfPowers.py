"""
Project Euler number 48
The sequence 1^1 + 2^2 +...+10^10 sums up to
10405071317. Find the last ten digits of this
sequence when the last term is 1000^1000.
"""
limit = int(input("Provide limit: "))
print(sum([(x ** x) for x in range(1, limit + 1)]))