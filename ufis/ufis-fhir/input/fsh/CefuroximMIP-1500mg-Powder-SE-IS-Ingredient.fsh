Instance: CefuroximMIP-1500mg-Powder-SE-IS-Ingredient
InstanceOf: PPLIngredient

* status = #active
* for[0] = Reference(CefuroximMIP-1500mg-Powder-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(CefuroximMIP-1500mg-Powder-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(CefuroximMIP-1500mg-Powder-SE-IS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000091436 "cefuroxime sodium"


* substance.strength.concentrationRatio.numerator = 1578 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000092667 "cefuroxime"

* substance.strength.referenceStrength.strengthRatio.numerator = 1500 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"