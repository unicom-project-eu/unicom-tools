Instance: Enalapril-Vitabalans-5mg-Tablet-EE-I
InstanceOf: PPLIngredient
Usage: #inline

* status = #active
* for[0] = Reference(Enalapril-Vitabalans-5mg-Tablet-EE-MPD)
* for[+] = Reference(Enalapril-Vitabalans-5mg-Tablet-EE-MID)
* for[+] = Reference(AdministrableProductDefinition/Enalapril-Vitabalans-5mg-Tablet-EE-APD)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000091343 "Enalapril maleate"
* substance.strength.presentationRatio.numerator = 5 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "Tablet"