
for i in range(3):
    x=input("Enter the PIN code: ")
    if x=="0805":
        print("Correct")
        break
    else:
        print("incorrect")
else:
    print("Sorry, your payment card has been blocked.")