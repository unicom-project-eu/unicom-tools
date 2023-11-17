Instance: Zoladex-3.6mg-Implant-EE-PPD-1002621
InstanceOf: PackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-08-14T19:15:01.191+00:00"
* extension.url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"
* extension.valueQuantity = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002150 "Syringe"
* identifier.system = "http://ema.europa.eu/example/pcid"
* identifier.value = "EE-EE-100014112-12130-1002621"
* packageFor = Reference(Zoladex-3.6mg-Implant-EE-MPD)
* description = "Üht implantaati sisaldav Safe System nõela kaitsva kattega süstel."
* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072172 "Estonian"
* marketingStatus.country = $100000000002#100000000388 "Republic of Estonia"
* marketingStatus.status = $100000072052#100000072083 "Marketed"
* package.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.type.coding.code = "100000073498"
* package.type.coding.display = "Box"
* package.quantity = 1
* package.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.material.coding.code = "200000003529"
* package.material.coding.display = "Cardboard"
* package.package.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.package.type.coding.code = "100000073544"
* package.package.type.coding.display = "Pre-filled syringe"
* package.package.quantity = 1
* package.package.containedItem.item.reference.reference = "ManufacturedItemDefinition/Zoladex-3.6mg-Implant-EE-MID"
* package.package.containedItem.amount.value = 1