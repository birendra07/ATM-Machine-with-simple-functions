import mysql.connector as mc
db = mc.connect(host = 'localhost', user= 'root', password = '*B2i9#ren0', database = 'atmlogin'  )
cur = db.cursor()

a = 1 
while (a <= 3 ):
    print("*" * 40)
    print("********* ATM OPERATIONS **********")
    print("enter your pin number.")
    entered = int(input())
    query = 'SELECT * FROM logindetails'
    cur.execute(query)
    rez = cur.fetchall()
    for el in rez:
        i = 0
        if el[0] == entered:
            print("Congratulations!, You have successfully logged in.")
            i += 1
            break
        else:
            pass
    if i == 1:
        print("*" * 40)
        balance = 999

        print("1.Withdraw")
        print("2.Balance enquiry")
        print("3.Exit")
        choice = int(input("Enter your choice:  "))
        if (choice <= 3 and choice >= 1):
            if (choice == 1):
                print("Enter the amount you want to withdraw: ")
                print("Note: You can only withdraw Rs.500 and Rs.1000 notes.")
                amount = int(input("Rs. "))
                if (amount >=  500 and amount <= 10000):
                    if (amount <= balance):
                        print("Please collect your cash carefully.")
                        balance = balance - amount
                        print(f"your A/C xxxxxxxxxxxxx869 has been debited by Rs. {amount}, available balance is Rs. {balance}.")
                    else:
                        print("Insufficient Balance.")
                        print(f"Available balance is Rs. {balance}.")
                else:
                    print("Please, Enter the amount between Rs. 500 and Rs. 10000.")
            elif (choice == 2):
                print(f"Available balance is Rs. {balance}.")
            else:
                print("Thank you for using SBI ATM. \nHave a nice and great time.")
                
        else:
            print("Please, enter number 1,2,3 only.")
        

    else:
        a += 1
        if a < 3:
            print("Sorry, You have entered incorrect pin no.\nPlease!, enter your correct PIN no.")
        else: 
            print("Sorry, You literally missed three chances.")

                    
                
            
        