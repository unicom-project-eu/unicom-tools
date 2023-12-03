Instance: MorphineUni-1mgml-Solution-SE-BS-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(MorphineUni-1mgml-Solution-SE-BS-MedicinalProductDefinition)
* for[+] = Reference(MorphineUni-1mgml-Solution-SE-BS-ManufacturedItemDefinition)
* for[+] = Reference(MorphineUni-1mgml-Solution-SE-BS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000090494 "Morphine hydrochloride"


* substance.strength.concentrationRatio.numerator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000091372 "Morphine"

* substance.strength.referenceStrength.strengthRatio.numerator = 0.76 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"