Instance: LidoAcc-20mgml-InjSol-SE-AJ-PackagedProductDefinition
InstanceOf: PackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-11-06T21:05:25.594+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* extension.valueQuantity = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002158 "Vial"
* packageFor = Reference(LidoAcc-20mgml-InjSol-SE-AJ-MedicinalProductDefinition)
* description = "Injektionsflaska, 20 ml"
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
* package.shelfLifeStorage.periodDuration.system = "http://spor.ema.europa.eu/v1/lists/100000110633"
* package.shelfLifeStorage.periodDuration.unit = "Year"
* package.package.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.package.type.coding.code = "100000073563"
* package.package.type.coding.display = "Vial"
* package.package.quantity = 1
* package.package.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material.coding.code = "200000003204"
* package.package.material.coding.display = "Glass type I"
* package.package.containedItem.item.reference.reference = "ManufacturedItemDefinition/LidoAcc-20mgml-InjSol-SE-AJ-ManufacturedItemDefinition"
* package.package.containedItem.amount.value = 20
* package.package.containedItem.amount.code = "100000110662"
* package.package.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/100000110633"
* package.package.containedItem.amount.unit = "millilitre(s)"