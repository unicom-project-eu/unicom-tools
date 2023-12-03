Instance: NitroglycerinAbicurinfu-SE-PLC-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(NitroglycerinAbicurinfu-SE-PLC-MedicinalProductDef)
* for[+] = Reference(NitroglycerinAbicurinfu-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(NitroglycerinAbicurinfu-SE-PLC-AdminProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000087614 "Glyceryl trinitrate"


* substance.strength.concentrationRatio.numerator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000087614 "Glyceryl trinitrate"

* substance.strength.referenceStrength.strengthRatio.numerator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"