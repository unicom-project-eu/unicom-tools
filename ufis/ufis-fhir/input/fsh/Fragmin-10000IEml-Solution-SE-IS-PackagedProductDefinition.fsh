Instance: Fragmin-10000IEml-Solution-SE-IS-PackagedProductDefinition
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "7"
* meta.lastUpdated = "2022-07-13T16:05:31.542+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 10 http://spor.ema.europa.eu/v1/lists/200000000014#200000002164 "Ampoule"
* packageFor = Reference(Fragmin-10000IEml-Solution-SE-IS-MedicinalProductDefinition)
* description = "Ampull, 10 x 1 ml"
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
* packaging.packaging.type.coding.code = #100000073490
* packaging.packaging.type.coding.display = "Ampoule"
* packaging.packaging.quantity = 10
* packaging.packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding.code = #200000003203
* packaging.packaging.material.coding.display = "Glass"
* packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/Fragmin-10000IEml-Solution-SE-IS-ManufacturedItemDefinition"
* packaging.packaging.containedItem.amount.value = 10
* packaging.packaging.containedItem.amount.code = #200000002164
* packaging.packaging.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* packaging.packaging.containedItem.amount.unit = "ampoule"