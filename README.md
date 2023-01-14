# refundScripting
automate refund script as a command

## AS-IS
1. access to server (django shell)
2. make and account object with Business license number
3. check whether account's balance is equal to query result
4. give a refund
5. check again whether account's balance is equal to query result ( should be 0 )

## TO-BE
1. upload CSV files
2. execute `python3 manage.py giverefund`