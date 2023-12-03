Instance: Fragmin-2500IE-Solution-SE-IS-Ingredient
InstanceOf: PPLIngredient
* status = #active
* for[0] = Reference(Fragmin-2500IE-Solution-SE-IS-MedicinalProductDefinition)
* for[+] = Reference(Fragmin-2500IE-Solution-SE-IS-ManufacturedItemDefinition)
* for[+] = Reference(Fragmin-2500IE-Solution-SE-IS-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000091301 "dalteparin sodium"
* substance.strength.concentrationRatio.numerator.extension.url = "http://terminology.hl7.org/CodeSystem/v3-NullFlavor"


* substance.strength.concentrationRatio.numerator = $100000110633#100000110671 "international unit(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000127573 "dalteparin"

* substance.strength.referenceStrength.strengthRatio.numerator = 2500 http://spor.ema.europa.eu/v1/lists/100000110633#100000110671 "international unit(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)"