Instance: EnoxaparinLedraxen2000IEinjektion-SE-PLC-Ingredient
InstanceOf: Ingredient
Usage: #inline
* status = #active
* for[0] = Reference(EnoxaparinLedraxen2000IEinjektion-SE-PLC-MedicinalProductDef)
* for[+] = Reference(EnoxaparinLedraxen2000IEinjektion-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(EnoxaparinLedraxen2000IEinjektion-SE-PLC-AdminProductDef)
* role = $100000072050_1#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition_1#100000090152 "Enoxaparin sodium"
* substance.strength.concentrationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.concentrationRatio.numerator = 20 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 0.2 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition_1#100000085598 "Enoxaparin"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength.strengthRatio.numerator = 2000 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "international unit(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 0.2 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"