Instance: Sporanox-10mgml-Solution-SE-IS-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(Sporanox-10mgml-Solution-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(Sporanox-10mgml-Solution-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(Sporanox-10mgml-Solution-SE-IS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000091697 "Itraconazole"


* substance.strength.concentrationRatio.numerator = 10 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000091697 "Itraconazole"

* substance.strength.referenceStrength.strengthRatio.numerator = 10 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"