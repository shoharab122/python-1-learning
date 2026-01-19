#for loops is use for iterating over a sequence (list,tuple,dictionary or string)
books = ["Python Basics", "AI for Beginners", "Cloud Computing Guide"]

for book in books:
    print(book)

#while loops is use for repeatedly execting a block of code as long as the condition is true 
correct_password = "cloud123"
attempt = ""

while attempt != correct_password:
    attempt = input("Enter your password: ")
    if attempt == correct_password:
        print("Login Successful!")
    else:
        print("Wrong password, try again.")


        #range is use to generate a sequence of numbers 
        for i in range(1, 6):
         print(f"Displaying book {i}")

         #practise
         correct_password= "cloud12321"
         attempt = ""
         while attempt != correct_password:
            attempt= input("Enter your password:")
            if attempt == correct_password:
                print("Login Successfull")
            else:
               print("wrong password,try again")
        #practise

    correct_password = "shoharab123"
    attempts_left = 3
    while attempts_left > 0:
        attempt = input("Enter your password: ")
        if attempt == correct_password:
            print("Login successful")
            break
        else:
            attempts_left -= 1
            if attempts_left > 0:
                print(f"Wrong password, try again. Attempts left: {attempts_left}")
            else:
                print("No attempts left. Access denied.")
#practise
with open("server_logs.txt", "r") as file:
    for line in file:
        print(line.strip())  # Process each line
