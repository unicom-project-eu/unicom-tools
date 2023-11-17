Instance: Nasonex-50mcg-Suspension-SE-IS-PackagedProductDefinition03
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-10-17T06:45:59.605+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"
* containedItemQuantity = 3 http://spor.ema.europa.eu/v1/lists/200000000014#200000002111 "Bottle"
* packageFor = Reference(Nasonex-50mcg-Suspension-SE-IS-MedicinalProductDefinition)
* description = "Plastflaska med dospump, 3 x 140 doser"
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
* packaging.shelfLifeStorage.periodDuration.unit = "years"
* packaging.shelfLifeStorage.specialPrecautionsForStorage.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073344"
* packaging.shelfLifeStorage.specialPrecautionsForStorage.coding.code = #100000073420
* packaging.shelfLifeStorage.specialPrecautionsForStorage.coding.display = "Do not freeze"
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.packaging.type.coding.code = #100000125779
* packaging.packaging.type.coding.display = "Multidose container with pump"
* packaging.packaging.quantity = 3
* packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material[=].coding.code = #200000003214
* packaging.packaging.material[=].coding.display = "PolyEthylene"
* packaging.packaging.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* packaging.packaging.material[=].coding.code = #200000003200
* packaging.packaging.material[=].coding.display = "200000003219"
* packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/Nasonex-50mcg-Suspension-SE-IS-ManufacturedItemDefinition"
* packaging.packaging.containedItem.amount.value = 50
* packaging.packaging.containedItem.amount.code = #100000110920
* packaging.packaging.containedItem.amount.system = "http://spor.ema.europa.eu/v1/lists/100000110633"
* packaging.packaging.containedItem.amount.unit = "microgram(s)/dose"