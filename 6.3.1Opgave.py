from pcinput import getFloat

score = getFloat("geef je score op")

if score >=8.5 :
    print("A")
elif score == 8 or score == 7.5 :
    print("B")
elif score == 6.5 or score == 7 :
    print("C")
elif score == 6 or score == 5.5 :
    print("D")
else:
    print("F")
