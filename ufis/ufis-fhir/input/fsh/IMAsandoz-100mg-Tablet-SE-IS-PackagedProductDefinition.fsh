Instance: IMAsandoz-100mg-Tablet-SE-IS-PackagedProductDefinition
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-13T16:42:09.691+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 10 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152 "Tablet"
* packageFor = Reference(IMAsandoz-100mg-Tablet-SE-IS-MedicinalProductDefinition)
* description = "Blister, 60 tabletter"
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
* packaging.shelfLifeStorage.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073343"
* packaging.shelfLifeStorage.type.coding.code = #100000073403
* packaging.shelfLifeStorage.type.coding.display = "Shelf life of the medicinal product as packaged for sale"
* packaging.shelfLifeStorage.periodDuration.value = 3
* packaging.shelfLifeStorage.periodDuration.unit = "years"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.code = #100000073411
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.display = "Do not store above 30 °C"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.code = #100000073421
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.display = "Store in the original package"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.code = #100000073427
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.display = "in order to protect from moisture"
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding.code = #100000073496
* packaging.packaging.type.coding.display = "Blister"
* packaging.packaging.quantity = 6
* packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material[=].coding.code = #200000003222
* packaging.packaging.material[=].coding.display = "PolyVinyl Chloride"
* packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material[=].coding.code = #200000003200
* packaging.packaging.material[=].coding.display = "Aluminium"
* packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/IMAsandoz-100mg-Tablet-SE-IS-ManufacturedItemDefinition"
* packaging.packaging.containedItem.amount.value = 10
* packaging.packaging.containedItem.amount.code = #200000002152
* packaging.packaging.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/200000000014"
* packaging.packaging.containedItem.amount.unit = "Tablet"