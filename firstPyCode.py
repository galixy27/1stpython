pinCode = 5555
bankBalance = 8
pinAttempt = 5555
withdrawAttempt = 7

if pinAttempt != pinCode:
    print('pincode invalid')
elif pinAttempt == pinCode and withdrawAttempt > bankBalance:
    print('insufficient funds')
else:
    print('money withdrawral succesful your remaining balance is:'),
    print(bankBalance - withdrawAttempt)
    