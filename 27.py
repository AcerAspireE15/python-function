# 1
def student_discount(x):
    return x-(x*10)/100

def additional_discount(y):
    return y-(y*5)/100

result = additional_discount(student_discount(100))
print(result)

# 2
def student_discount(price):
    price = price - (price * 10) / 100
    return price


def additional_discount(newprice):
    newprice = newprice - (newprice * 5) / 100
    return newprice


selling_price = 100

# applying both discounts simultaneously

print(additional_discount(student_discount(selling_price)))