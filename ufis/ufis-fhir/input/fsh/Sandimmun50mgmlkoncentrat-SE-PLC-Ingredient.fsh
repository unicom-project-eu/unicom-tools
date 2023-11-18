Instance: Sandimmun50mgmlkoncentrat-SE-PLC-Ingredient
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-02T13:09:40.586+00:00"
* status = #active
* for[0] = Reference(Sandimmun50mgmlkoncentrat-SE-PLC-MedicinalProductDef)
* for[+] = Reference(Sandimmun50mgmlkoncentrat-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(AdministrableProductDefinition/Sandimmun50mgmlkoncentrat-SE-PLC-AdminProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000092121 "Ciclosporin"


* substance.strength.concentrationRatio.numerator = 50 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000092121 "Ciclosporin"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"

* substance.strength.referenceStrength.strengthRatio.numerator = 50 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"