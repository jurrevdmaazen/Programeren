#heb eerst twee variable gemaakt, "uur_loon" en "uren_gewerkt" alles wat je hier intypt woord aan de bijbehoorende-
#variables teruggegeven, bij print heb ik er een string in verwerkt met onder andere de variables-
#omdat de waardes die bij "input" zijn gegeven strings zijn geworden moet het voor de berekening omgezet worden naar-
#float als dat eenmaal is uitgerekend moet het weer naar een string omgezet worden, vandaar die lange regel.

uur_loon = input ("wat verdien je per uur: " )

uren_gewerkt = input ("Hoeveel uur heb je gewerkt: ")

print (uren_gewerkt + " uur werken levert " + str((float(uur_loon) * float(uren_gewerkt))) + " euro op")
