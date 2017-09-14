#je krijgt eerst te vraag hoe oud je bent en daarna de vraag of je een nederlands paspoort heb. Bij vaiable "leeftijd"-
#heb ik "eval" gezet vanwege de sting omgezet moet worden naar een integer. De if statement luid, if (als) de ingevulde-
#"leeftijd"gelijk of hoger is dan 18 en als "paspoort" gelijk is aan "ja" dan wordt de zin "Gefeliciteerd je mag stemmen"-
#geprint. Alle fouten antwoorden (else) worden omgezet naar "Helaas je mag niet stemmen"
leeftijd = eval(input("Geef je leeftijd: "))
paspoort = (input("Ben je in bezit van een Nederlands paspoort? "))

if leeftijd >= 18 and paspoort == "ja":
    print("Gefeliciteerd je mag stemmen")
else:
    print("Helaas je mag niet stemmen")