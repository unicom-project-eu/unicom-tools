Instance: NitroglycerinAbicurinfu-SE-PLC-Ingredient
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-13T16:18:20.009+00:00"
* status = #active
* for[0] = Reference(NitroglycerinAbicurinfu-SE-PLC-MedicinalProductDef)
* for[+] = Reference(NitroglycerinAbicurinfu-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(AdministrableProductDefinition/NitroglycerinAbicurinfu-SE-PLC-AdminProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000087614 "Glyceryl trinitrate"


* substance.strength.concentrationRatio.numerator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000087614 "Glyceryl trinitrate"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"

* substance.strength.referenceStrength.strengthRatio.numerator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"