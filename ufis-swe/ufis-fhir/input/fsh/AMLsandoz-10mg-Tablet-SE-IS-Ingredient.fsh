Instance: AMLsandoz-10mg-Tablet-SE-IS-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(AMLsandoz-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(AMLsandoz-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(AMLsandoz-10mg-Tablet-SE-IS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000090079 "Amlodipine besilate"
* substance.strength.presentationRatio.numerator = 13.87 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000085259 "Amlodipine"

* substance.strength.referenceStrength.strengthRatio.numerator = 10 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"