# Exercise 11
satisfied = False
num = 0
money = []
add = 0


dollars_needed = int(input("How much do you need to give: "))#
dollar_types = [500, 100, 10, 5, 2, 1,"placeholder"]
while satisfied == False:
    for i in dollar_types:
        add = dollars_needed // i
        money.append(add)
        dollars_needed = dollars_needed - (add * i)
        num += dollars_needed
        if dollars_needed == 0:
            satisfied = True
            print(money)
            break
five_hundreds = money[0]
hundreds = money[1]
tens = money[2]
fives = money[3]
twos = money[4]
print("The denominations breakdown is as follows:")
print("Number of Five Hundreds:", five_hundreds)
print("Number of Hundreds:", hundreds)
print("Number of Tens:", tens)
print("Number of Fives:", fives)
print("Number of Twos:", twos)
if len(money) > 5:
    ones = money[5]
else:
    ones = 0 
    print("Number of Ones:", ones)



# add = dollars_needed // i
# if i == 500:
#     money[0] = add
# elif i == 100:
#     money[1] = add
# elif i == 10:
#     money[2] = add
# elif i == 5:
#     money[3] = add
# elif i == 2:
#     money[4] = add
# else:
#     money[5] = add


    # if money[5] > 1:
    #     ones = money[5]

# hundreds = dollars_needed // 100
# tens = dollars_needed // 10 % 10
# ones = dollars_needed % 10
# if ones % 2 == 1:
    
# print(hundreds)
# print(tens)
# print(ones)

