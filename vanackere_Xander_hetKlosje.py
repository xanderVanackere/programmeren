from pcinput import getString

# vraagt de naam en wachtwoord
naam = getString("Wat is uw naam? ")
wachtwoord = getString("Wat is uw wachtwoord? ")

# controlleert of het correct is of niet
if naam == "Jolien" and wachtwoord == "knutselKnuts":
    print("Welkom Jolien")
else:
    print("Ik ken je niet")
