# The goal of this python challenge is to take in a number n, 
# and preform the fibonacci sequence for n number of times. 
# It then needs to count the number of occurrences for each 
# digit 0-9, and sort in decending order by the number of occurences.

def fib_digits(n, signature = [1, 1]):
    [signature.append(sum(signature[-2:])) for i in range(n-2)]
    signature = [int(d) for d in str(''.join(str(signature[-1])))]
    tuples = list(zip([signature.count(i) for i in range(10)], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    tuples = [tuples for tuples in tuples if tuples[0] != 0]
    tuples.sort(key = lambda item:item[0], reverse=True)
    return tuples
