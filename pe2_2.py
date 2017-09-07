#ik denk dat ik voor de onderstaande vakken deze cijfers ga behalen. Daarna heb ik bij variable "gemiddelde" alle-
#cijfers in float bij elkaar opgeteld en gedeeld door 3, daarnaast heb ik het cijfer afgerond. Bij de variable-
#"beloning" heb ik weer alles bij elkaar opgeteld en vermenigvuldigd met 30. en bij het de variable "overzicht"-
#heb ik alles op een rijdje gezet en de float waardes die bij de variables "gemiddelde" en "beloning" uitkomen doormiddel-
#van het omzetten van float naar een string in de tekst verwerkt. Daarnaast heb ik na elke variable een print gemaakt
#zodat het totale overzicht van waardes te zien is.

cijferICOR = 7
cijferPROG = 6
cijferCSN = 7

gemiddelde = (round(float(float(cijferCSN) + float(cijferICOR) + float(cijferPROG))/3))
print("Gemiddelde: " + str(gemiddelde))

beloning = (float(float(cijferCSN) + float(cijferPROG) + float(cijferICOR) )* 30)
print ("Beloning:","€",beloning)

overzicht = ("Mijn cijfers zijn gemiddeld afgerond een " + str(gemiddelde) +" leveren een beloning van " + str(beloning) + " op.")
print (overzicht)
