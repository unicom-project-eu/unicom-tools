Instance: Tramadol-KRKA-100mg-Prolonged-release-tablet-EE-PPD-1043525
InstanceOf: PackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-08-14T20:58:49.382+00:00"
* extension.url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"
* extension.valueQuantity = 30 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"
* identifier.system = "http://ema.europa.eu/example/pcid"
* identifier.value = "EE-100009540-12260-1043525"
* packageFor = Reference(Tramadol-KRKA-100mg-Prolonged-release-tablet-EE-MPD)
* description = "100 mg toimeainet prolongeeritult vabastavad tabletid Al/PVC blisterpakendis – 30 tk."
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
* package.package.type.coding.code = "100000073496"
* package.package.type.coding.display = "Blister"
* package.package.quantity = 1
* package.package.material[0].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material[=].coding.code = "200000003200"
* package.package.material[=].coding.display = "Aluminium"
* package.package.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material[=].coding.code = "200000003222"
* package.package.material[=].coding.display = "PolyVinyl Chloride"
* package.package.containedItem.item.reference.reference = "ManufacturedItemDefinition/Tramadol-KRKA-100mg-Prolonged-release-tablet-EE-MID"
* package.package.containedItem.amount.value = 30