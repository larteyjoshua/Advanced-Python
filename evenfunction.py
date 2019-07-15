'''number = int(input("Please the number "))'''

def even_num(number):
    if number%2==0:
        return True
   
    else:
        return False
'''print(even_num(2))'''

numbers = [1,56,234,87,4,76,24,69,90,135]
print ([num for num in numbers if (even_num(num))])
print ([num for num in numbers if not(even_num(num))])
