Instance: TramadolRetardHexal100mgdepot-SE-PLC-RegAutho
InstanceOf: RegulatedAuthorization
Usage: #inline
* identifier.system = "http://ema.europa.eu/fhir/MarketingAuthorizationNumber"
* identifier.value = "21235"
* subject = Reference(TramadolRetardHexal100mgdepot-SE-PLC-MedicinalProductDef)
* type = $220000000060#220000000061 "Marketing Authorisation"
* region = $100000000002#100000000535 "Sweden"
* status = $100000072049#100000072099 "Valid"
* statusDate = "2005-04-29"
* holder.identifier.system = "https://spor.ema.europa.eu/v1/locations"
* holder.identifier.value = "LOC-100001468"
* holder.display = "Hexal A/S"
* case.type = $authorisationDateType#dateOfFirstAuthorisation "First Authorisation"
* case.dateDateTime = "2005-04-29"