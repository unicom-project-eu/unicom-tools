Instance: Yaz-0023mg-tablet-SE-AJ-PackagedProductDefinition
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-08-08T17:36:00.224+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 84 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "tablet"
* packageFor = Reference(Yaz-0023mg-tablet-SE-AJ-MedicinalProductDefinition)
* description = "Blister, 3 x 28 tabletter"
* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072288 "Swedish"
* marketingStatus.country = $100000000002#100000000535 "Sweden"
* marketingStatus.status = $100000072052#100000072083 "Marketed"
* packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.type.coding.code = #100000073498
* packaging.type.coding.display = "Box"
* packaging.quantity = 1
* packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.material.coding.code = #200000003208
* packaging.material.coding.display = "Plastic"
* packaging.shelfLifeStorage.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073343"
* packaging.shelfLifeStorage.type.coding.code = #100000073403
* packaging.shelfLifeStorage.type.coding.display = "Shelf life of the medicinal product as packaged for sale"
* packaging.shelfLifeStorage.periodDuration.value = 5
* packaging.shelfLifeStorage.periodDuration.code = #200000003434
* packaging.shelfLifeStorage.periodDuration.system = "http://spor.ema.europa.eu/v1/lists/100000110633"
* packaging.shelfLifeStorage.periodDuration.unit = "Year"
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding.code = #100000073498
* packaging.packaging.type.coding.display = "Box"
* packaging.packaging.quantity = 3
* packaging.packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding.code = #200000003529
* packaging.packaging.material.coding.display = "Cardboard"
* packaging.packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.packaging.type.coding.code = #100000073496
* packaging.packaging.packaging.type.coding.display = "Blister"
* packaging.packaging.packaging.quantity = 1
* packaging.packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.packaging.material[=].coding.code = #200000003200
* packaging.packaging.packaging.material[=].coding.display = "Aluminium"
* packaging.packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.packaging.material[=].coding.code = #200000003222
* packaging.packaging.packaging.material[=].coding.display = "PolyVinyl Chloride"
* packaging.packaging.packaging.containedItem[+].item.reference.reference = "ManufacturedItemDefinition/Yaz-0023mg-tablet-SE-AJ-ManufacturedItemDefinition01"
* packaging.packaging.packaging.containedItem[=].amount.value = 24
* packaging.packaging.packaging.containedItem[=].amount.code = #200000002152
* packaging.packaging.packaging.containedItem[=].amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* packaging.packaging.packaging.containedItem[=].amount.unit = "tablet"
* packaging.packaging.packaging.containedItem[+].item.reference.reference = "ManufacturedItemDefinition/Yaz-0023mg-tablet-SE-AJ-ManufacturedItemDefinition02"
* packaging.packaging.packaging.containedItem[=].amount.value = 4
* packaging.packaging.packaging.containedItem[=].amount.code = #200000002152
* packaging.packaging.packaging.containedItem[=].amount.system = "http://spor.ema.europa.eu/v1/lists/100000110633~200000000014"
* packaging.packaging.packaging.containedItem[=].amount.unit = "tablet"