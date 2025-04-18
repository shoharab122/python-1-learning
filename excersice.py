time=int(input("Enter th time in 24 hour format:"))

if (time<12):
    print("Good Morning")
elif (time<17):
    print("Good Afternoon")
elif (time<20):
    print("Good Evening")
else:
    print("Good Night")

while True:
    time=int(input("Enter the time in 24 hour format:"))

    if (time<12):
        print("Good Morning")
    elif (time<17):
        print("Good Afternoon")
    elif (time<20):
        print("Good Evening")
    else:
        print("Good Night")

    repeat = input("Do you want to run the program again? (yes/no): ")
    if str(repeat).lower() != 'yes':
        break


#another exercise 
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
print("shoharab".lower().count("h"))
