Instance: Panodil60mgsuppositorium-SE-PLC-PackageProductDef
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-23T10:54:21.439+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 10 http://spor.ema.europa.eu/v1/lists/200000000014#200000002149 "Suppository"
* packageFor = Reference(Panodil60mgsuppositorium-SE-PLC-MedicinalProductDef)
* description = "Strip, 10 suppositorier"
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
* packaging.shelfLifeStorage.periodDuration.value = 5
* packaging.shelfLifeStorage.periodDuration.code = #200000003434
* packaging.shelfLifeStorage.periodDuration.system = "https://spor.ema.europa.eu/v1/lists/100000110633"
* packaging.shelfLifeStorage.periodDuration.unit = "year"
* packaging.shelfLifeStorage.specialPrecautionsForStorage.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage.specialPrecautionsForStorage.coding.code = #100000073410
* packaging.shelfLifeStorage.specialPrecautionsForStorage.coding.display = "Do not store above 25°C"
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding.code = #100000073559
* packaging.packaging.type.coding.display = "Strip"
* packaging.packaging.quantity = 10
* packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material[=].coding.code = #200000003222
* packaging.packaging.material[=].coding.display = "PolyVinyl Chloride"
* packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material[=].coding.code = #200000003214
* packaging.packaging.material[=].coding.display = "PolyEthylene"
* packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/Panodil60mgsuppositorium-SE-PLC-ManufacturedItemDef"
* packaging.packaging.containedItem.amount.value = 1
* packaging.packaging.containedItem.amount.code = #200000002149
* packaging.packaging.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/100000110633~200000000014"
* packaging.packaging.containedItem.amount.unit = "Suppository"