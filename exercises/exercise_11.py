# Exercise 11
satisfied = False
num = 0
money = []
add = 0


dollars_needed = int(input("How much do you need to give: "))#
dollar_types = [500, 100, 10, 5, 1]
while satisfied == False:
    for i in dollar_types:
        add = dollars_needed // i
        money.append(add)
        dollars_needed = dollars_needed - (add * i)
        num += dollars_needed
        if dollars_needed == 0:
            satisfied = True
            break

if len(money) > 0:
    five_hundreds = money[0]
    # print("Number of Five Hundreds:", five_hundreds)
    print(f"{five_hundreds}(500)")
else:
    five_hundreds = 0 
    print("Number of Five Hundreds:", five_hundreds)
    print(f"{five_hundreds}(500)")
if len(money) > 1:
    hundreds = money[1]
    # print("Number of Hundreds:", hundreds)
    print(f"{five_hundreds}(500){hundreds}(100)")
else:
    hundreds = 0 
    print("Number of Hundreds:", hundreds)

if len(money) > 2:
    tens = money[2]
    # print("Number of Tens:", tens)
    print(f"{five_hundreds}(500){hundreds}(100){tens}(10)")
else:
    tens = 0 
    print("Number of Tens:", tens)

if len(money) > 3:
    fives = money[3]
    print("Number of Fives:", fives)
    print(f"{five_hundreds}(500){hundreds}(100){tens}(10){fives}(5)")
else:
    fives = 0 
    print("Number of Fives:", fives)

# if len(money) > 4:
#     twos = money[4]
#     print("Number of Twos:", twos)
# else:
#     twos = 0 
#     print("Number of Twos:", twos)

if len(money) > 4:
    ones = money[4]
    print("Number of Ones:", ones)
    print(f"{five_hundreds}(500){hundreds}(100){tens}(10){fives}(5){ones}(1)")
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

