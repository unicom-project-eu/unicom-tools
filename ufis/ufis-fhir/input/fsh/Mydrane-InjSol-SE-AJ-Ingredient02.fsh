Instance: Mydrane-InjSol-SE-AJ-Ingredient02
InstanceOf: PPLIngredient
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-11-10T17:25:48.289+00:00"
* status = #active
* for[0] = Reference(Mydrane-InjSol-SE-AJ-MedicinalProductDefinition)
* for[+] = Reference(Mydrane-InjSol-SE-AJ-ManufacturedItemDefinition)
* for[+] = Reference(AdministrableProductDefinitionMydrane-InjSol-SE-AJ-AdministrableProductDefinition)
* role = $100000072050#100000072072 "Active"
* substance.code.concept = $SubstanceDefinition#100000160254 "Phenylephrine hydrochloride ph. eur."


* substance.strength.concentrationRatio.numerator = 3.1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.concentrationRatio.denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $SubstanceDefinition#100000088260 "Phenylephrine"
* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"

* substance.strength.referenceStrength.strengthRatio.numerator = 2.54 https://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"
* substance.strength.referenceStrength.strengthRatio.denominator = 1 https://spor.ema.europa.eu/v1/lists/100000110633#100000110662 "millilitre(s)"