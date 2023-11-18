Instance: e90fb5fe-5531-4280-865e-745865deb686
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "2"
* meta.lastUpdated = "2022-06-22T09:51:53.434+00:00"
* extension.url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"
* containedItemQuantity = 12 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152
* packageFor = Reference(bb8c2306-04c5-42df-94c9-aa6d6e68050b)
* description = "12 comprimido blister"
* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072251#100000072251 "Portuguese"
* packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.type.coding.code = #100000073498
* packaging.type.coding.display = "Box"
* packaging.quantity = 1
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346/terms/100000073496"
* packaging.packaging.type.coding.code = #100000073496
* packaging.packaging.type.coding.display = "Blister"
* packaging.packaging.quantity = 1
* packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/cade57d9-734e-4b1a-83a0-743b8af67174"