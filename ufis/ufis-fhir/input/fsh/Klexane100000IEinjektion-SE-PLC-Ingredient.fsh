Instance: Klexane100000IEinjektion-SE-PLC-Ingredient
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-24T16:55:35.703+00:00"
* status = #active
* for[0] = Reference(Klexane100000IEinjektion-SE-PLC-MedicinalProductDef)
* for[+] = Reference(Klexane100000IEinjektion-SE-PLC-ManufacturedItemDef)
* for[+] = Reference(AdministrableProductDefinition/Klexane100000IEinjektion-SE-PLC-AdminProductDef)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000090152 "Enoxaparin sodium"
* substance.strength.concentrationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.concentrationRatio.numerator = 100000 https://spor.ema.europa.eu/v1/lists/100000110633#100000110671 "international unit(s)"
* substance.strength.concentrationRatio.denominator = 10 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000085598 "Enoxaparin"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength.strengthRatio.numerator = 100000 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "international unit(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 10 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"