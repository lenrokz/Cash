import cs50
dollars = cs50.get_float("Change owed: ")
cents = round(dollars *100)
coins = 0
if dollars <= 0:
    
while cents >= 25:
    cents -=25
    coins += 1
while cents >= 10:
    cents -= 10
    coins += 1
while cents >= 5:
    cents -= 5
    coins += 1
while cents >= 1:
    cents -= 1
    coins += 1
print(f"{coins}")
