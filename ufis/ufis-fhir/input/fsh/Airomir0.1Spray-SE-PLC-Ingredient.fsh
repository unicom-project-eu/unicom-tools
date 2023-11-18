Instance: Airomir0.1Spray-SE-PLC-Ingredient
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "3"
* meta.lastUpdated = "2022-06-29T07:42:20.708+00:00"
* status = #active
* for[0] = Reference(Airomir0.1Spray-SE-PLC-MedicinalProductDefinition)
* for[+] = Reference(Airomir0.1Spray-SE-PLC-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinition/Airomir0.1Spray-SE-PLC-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000090564 "Salbutamol sulfate"
* substance.strength.presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.presentationRatio.numerator = 0.12 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002163 "Actuation"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000091629 "salbutamol"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"

* substance.strength.referenceStrength.strengthRatio.numerator = 0.1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002163 "Actuation"