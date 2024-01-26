Instance: Fragmin-10000IEml-Solution-SE-IS-Ingredient
InstanceOf: Ingredient
Usage: #inline
* status = #active
* for[0] = Reference(Fragmin-10000IEml-Solution-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(Fragmin-10000IEml-Solution-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(Fragmin-10000IEml-Solution-SE-IS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000091301 "dalteparin sodium"
* substance.strength.concentrationRatio.numerator.extension.url = "http://terminology.hl7.org/CodeSystem/v3-NullFlavor"
* substance.strength.concentrationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000165006 "quantity sufficient"
* substance.strength.concentrationRatio.numerator = $100000110633#100000110671 "international unit(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition_1#100000127573 "dalteparin"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"
* substance.strength.referenceStrength.strengthRatio.numerator = 10000 http://spor.ema.europa.eu/v1/lists/100000110633#100000110671 "international unit(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"