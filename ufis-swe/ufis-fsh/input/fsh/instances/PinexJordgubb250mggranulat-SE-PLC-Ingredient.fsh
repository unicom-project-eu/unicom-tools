Instance: PinexJordgubb250mggranulat-SE-PLC-Ingredient
InstanceOf: Ingredient
Usage: #inline
* status = #active
* for[0] = Reference(PinexJordgubb250mggranulat-SE-PLC-MedicinalProductDef)
* for[+] = Reference(PinexJordgubb250mggranulat-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(PinexJordgubb250mggranulat-SE-PLC-AdminProductDef)
* role = $100000072050_1#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition_1#100000090270 "Paracetamol"
* substance.strength.presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.presentationRatio.numerator = 250 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002143 "Sachet"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition_1#100000090270 "Paracetamol"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength.strengthRatio.numerator = 250 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002143 "Sachet"