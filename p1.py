def credit_card_penalty(balance, days):
    if days < 15:
        return balance*.05
    elif days < 30 and days >= 15:
        return balance * .10
    elif days < 60 and days >= 31:
        return balance * .15
    else:
        return balance * .20

print "Penalty 1: ", credit_card_penalty(15000, 18)
print "Penalty 2: ", credit_card_penalty(7000, 31)
print "Penalty 3: ", credit_card_penalty(300, 70)
print "Penalty 4: ", credit_card_penalty(1000, 3)
