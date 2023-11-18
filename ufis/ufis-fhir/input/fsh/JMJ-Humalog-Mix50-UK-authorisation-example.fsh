Instance: JMJ-Humalog-Mix50-UK-authorisation-example
InstanceOf: PPLRegulatedAuthorization
Usage: #inline

* identifier.system = "http://ema.europa.eu/fhir/marketingAuthorizationNumber"
* identifier.value = "EU/1/96/007/035"
* subject = Reference(JMJ-Humalog-Mix50-Kwikpen-product-example)
* type = $220000000060#220000000061 "Marketing Authorisation"
* region.coding[0] = $100000000002#100000000556 "United Kingdom of Great Britain and Northern Irelan"
* region.coding[+] = $iso3166-1edition2#GBR "United Kingdom of Great Britain and Northern Ireland"
* status = $100000072049#100000072099 "Valid"
* statusDate = "2006-03-30"
* holder.display = "Eli Lilly Nederland B.V"
* regulator.display = "European Medicines Agency"