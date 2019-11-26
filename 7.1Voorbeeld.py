from pcinput import getInteger

num = 1

while num <=5:
    print(num)
    num+=1
print("klaar")

totaal=0
teller=0

while teller < 5:
    totaal += getInteger("geef een nummer: ")
    teller +=1
print("totaal is "+ str(totaal))

num=-1
teller=0

while num != 0:
    num = getInteger("geef een nummer: ")
    teller += num
print("totaal is "+ str(teller))



fruit = "banaan"

for letter in fruit:
    print(letter)
    if letter == "n":
        fruit = "mango"

print("klaar")
print(fruit)
