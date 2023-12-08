unique = [3,3,3,3,3,3,0,5,3,3]

def find_unique(list):
    for x in list:
        if list.count(x) == 1:
            return x
print(find_unique(unique))


import random

print("GUESS THE NUMBER")

a = int(input("Qaysi sondan boshlansin : "))
b = int(input("Qaysi songacha bo'lsin : "))

num = random.randrange(a,b+1)



while True:
    son = int(input("Find the numb!: "))

    if son > num :
        print("High")

    elif son < num :
        print("Low")

    elif son == num:
        print("Correct answer!")
        break

a = int(input("Enter :"))

def number():
    if a> 1802 and a<1900:
        print("19 th century")

    elif a> 1901 and a<2000:
        print("20 th century")

    elif a>2001 and a>2024:
        print("21 th century")
