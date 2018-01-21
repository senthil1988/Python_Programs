ui=raw_input("Enter Your Text Here: ")

while not ui.isalpha():
    print "Enter only texts!!"
    ui=raw_input("Enter Your Text Here: ")
count=0
y=count-1
ui=ui.lower()
for x in list(ui):
    if x==list(ui)[y]:
        y-=1
    else:
        print ("Text You Entered '%s' is Not a palindrome..!!" %ui)
        exit()
print ("Text You Entered '%s' is a palindrome." %ui)
