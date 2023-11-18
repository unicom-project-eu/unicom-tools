Instance: Aspirin500mgtablett-SE-PLC-MedicinalProductDef
InstanceOf: PPLMedicinalProductDefinition
Usage: #inline
* meta.versionId = "1"
* meta.lastUpdated = "2022-08-18T10:05:10.891+00:00"
* extension.url = "http://ema.europa.eu/fhir/extension/authorisedDoseForm"
* combinedPharmaceuticalDoseForm = $200000000004~200000000006~200000000007~200000000008#100000073664 "Tablet"
* identifier[+].system = "http://ema.europa.eu/fhir/mpId"
* identifier[=].value = "SE-100004813-00000137"
* identifier[+].system = "http://ema.europa.eu/fhir/eurdId"
* identifier[=].value = "39"
* domain = $100000000004#100000000012 "Human use"
* status = $200000005003#200000005004 "Current"
* indication = "Huvudvärk, menstruationssmärtor, tandvärk, led- och muskelsmärtor, reumatiska smärtor, feber vid infektions- och förkylningssjukdomar.  Till barn med feber som ej svarat på gängse behandling endast efter kontakt med läkare"
* legalStatusOfSupply = $100000072051#100000072076 "Medicinal product not subject to medical prescription"
* classification = $100000093533#100000097266 "N02BA01"
* name.productName = "Aspirin 500 mg tablett"
* name.part[+].part = "Aspirin"
* name.part[=].type.coding.system = "http://spor.ema.europa.eu/v1/lists/220000000000"
* name.part[=].type.coding.code = #220000000002
* name.part[=].type.coding.display = "Invented name part"
* name.part[+].part = "500 mg"
* name.part[=].type.coding.system = "http://spor.ema.europa.eu/v1/lists/220000000000"
* name.part[=].type.coding.code = #220000000004
* name.part[=].type.coding.display = "Strength part"
* name.part[+].part = "tablett"
* name.part[=].type.coding.system = "http://spor.ema.europa.eu/v1/lists/220000000000"
* name.part[=].type.coding.code = #220000000005
* name.part[=].type.coding.display = "Pharmaceutical dose form part"
* name.usage.country.coding.system = "http://spor.ema.europa.eu/v1/lists/100000000002"
* name.usage.country.coding.code = #100000000535
* name.usage.country.coding.display = "Sweden"
* name.usage.language.coding.system = "http://spor.ema.europa.eu/v1/lists/100000072057"
* name.usage.language.coding.code = #100000072288
* name.usage.language.coding.display = "Swedish"
//DUMMY
* legalStatusOfSupply = $100000072051#100000072084 "Medicinal product subject to medical prescription"