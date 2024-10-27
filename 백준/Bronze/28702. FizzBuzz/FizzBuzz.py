A = input()
B = input()
C = input()

if not(A =="FizzBuzz" or A =="Fizz" or A =="Buzz"):
      #B = int(A)+1
      C= int(A)+2
elif not(B =="FizzBuzz" or B =="Fizz" or B =="Buzz"):
      #A = int(B)-1
      C = int(B)+1
# elif not(C =="FizzBuzz" or C =="Fizz" or C =="Buzz"):
#       #A = int(C)-2
#       #B = int(C)-1
#       C = int(C)
else:
      # A = int(A)
      # B = int(B)
      C = int(C)

D = C+1
if D%3==0 and D%5==0:
      print("FizzBuzz")
elif D%3==0 and D%5!=0:
      print("Fizz")
elif D%3!=0 and D%5==0:
      print("Buzz")
else:
      print(D)