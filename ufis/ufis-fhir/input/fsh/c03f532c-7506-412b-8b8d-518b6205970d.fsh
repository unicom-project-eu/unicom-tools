Instance: c03f532c-7506-412b-8b8d-518b6205970d
InstanceOf: PPLPackagedProductDefinition
Usage: #inline
* meta.versionId = "2"
* meta.lastUpdated = "2022-06-22T09:51:53.454+00:00"
* extension.url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"
* containedItemQuantity = 30 http://spor.ema.europa.eu/v1/lists/200000000014#200000002152
* packageFor = Reference(bb8c2306-04c5-42df-94c9-aa6d6e68050b)
* description = "30 comprimido blister"
* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072251#100000072251 "Portuguese"
* packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346/terms/100000073498"
* packaging.type.coding.code = #100000073498
* packaging.type.coding.display = "Box"
* packaging.quantity = 1
* packaging.packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346/terms/100000073496"
* packaging.packaging.type.coding.code = #100000073496
* packaging.packaging.type.coding.display = "Blister"
* packaging.packaging.quantity = 1
* packaging.packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/cade57d9-734e-4b1a-83a0-743b8af67174"