Instance: JMJ-Humalog-UK-authorisation-example
InstanceOf: PPLRegulatedAuthorization
Usage: #inline

* subject = Reference(JMJ-Humalog-Kwikpen-product-example)
* type = $220000000060#220000000061 "Marketing Authorisation"
* region.coding[0] = $100000000002#100000000556 "United Kingdom of Great Britain and Northern Irelan"
* region.coding[+] = $iso3166-1edition2#GBR "United Kingdom of Great Britain and Northern Ireland"
* status = $100000072049#100000072099 "Valid"
* statusDate = "2006-03-30"
* holder.display = "Eli Lilly Nederland B.V"
* regulator.display = "Medicines and Healthcare products Regulatory Agency"
//DUMMY
* identifier.value = "dummy"