wnumber=(1,2,3,4,4)
print("the following is the tuple: ",wnumber)
print("the first element in the tuple: ",wnumber[0])
#print(count("4"))
print("the maximum number is: ",max(wnumber))
print("the minimum number is: ",min(wnumber))
enumber=(2,4,6,8,10)
print("the tuple of even number: ",enumber)
number=wnumber+enumber
print("the combination of two tuples: ",number)
num=int(input("Enter a number: "))
if num in number:
    print(num," is found")
else:
    print(num," is not found")

print("the length of the tuple: ",len(number))
nam=[11,12,13,14,15,16]
print("the list is: ",nam)
print("we are changing the list to tuple")
tapl=tuple(nam)
print("this is tuple from list: ",tapl)

