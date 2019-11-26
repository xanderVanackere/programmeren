from pcinput import getInteger

x = getInteger("geef een gewicht op")

print(x)

if x > 20:
    print("Er moet een toeslag van 25$ betaald worden voor bagage die zwaarder is")
elif x < 20:
    print("Goede reis!")
else:
    print("Dat gewicht is precies goed!")
