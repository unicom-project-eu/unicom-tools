Instance: MorfinSpecial-2mgml-Solution-SE-BS-Ingredient
InstanceOf: PPLIngredient
Usage: #inline

* status = #active
* for[0] = Reference(MorfinSpecial-2mgml-Solution-SE-BS-MedicinalProductDefinition)
* for[+] = Reference(MorfinSpecial-2mgml-Solution-SE-BS-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinition/MorfinSpecial-2mgml-Solution-SE-BS-AdministrableProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000090494 "Morphine hydrochloride"


* substance.strength.concentrationRatio.numerator = 2 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000091372 "Morphine"

* substance.strength.referenceStrength.strengthRatio.numerator = 1.519 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"