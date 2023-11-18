Instance: JMJ-Monuril-UK-authorisation-example
InstanceOf: PPLRegulatedAuthorization
Usage: #inline

* identifier.system = "http://ema.europa.eu/fhir/marketingAuthorizationNumber"
* identifier.value = "PL 31654/0006"
* subject = Reference(JMJ-Monuril-product-example)
* type = $220000000060#220000000061 "Marketing Authorisation"
* region.coding[0] = $100000000002#100000000556 "United Kingdom of Great Britain and Northern Irelan"
* region.coding[+] = $iso3166-1edition2#GBR "United Kingdom of Great Britain and Northern Ireland"
* status = $100000072049#100000072099 "Valid"
* statusDate = "2021-05-17"
* holder.display = "Zambon UK Limited (formerly Profile Pharma)"
* regulator.display = "Medicines and Healthcare products Regulatory Agency"