Instance: Smofkabiven-Emulsion-SE-IS-Ingredient03
InstanceOf: PPLIngredient
Usage: #inline

* status = #active
* for[0] = Reference(Smofkabiven-Emulsion-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(Smofkabiven-Emulsion-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinition/Smofkabiven-Emulsion-SE-IS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* function = $200000004946#200000004948 "Specified Substance Group 1 to Parent"
* substance.code.concept = $SubstanceDefinition#100000090106 "Calcium chloride dihydrate"


* substance.strength.concentrationRatio.numerator = 0.74 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000076563 "Calcium chloride anhydrous"

* substance.strength.referenceStrength.strengthRatio.numerator = 0.56 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"