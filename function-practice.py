#function for find mas_number of 3 numbers
def max_number(a, b, c):
    return max([a,b,c])
print(max_number(5,8,10))

#funtion called mult_list() to multiply all the numbers in a list
def mult_list(numbers):
    total = 1
    for x in numbers:
        total *= x 
    return total
print(mult_list((2,4,6)))

 #function called rev_string() to reverse a string.
def rev_string(x):
  return x[::-1]

mytxt = rev_string("It is a beautiful day!")

print(mytxt)
   
#function called num_within() to check whether a number falls in a given range
def num_within(x):
    if x in range(5,9):
        print( "%s is in range"%str(x))
    else :
        print("Out of range.")
num_within(6)
num_within(10)
        
#Python function called pascal() that prints out the first n rows of Pascal's triangle
def pascal(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal(1) 
pascal(5)
    