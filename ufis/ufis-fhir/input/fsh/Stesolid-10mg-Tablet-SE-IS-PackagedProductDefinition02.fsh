Instance: Stesolid-10mg-Tablet-SE-IS-PackagedProductDefinition02
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-08T13:39:10.118+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 100 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"
* packageFor = Reference(Stesolid-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* description = "Burk, 100 tabletter"
* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072288 "Swedish"
* marketingStatus.country = $100000000002#100000000535 "Sweden"
* marketingStatus.status = $100000072052#100000072083 "Marketed"
* packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.type.coding.code = #100000073498
* packaging.type.coding.display = "Box"
* packaging.quantity = 1
* packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.material.coding.code = #200000003529
* packaging.material.coding.display = "Cardboard"
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding.code = #100000073497
* packaging.packaging.type.coding.display = "Bottle"
* packaging.packaging.quantity = 1
* packaging.packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding.code = #200000003208
* packaging.packaging.material.coding.display = "Plastic"
* packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/Stesolid-10mg-Tablet-SE-IS-ManufacturedItemDefinition"
* packaging.packaging.containedItem.amount.value = 100
* packaging.packaging.containedItem.amount.code = #200000002152
* packaging.packaging.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* packaging.packaging.containedItem.amount.unit = "Tablet"