Instance: SandimmunNeoral100mgmlorallos-SE-PLC-Ingredient03
InstanceOf: PPLIngredient
Usage: #inline

* status = #active
* for[0] = Reference(SandimmunNeoral100mgmlorallos-SE-PLC-MedicinalProductDef)
* for[+] = Reference(SandimmunNeoral100mgmlorallos-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(AdministrableProductDefinition/SandimmunNeoral100mgmlorallos-SE-PLC-AdminProductDef)
* role = $100000072050#100000072082 "Excipient"
* substance.code.concept = $SubstanceDefinition#100000079902 "Macrogolglycerol hydroxystearate"


* substance.strength.concentrationRatio.numerator = 5 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000079902 "Macrogolglycerol hydroxystearate"

* substance.strength.referenceStrength.strengthRatio.numerator = 5 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"