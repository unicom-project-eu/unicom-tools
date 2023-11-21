Instance: Mydrane-InjSol-SE-AJ-Ingredient03
InstanceOf: PPLIngredient

* status = #active
* for[0] = Reference(Mydrane-InjSol-SE-AJ-MedicinalProductDefinition)
* for[+] = Reference(Mydrane-InjSol-SE-AJ-ManufacturedItemDefinition)
* for[+] = Reference(Mydrane-InjSol-SE-AJ-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000091954 "Tropicamide"


* substance.strength.concentrationRatio.numerator = 0.2 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000091954 "Tropicamide"

* substance.strength.referenceStrength.strengthRatio.numerator = 0.2 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"