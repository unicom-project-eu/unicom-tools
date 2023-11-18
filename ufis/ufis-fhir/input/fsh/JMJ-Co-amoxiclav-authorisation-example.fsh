Instance: JMJ-Co-amoxiclav-authorisation-example
InstanceOf: PPLRegulatedAuthorization
Usage: #inline

* identifier.system = "http://ema.europa.eu/fhir/marketingAuthorizationNumber"
* identifier.value = "la-la-la-la"
* subject = Reference(JMJ-Co-amoxiclav-product-example)
* type = $220000000060#220000000061 "Marketing Authorisation"
* region.coding[0] = $100000000002#100000000556 "United Kingdom of Great Britain and Northern Ireland"
* region.coding[+] = $iso3166-1edition2#GBR "United Kingdom of Great Britain and Northern Ireland"
* status = $100000072049#100000072099 "Valid"
* statusDate = "2021-03-25"
* holder.display = "Reference for Aurobindo Pharma - Milpharm Ltd"
* regulator.display = "Reference for Medicines and Healthcare products Regulatory Agency"