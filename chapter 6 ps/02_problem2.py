marks1 =  int(input("Enter marks 1: "))
marks2 = int(input("Entyer marks 2: "))
marks3 = int(input("Enter masrks 3: "))

# check or percentage
total_percentage = (marks1+ marks2 + marks3)/300

if(total_percentage>=40):
    print("You are pass")
else:
    print("Fail")
