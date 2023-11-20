'''def pattern(n):
    for i in range(n):
        for j in range(i):
            print('*' ,end=" ")
        print('  ')
    for i in range(n,0,-1):
        for j in range(i):
          print('*',end=" ")
        print(' ')
n=int(input("enter the number of rows: "))
pattern(n)
def longestWord(word):
    max_length=len(word[0])
    for item in word:
        length=len(item)
        if length>max_length:
            max_length=length
    return max_length
words=input("enter a list of words seperated by spaces:")
word=words.split()
result=longestWord(word)
print(f"the length of the longestWord is:{result}")
def find_factors(number):
    factors = []
    for i in range(1,number + 1):
        if number % i == 0:
            factors.append(i)
    return factors
num=int(input("enter the number of rows: "))
result = find_factors(num)
print(f"the factors of{num} are: {result}")'''
square_area= lambda a: a**2
rectangle_area= lambda l, b: l * b
triangle_area= lambda ba, h: 0.5 * ba * h

a = int(input("enter the length: "))
print("area of the square:",square_area(a))

l = int(input("enter the length: "))
b = int (input("enter the breadth: "))
print("area of the triangle:", rectangle_area(1,b))

ba = int(input("enter the base: "))
h = int(input("enter the height: "))
print("area of the rectangle:", triangle_area(ba,h))

                      
