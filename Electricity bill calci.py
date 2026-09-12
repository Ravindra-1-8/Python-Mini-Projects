# Electricity Bill Generator.
# 100 below units = 5 per unit.
# 101 - 200 units = 7 per unit.
# 201 - 300 units = 10 per unit.
# 300 above units = 15 per unit.

# Example:

# 78 units = 78 * 5
# But when 105 units = (100 * 5), remaining (5 * 7)

def bill_calci(units):

    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    elif units <= 300:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    else:
        bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 15)
    return bill

units = float(input("Enter units: "))
total_bill = bill_calci(units)

print(f"Total bill: {units}, units = {total_bill}/-")