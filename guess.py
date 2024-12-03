from functools import reduce
numbers =list(int(num) for num in input("Enter a number:").split())

mapped_numbers = list(map(lambda x: x, numbers)) 
even=list(filter(lambda x : x%2==0 , numbers))
odd=list(filter(lambda x : x%2!=0 , numbers))

sum_of_even= reduce(lambda acc, x: acc + x, even, 0)
sum_of_odd= reduce(lambda acc, x: acc + x, odd, 0)

print("Original List:", numbers)
print("even list:",even)
print("odd list:",odd)
print("Sum of even Values:", sum_of_even)
print("Sum of odd Values:", sum_of_odd)