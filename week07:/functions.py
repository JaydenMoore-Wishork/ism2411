# Self assesment 1. The first bug I found was the missing : and I found that one just by reading through it. 2. It applies a discount based on a price and tier the imputs are price and tier it returns a total. 3. I used Ai to help locate bugs in the broken_sales.py file its helped build my understanding but it also shortcutted it because I didnt have to go through trial and error.

#Exercise 1 
def calculate_tax(price, rate):
    return price * rate 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax1:.2f}")
print(f"Tax for $350 at 5%: ${tax1:.2f}")


#Exersice 2 

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price 

#Exercise 3 

original_price = 200

for tier in ["gold", "silver", "bronze" "none"]:
    print(f"(teir): ${apply_discount(original_price, tier):.2f}")

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax 


print(f"final_prive(200, 0.07, 'gold') = $(final_price(200, 0.07, 'gold'):.2f)")

#exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")


#exercise 5 

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")

count = 0
for sale in sales: #add the : on the end
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): #remove the =
    print(sales[i])
    i += 1




#Exercise 6 

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)







