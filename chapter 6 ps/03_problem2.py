# Spam detetctor:  To fonda spam comment by detecting the text containing the following words:
#"make lots of money", "buy now" "Subscribe this", "click this".  

# to write a program to detect these spams

p1 = "make lots of money"
p2 = "buy now"
p3 = "Subscribe this"
p4 = "click this"

message =  input("enter your comment")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print( "this is a spam")

else:
    print("This comment is not a spam")
    


