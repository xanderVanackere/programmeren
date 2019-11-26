from pcinput import getString

# vraagt of het de eerste keer is
eersteKeer = getString("Is dit de eerste keer dat je inlogt? ")

#controlleert of het de eerste keer is
if eersteKeer == "ja":

    # vraagt de naam en wachtwoord
    naam = getString("Wat is uw naam? ")
    wachtwoord = getString("Wat is uw wachtwoord? ")

else:

    wijzigen = getString("Wens je het wachtwoord te wijzigen? ")

    #kijken voor het wachtwoor te wijzigen of niet
    if wijzigen == "ja":
        wachtwoord = getString("Geef het nieuwe wachtwoord in. ")


    else:

        naam = getString("Wat is uw naam? ")
        wachtwoord = getString("Wat is uw wachtwoord? ")

        # controlleert of het correct is of niet
        if naam == "Jolien" and wachtwoord == "knutselKnuts":
            print("Welkom Jolien")
        else:
            print("Ik ken je niet")







