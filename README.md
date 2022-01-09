# ATM-Machine-with-simple-functions
An ATM, or automated teller machine, is a specialized computer that makes managing a bank account holder's funds more convenient. 
It enables users to check account balances, make cash withdrawals or deposits, print a record of account activities or transactions, and even buy stamps.
ATMs were first utilized in London in 1967, and now they may be found all throughout the country after 50 years.

ATMs can be located on-site or off-site. In financial institutions, on-premise ATMs are located. 
Clients benefit from increased choice, convenience, and availability, while banks benefit 
from increased transaction revenue, reduced operational expenses, and increased staff resources.
Off-premise ATMs are often situated in places where there is a simple need for cash, 
such as airports, grocery and convenience stores, and shopping complexes.

In this project, an user is provided with simple and limited services of ATM Machine.
The balance of every user is supposed to be Rs. 999, and The user can withddraw only Rs. 500 for now,
I am currently working in this project so I would like to store the balance of users corresponding to their
pin number. At first, the user is asked to enter pin number and around 11 pin no. have been stored in database.
So, using MySQL connector, I m able to check whether the user typed pin number matches the stored pin number
or not. If the pin number is matched, then providing the user with the facility like withdrawing, printing
statement, and exit. If the user typed pin doesn't match then the user can get two more times in order to 
try to type correct pin number. If the user name doesn't match up to the third time then the session is expired
and the process begins from beginning.
