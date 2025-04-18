users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status



  #practise 
local_password="shoharab3421"
attempt="3"
while attempt != local_password:
    attempt=input("Enter your password:")
    if attempt==local_password:
        print('Login successfull')
    else: 
        print("Wrong pasword,try again") 
        #practise 
     
#practise

import time

lights = ["Red", "Green", "Yellow"]
index = 0

while True:
    print(f"Traffic light: {lights[index]}")
    time.sleep(1)  # Wait 3 seconds before changing
    index = (index + 1) % len(lights)  # Cycle through lights
        #practise
        #traffic light simulation
import time

lights = [("Red", 3), ("Green", 2), ("Yellow", 1)]
index = 0

while True:
    color, duration = lights[index]
    print(f"Traffic light: {color}")
    time.sleep(duration)
    index = (index + 1) % len(lights)
#pracitise
import time 
lights = [("Red", 3), ("Green", 2), ("Yellow", 1)]
index =0
while True :
    colour ,duration = lights[index]
    print(f"Traffic LIght;;{colour}")
    time.sleep(duration)
    index= (index+1)% len(lights)