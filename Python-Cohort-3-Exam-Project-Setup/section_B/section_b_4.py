#number4(a)
def calculate_bonus(salary, years_of_service):
    if years_of_service > 4:
        bonus = 0.08 * salary
    elif years_of_service == 3:
        bonus = 0.05 * salary
    else:
        bonus = 0
    return bonus

while True:
    try:
        salary = float(input("Enter your salary: "))
        years_of_service = int(input("Enter your years of service: "))
        
        if years_of_service < 0:
            print("Years of service cannot be negative.")
            continue
        
        bonus = calculate_bonus(salary, years_of_service)
        net_salary = salary + bonus
        
        print(f"Net bonus amount: {bonus}")
        print(f"Net salary amount: {net_salary}")
        
        choice = input("Do you want to calculate again? (yes/no): ").lower()
        if choice != "yes":
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
#calling the function
calculate_bonus()




# # number4_(b)

def sacco_transactions():

    accountBalance = 0
    run = 1

    while run == 1:

        print("\nWelcome to, UTAMUGuild Sacco.")

        print('1. Deposit Money')
        print('2. Withdraw Money')
        print('3. Check Balance')


        studentChoice = int(input("Enter your selection from (1,2,or 3): "))

        #making  the transactions basing on what the student has selected 

        if studentChoice == 1:

            print('\n.Processing a deposit transaction.')
            depositAmount =  int(input("Enter the  amount to be deposited: "))

            #check if deposit amount is less than 1000
            if depositAmount < 1000:

                print('\nMinimum deposit is 1000')

            else:
                accountBalance += depositAmount

                print(f'Dear student, you have deposited {depositAmount:,} and your new account balance is {accountBalance:,}')


        elif studentChoice == 2:
            print('\n...Processing a withdraw transaction...')
            withdrawAmount =  int(input("Enter amount to be withdrawn: "))

            if accountBalance == 0:

                print("Your balance is 0") 

            elif withdrawAmount < 500:

                print("Mininum withdraw amount is 500")

            elif withdrawAmount > accountBalance:

                print(f"Withdraw failed, insufficient funds")

            else:
                accountBalance -= withdrawAmount
                print(f'Dear student, you have withdrawn {withdrawAmount:,} and your new account balance is {accountBalance:,}')

            
        elif studentChoice == 3:
            print(f'Your account balance is {accountBalance:,}')
        else:
            print("You entered  a wrong choice!! Please select 1, 2, or 3\n")


        run = int(input("Enter 1 to continue or any number to exit: "))

        if run!=1:
            print("Thanks for using our sacco")
            break
#calling the function
sacco_transactions()


#number4(c)
# importing the laibrary
import math

def value_of_d():
    
    X1 = int(input('Enter the value of X1:\t'))  
    X2 = int(input('Enter the value of X2:\t'))
    Y1 = float(input('Enter the value of Y1:\t')) 
    Y2 = float(input('Enter the value of Y2:\t')) 

    simplifiedExpression = (X1-X2) ** 2 + (Y1-Y2) ** 2
    d = math.sqrt(simplifiedExpression)
    #return d
    print("The value of d is: %.2f " %d + " ")
    
#calling the function  
value_of_d()

