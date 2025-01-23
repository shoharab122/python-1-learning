#if else
a=int(input('Enter you age:'))
print("your age is",a)
print(a==18)
print(a<=18)
print(a>=18)
print(a<18)
print(a>18)
print(a!=18)
if(a>18):
    print("You can go to the website")
elif(a<50):
     print("you can also use this website")
else:
     print("you can't use this website")

     #use this symble to clarify (<=,==,>=,<,>,!=)
#nested loop in python 
for i in range(1, 6):  # Outer loop: Rows
    for j in range(1, 6):  # Inner loop: Columns
        print(f"{i * j:2}", end=" ")  # Print product, aligned
    print()  # Move to the next line after each row

