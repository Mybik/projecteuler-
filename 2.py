'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

numbers = [1, 2]
while numbers[-1] < 4000000:
    numbers.append(numbers[-1] + numbers[-2])
numbers.pop()


even_valued_terms = []
for i in numbers :
    if i % 2 == 0:
        even_valued_terms.append(i)
print(sum(even_valued_terms))