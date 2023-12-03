Instance: TPTDteva-2080-Solution-SE-IS-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(TPTDteva-2080-Solution-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(TPTDteva-2080-Solution-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(TPTDteva-2080-Solution-SE-IS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000089193 "Teriparatide"


* substance.strength.concentrationRatio.numerator = 0.25 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "milliliter(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000089193 "Teriparatide"

* substance.strength.referenceStrength.strengthRatio.numerator = 0.25 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "milliliter(s)"