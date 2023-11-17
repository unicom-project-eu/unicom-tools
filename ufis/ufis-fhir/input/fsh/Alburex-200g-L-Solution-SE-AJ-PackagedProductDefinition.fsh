Instance: Alburex-200g-L-Solution-SE-AJ-PackagedProductDefinition
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-07-13T09:43:44.995+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002158 "vial"
* packageFor = Reference(Alburex-200g-L-Solution-SE-AJ-MedicinalProductDefinition)
* description = "Injektionsflaska, 100 ml"
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
* packaging.shelfLifeStorage.periodDuration.value = 2
* packaging.shelfLifeStorage.periodDuration.code = #200000003434
* packaging.shelfLifeStorage.periodDuration.system = "https://spor.ema.europa.eu/v1/lists/100000110633"
* packaging.shelfLifeStorage.periodDuration.unit = "year"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.code = #100000073410
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.display = "Do not store above 25 °C"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[+].coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.code = #100000073420
* packaging.shelfLifeStorage.specialPrecautionsForStorage[=].coding.display = "Do not freeze"
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding.code = #100000073563
* packaging.packaging.type.coding.display = "Vial"
* packaging.packaging.quantity = 1
* packaging.packaging.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material.coding.code = #200000003205
* packaging.packaging.material.coding.display = "Glass type II"
* packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/Alburex-200g-L-Solution-SE-AJ-ManufacturedItemDefinition"
* packaging.packaging.containedItem.amount.value = 100
* packaging.packaging.containedItem.amount.code = #100000110662
* packaging.packaging.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/100000110633"
* packaging.packaging.containedItem.amount.unit = "Millilitre(s)"