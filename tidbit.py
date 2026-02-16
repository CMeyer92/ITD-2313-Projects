purchase_price = float(input("Input purchasing price: "))

DOWN_PAYMENT_RATE = 0.10
ANNUAL_RATE = 0.12
MONTHLY_RATE = ANNUAL_RATE / 12
MONTHLY_PAYMENT_RATE = 0.05

down_payment = purchase_price * DOWN_PAYMENT_RATE
balance = purchase_price - down_payment
monthly_payment = purchase_price * MONTHLY_PAYMENT_RATE

print("Month\tBalance\t\tInterest\tPrincipal\tPayment\t\tRemaining")

month = 1

while balance > 0:
    interest = balance * MONTHLY_RATE
    principal = monthly_payment - interest

    if principal > balance:
        principal = balance
        monthly_payment = interest + principal

    remaining_balance = balance - principal

    print(
        month, "\t",
        format(balance, ".2f"), "\t",
        format(interest, ".2f"), "\t\t",
        format(principal, ".2f"), "\t\t",
        format(monthly_payment, ".2f"), "\t\t",
        format(remaining_balance, ".2f")
    )

    balance = remaining_balance
    month += 1
