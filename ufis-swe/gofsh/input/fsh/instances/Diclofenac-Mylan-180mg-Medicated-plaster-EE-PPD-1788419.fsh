Instance: Diclofenac-Mylan-180mg-Medicated-plaster-EE-PPD-1788419
InstanceOf: PackagedProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-08-14T21:07:05.752+00:00"
* extension.url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"
* extension.valueQuantity = 5 http://spor.ema.europa.eu/v1/lists/200000000014#200000002140 "Plaster"
* identifier.system = "http://ema.europa.eu/example/pcid"
* identifier.value = "EE-100022866-36016-1788419"
* packageFor = Reference(Diclofenac-Mylan-180mg-Medicated-plaster-EE-MPD)
* description = "Suletava ümbrise materjal on paber/PE/alumiinium/etüleen ja metüülakrüülhappe kopolümeer. Ümbrises on 5 ravimplaastrit. Pakendi suurus: 5 või 10 ravimplaastrit karbis."
* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072172 "Estonian"
* marketingStatus.country = $100000000002#100000000388 "Republic of Estonia"
* marketingStatus.status = $100000072052#100000072083 "Marketed"
* package.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.type.coding.code = "100000073498"
* package.type.coding.display = "Box"
* package.quantity = 1
* package.material.coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.material.coding.code = "200000003529"
* package.material.coding.display = "Cardboard"
* package.package.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* package.package.type.coding.code = "100000073540"
* package.package.type.coding.display = "Pouch"
* package.package.quantity = 1
* package.package.material[0].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material[=].coding.code = "200000003207"
* package.package.material[=].coding.display = "Paper"
* package.package.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material[=].coding.code = "200000003214"
* package.package.material[=].coding.display = "PolyEthylene"
* package.package.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material[=].coding.code = "200000012521"
* package.package.material[=].coding.display = "Ethylene meta-acrylic acid"
* package.package.material[+].coding.system = "https://spor.ema.europa.eu/v1/lists/200000003199"
* package.package.material[=].coding.code = "200000003200"
* package.package.material[=].coding.display = "Aluminium"
* package.package.containedItem.item.reference.reference = "ManufacturedItemDefinition/Diclofenac-Mylan-180mg-Medicated-plaster-EE-MID"
* package.package.containedItem.amount.value = 5
* package.package.containedItem.amount.code = "200000002140"
* package.package.containedItem.amount.system = "https://spor.ema.europa.eu/v1/lists/200000000014"
* package.package.containedItem.amount.unit = "Plaster"