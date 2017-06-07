word=raw_input("Enter the Text: ")
n=0
m=n-1
while not word.isalpha():
    print ("Enter only texts...\n")
    word=raw_input("Enter the Text: ")
else:
    while True:
        try:
            if word[n]==word[m]:
                n+=1
                m=m-1
            else:
                print ("%s is not a Palindrome..." %word)
                break
        except IndexError:
            print ("%s is a Palindrome..!!:" %word)
            break
