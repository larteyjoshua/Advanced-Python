numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
n = [12, 54, 33, 67, 24, 89, 11, 24, 47]

print ([num for num in numbers if num>=0])
print ([num for num in n if num%2==0])
print ([num for num in n if num%2==1])

words = ["hello", "my", "name", "is", "Sam"]
print ([((word.upper()),len(word)) for word in words if len(word)])