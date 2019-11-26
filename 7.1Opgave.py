from pcinput import getInteger

i=0
teller=0
totaal = getInteger("geef een nummer: ")
while teller < 10:
    totaal *= teller
    i += 1

    print(str(i) +" * "+ str(totaal) str(totaal))
