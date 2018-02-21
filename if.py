user_input = input("Please enter your age ")
try:
    reply = ""
    user_age = int(user_input)
    if user_age <= 6:
        reply = "Kindergarten"
    elif user_age <= 17:
        reply = "School"
    elif user_age <= 23:
        reply = "Univercity"
    else:
        reply = "Job"
    print (reply)
except:
    print ("The age is supposed to be a number")