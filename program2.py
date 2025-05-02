import time
print("Welcome to Canara Bank")
print("Insert your Card")
password=1234
Balance=10000
check=int(input("Press 1.Yes 2.No"))
if check==1:
    print("Select the language")
    print("1.English\n 2.Kannada\n 3.Telugu\n 4.Malayalam")
    choice=int(input())
    if choice==1:
        print("Enter your Pin")
        pin=int(input())
        if pin==password:
            print("Select the option")
            print("1.Balance Enquiry\n 2.Withdrawal")
            choice1=int(input())
            if choice1==1:
                print("Your available balance",Balance)
            elif choice1==2:
                print("Enter your Amount")
                Amount=int(input())
                if Amount % 100 ==0 and Amount <= Balance:
                   print("Please wait for the transaction")
                   time.sleep(3)
                   print("Please collect your cash")
                   print("Do you want to check your Balance?")
                   print("1.Yes\n 2.No")
                   choice2=int(input())
                   if choice2==1:
                       print("Your available Balance is:",Balance-Amount)
                       print("Thank you. Visit again")
                else:
                    print("insufficient balance")
                    print("your available balance is", Balance)
            else:
                print("Selected wrong option")
        else:
            print("Wrong Pin")


    else:
        print("Please select English")
else:
    print("Insert your Card properly")