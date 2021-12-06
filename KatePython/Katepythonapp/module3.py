print("Mon\tTues\tWed")

number = format(12345.6789, '.2f')
print(number)

amount_due = 5000.0
monthly_payment = amount_due / 12
print("The monthly payment is", format(monthly_payment, '.2f'))

monthly_pay = 5000.00
annual_pay = monthly_pay * 12
print("Your annual pay is $", format(annual_pay, ',.2f'), sep='')
