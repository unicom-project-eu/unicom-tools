Instance: Prokanazol-100mg-Hard-capsule-EE-PPD-1164035
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-08-14T19:10:34.636+00:00"
* extension.url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"
* containedItemQuantity = 4 http://spor.ema.europa.eu/v1/lists/200000000014#200000002113 "Capsule"
* identifier.system = "http://ema.europa.eu/example/pcid"
* identifier.value = "EE-100000151-15472-1164035"
* packageFor = Reference(Prokanazol-100mg-Hard-capsule-EE-MPD)
* description = "Termovormitud alumiiniumblister. Pakendis 4, 14, 18, 28 või 30 kapslit. Kõik pakendi suurused ei pruugi olla müügil."
* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072172 "Estonian"
* marketingStatus.country = $100000000002#100000000388 "Republic of Estonia"
* marketingStatus.status = $100000072052#100000072083 "Marketed"
* packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.type.coding.code = #100000073498
* packaging.type.coding.display = "Box"
* packaging.quantity = 1
* packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.material.coding.code = #200000003529
* packaging.material.coding.display = "Cardboard"
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding.code = #100000073496
* packaging.packaging.type.coding.display = "Blister"
* packaging.packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding.code = #200000003200
* packaging.packaging.material.coding.display = "Aluminium"
* packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/Prokanazol-100mg-Hard-capsule-EE-MID"
* packaging.packaging.containedItem.amount.value = 4