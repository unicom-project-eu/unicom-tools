Instance: MorfinMeda-10mgml-Solution-SE-BS-PackagedProductDefinition-02
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-11-04T20:04:57.365+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 10 http://spor.ema.europa.eu/v1/lists/200000000014#200000002164 "Ampoule"
* packageFor = Reference(MorfinMeda-10mgml-Solution-SE-BS-MedicinalProductDefinition)
* description = "Ampull, 10 x 10 ml"
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
* packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/MorfinMeda-10mgml-Solution-SE-BS-ManufacturedItemDefinition"
* packaging.packaging.containedItem.amount.value = 10
* packaging.packaging.containedItem.amount.code = #100000110662
* packaging.packaging.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/100000110633~200000000014"
* packaging.packaging.containedItem.amount.unit = "millilitre(s)"