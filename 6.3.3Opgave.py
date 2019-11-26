from pcinput import getString

woord= getString("geef een woord of zin: ")
tell=0

if "a" in woord or "A" in woord:
    tell+= 1

if "e" in woord or "E" in woord:
    tell+= 1

if "i" in woord or "I" in woord:
    tell+= 1

if "o" in woord or "O" in woord:
    tell+= 1

if "u" in woord or "U" in woord:
    tell+= 1

if tell==0:
    print("er zijn geen klinkers")
elif tell==1:
    print("er is 1 klinker")
else:
    print("er zijn "+str(tell)+" verschillende klinkers")
