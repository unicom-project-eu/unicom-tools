Instance: NitroglycerinAbicurinfu-SE-PLC-PackageProductDef
InstanceOf: PackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-13T16:18:19.988+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* extension.valueQuantity = 10 http://spor.ema.europa.eu/v1/lists/200000000014#200000002111 "Bottle"
* packageFor = Reference(NitroglycerinAbicurinfu-SE-PLC-MedicinalProductDef)
* description = "Injektionsflaska, 10 x 50 ml"
* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072288 "Swedish"
* marketingStatus.country = $100000000002#100000000535 "Sweden"
* marketingStatus.status = $100000072052#100000072083 "Marketed"
* package.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.type.coding.code = "100000073498"
* package.type.coding.display = "Box"
* package.quantity = 1
* package.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.material.coding.code = "200000003529"
* package.material.coding.display = "Cardboard"
* package.shelfLifeStorage.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073343"
* package.shelfLifeStorage.type.coding.code = "100000073403"
* package.shelfLifeStorage.type.coding.display = "Shelf life of the medicinal product as packaged for sale"
* package.shelfLifeStorage.periodDuration.value = 3
* package.shelfLifeStorage.periodDuration.code = "200000003434"
* package.shelfLifeStorage.periodDuration.system = "https://spor.ema.europa.eu/v1/lists/100000110633"
* package.shelfLifeStorage.periodDuration.unit = "year"
* package.shelfLifeStorage.specialPrecautionsForStorage.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* package.shelfLifeStorage.specialPrecautionsForStorage.coding.code = "100000073424"
* package.shelfLifeStorage.specialPrecautionsForStorage.coding.display = "This medicinal product does not require any special storage conditions"
* package.containedItem.item.reference.reference = "ManufacturedItemDefinition/NitroglycerinAbicurinfu-SE-PLC-ManufacturedItemDef"
* package.containedItem.amount.value = 10
* package.containedItem.amount.code = "200000002111"
* package.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/100000110633~200000000014"
* package.containedItem.amount.unit = "Bottle"