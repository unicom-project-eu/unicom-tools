Instance: Zoladex-10.8mg-Solution-SE-IS-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(Zoladex-10.8mg-Solution-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(Zoladex-10.8mg-Solution-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(Zoladex-10.8mg-Solution-SE-IS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000086673 "Goserelin acetate"


* substance.strength.concentrationRatio.numerator = $100000000008#100000165006 "quantity sufficient"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#200000025238 "dose"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000084238 "Goserelin"

* substance.strength.referenceStrength.strengthRatio.numerator = 10.8 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#200000025238 "dose"