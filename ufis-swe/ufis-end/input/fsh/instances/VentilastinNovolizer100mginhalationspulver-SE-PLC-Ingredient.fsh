Instance: VentilastinNovolizer100mginhalationspulver-SE-PLC-Ingredient
InstanceOf: Ingredient
Usage: #inline
* status = #active
* for[0] = Reference(VentilastinNovolizer100mginhalationspulver-SE-PLC-MedProdDef)
* for[+] = Reference(VentilastinNovolizer100mginhalationspulver-SE-PLC-ManuItemDef)
* for[+] = Reference(VentilastinNovolizer100mginhalationspulver-SE-PLC-AdminiProdDef)
* role = $100000072050_1#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition_1#100000090564 "Salbutamol sulfate"
* substance.strength.presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.presentationRatio.numerator = 120 https://spor.ema.europa.eu/v1/lists/100000110633#100000110656 "microgram(s)"
* substance.strength.presentationRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002163 "Actuation"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition_1#100000091629 "salbutamol"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength.strengthRatio.numerator = 100 https://spor.ema.europa.eu/v1/lists/100000110633#100000110656 "microgram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/200000000014#200000002163 "Actuation"