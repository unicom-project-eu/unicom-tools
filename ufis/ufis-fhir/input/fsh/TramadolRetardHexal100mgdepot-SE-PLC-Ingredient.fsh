Instance: TramadolRetardHexal100mgdepot-SE-PLC-Ingredient
InstanceOf: PPLIngredient

* status = #active
* for[0] = Reference(TramadolRetardHexal100mgdepot-SE-PLC-MedicinalProductDef)
* for[+] = Reference(TramadolRetardHexal100mgdepot-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(TramadolRetardHexal100mgdepot-SE-PLC-AdminProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000093275 "Tramadol hydrochloride"
* substance.strength.presentationRatio.numerator = 100 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "Tablet"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000077198 "Tramadol"

* substance.strength.referenceStrength.strengthRatio.numerator = 87.95 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "Tablet"