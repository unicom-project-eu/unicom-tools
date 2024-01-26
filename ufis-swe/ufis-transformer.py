from os import listdir, mkdir, remove
import hashlib
import re
import shutil

org_file = "../../ufis-swe-ig/input/fsh/Organization.fsh"
target_folder = "../../ufis-swe-ig/input/fsh/"
FOLDER = "./gofsh/input/fsh/instances"
##TODO
shutil.rmtree(target_folder)
mkdir(target_folder)


f = open(FOLDER + "/missing.fsh", "w")

f.write(
    """
Instance: Zoloft50mgdepottablett-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Trombyl160mgtablett-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(Zoloft50mgdepottablett-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: VaxigripTetra-0.5ml-Suspension-SE-AJ-AdministrableProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(VaxigripTetra-0.5ml-Suspension-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073864 "Suspension for injection"
* producedFrom = Reference(VaxigripTetra-0.5ml-Suspension-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"

Instance: Stesolid-10mg-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Stesolid-10mg-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073829 "Rectal solution"
* producedFrom = Reference(Stesolid-10mg-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073628 "Retal use"

Instance: Stesolid-2mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Stesolid-2mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(Stesolid-2mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Renitec-10mg-Tablet-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Renitec-10mg-Tablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "tablet"
* producedFrom = Reference(Renitec-10mg-Tablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Oxascand-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Oxascand-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(Oxascand-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Zinacef-250mg-Powder-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Zinacef-250mg-Powder-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000074038 "Solution for injection/infusion"
* producedFrom = Reference(Zinacef-250mg-Powder-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"

Instance: Zinacef-1.5g-Powder-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Zinacef-1.5g-Powder-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000074038 "Solution for injection/infusion"
* producedFrom = Reference(Zinacef-1.5g-Powder-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"

Instance: Softacort335mgpermlogondroppar-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Softacort335mgpermlogondroppar-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073759 "Eye drops, solution"
* producedFrom = Reference(Softacort335mgpermlogondroppar-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073617 "Ocular use"

Instance: TPTDteva-20mcg80mcl-Solution-SE-IS-AdminProdDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(TPTDteva-20mcg80mcl-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(TPTDteva-20mcg80mcl-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073633 "Subcutaneous use"

Instance: Rectogesic4mggrektalsalva-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Rectogesic4mggrektalsalva-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073828 "Rectal ointment"
* producedFrom = Reference(Rectogesic4mggrektalsalva-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073628 "Rectal use"

Instance: TramadolRetardActavis100mgdepot-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(TramadolRetardActavis100mgdepot-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(TramadolRetardActavis100mgdepot-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Zeldox20mgmlpulvervatskainjek-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Zeldox20mgmlpulvervatskainjek-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom[0] = Reference(ManufacturedItemDefinition/Zeldox20mgmlpulvervatskainjek-SE-PLC-ManufacturedItemDef01)
* producedFrom[+] = Reference(ManufacturedItemDefinition/Zeldox20mgmlpulvervatskainjek-SE-PLC-ManufacturedItemDef02)
* routeOfAdministration.code = $100000073345#100000073600 "Intramuscular use"

Instance: Sporanox-10mgml-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Sporanox-10mgml-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073646 "Oral solution"
* producedFrom = Reference(Sporanox-10mgml-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Sobril-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Sobril-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(Sobril-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Levaxin-200mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Levaxin-200mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(Levaxin-200mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Sobril-15mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Sobril-15mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(Sobril-15mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Tradolan50mgmlinjektionlosning-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Tradolan50mgmlinjektionlosning-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Tradolan50mgmlinjektionlosning-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code.coding[0] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073633 "Subcutaneous use"

Instance: Voxra-150mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Voxra-150mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073668 "Modified-release tablet"
* producedFrom = Reference(Voxra-150mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Sporanox-100mg-Cap-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Sporanox-100mg-Cap-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073375 "Capsule, hard"
* producedFrom = Reference(Sporanox-100mg-Cap-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Suscard5mgbuckaltablett-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Suscard5mgbuckaltablett-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073699 "Buccal tablet"
* producedFrom = Reference(Suscard5mgbuckaltablett-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000075275 "Buccal use"

Instance: CMImylan-25mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(CMImylan-25mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(CMImylan-25mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Zoladex-3.6mg-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Zoladex-3.6mg-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073874 "Implant"
* producedFrom = Reference(Zoladex-3.6mg-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000075249 "Implantation"

Instance: Suscard25mgbuckaltablett-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Suscard25mgbuckaltablett-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073699 "Buccal tablet"
* producedFrom = Reference(Suscard25mgbuckaltablett-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000075275 "Buccal use"

Instance: CMImylan-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(CMImylan-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(CMImylan-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Ventoline2mgmllosningnebulisator-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Ventoline2mgmllosningnebulisator-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073835 "Nebuliser solution"
* producedFrom = Reference(Ventoline2mgmllosningnebulisator-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073584 "Inhalation use"

Instance: Stesolid-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Stesolid-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(Stesolid-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Voxra-300mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Voxra-300mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073668 "Modified-release tablet"
* producedFrom = Reference(Voxra-300mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Stesolid-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Stesolid-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(Stesolid-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: EnoxaparinBecat8000IEinjektion-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(EnoxaparinBecat8000IEinjektion-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(EnoxaparinBecat8000IEinjektion-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code.coding[0] = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073633 "Subcutaneous use"

Instance: Klexane100000IEinjektion-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Klexane100000IEinjektion-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Klexane100000IEinjektion-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code.coding[0] = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073633 "Subcutaneous use"

Instance: Losec-10mg-Tablet-SE-BS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Losec-10mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073667 "Gastro-resistant tablet"
* producedFrom = Reference(Losec-10mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: SoluCortef100mgpulvervatskainj-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(SoluCortef100mgpulvervatskainj-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(SoluCortef100mgpulvervatskainj-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code.coding[0] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"

Instance: Espranor-8mg-Lyophilisate-SE-BS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Espranor-8mg-Lyophilisate-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073682 "Oral lyophilisate"
* producedFrom = Reference(Espranor-8mg-Lyophilisate-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Locoid01kutanlosning-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Locoid01kutanlosning-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073731 "Cutaneous solution"
* producedFrom = Reference(Locoid01kutanlosning-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code.coding[0] = $100000073345#100000073566 "Cutaneous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073564 "Auricular use"

Instance: Orimox-50mcg-Suspension-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Orimox-50mcg-Suspension-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000174018 "Suspension for spray"
* producedFrom = Reference(Orimox-50mcg-Suspension-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073615 "Nasal use"

Instance: Tiparol50mgbrustablett-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Tiparol50mgbrustablett-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073681 "Effervescent tablet"
* producedFrom = Reference(Tiparol50mgbrustablett-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: EnoxaparinLedraxen2000IEinjektion-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(EnoxaparinLedraxen2000IEinjektion-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(EnoxaparinLedraxen2000IEinjektion-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code.coding[0] = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073633 "Subcutaneous use"

Instance: Oxascand-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Oxascand-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(Oxascand-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Stesolidpre-5mgml-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Stesolidpre-5mgml-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073829 "Rectal solution"
* producedFrom = Reference(Stesolidpre-5mgml-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073628 "Retal use"

Instance: Zinacef-750mg-Powder-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Zinacef-750mg-Powder-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000074038 "Solution for injection/infusion"
* producedFrom = Reference(Zinacef-750mg-Powder-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"

Instance: IMAsandoz-400mg-Tablet-SE-IS-ManufacturedItemDefinition
InstanceOf: PPLManufacturedItemDefinition
* status = #active
* manufacturedDoseForm = $200000000004#100000073665 "Film-coated tablet"
* unitOfPresentation = $200000000014#200000002152 "Tablet"

Instance: Stesolid-5mg-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Stesolid-5mg-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073829 "Rectal solution"
* producedFrom = Reference(Stesolid-5mg-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073628 "Retal use"

Instance: Espranor-2mg-Lyophilisate-SE-BS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Espranor-2mg-Lyophilisate-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073682 "Oral lyophilisate"
* producedFrom = Reference(Espranor-2mg-Lyophilisate-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Glytrin04mgdossublingualspray-SE-PLC-ManufacturedItemDef
InstanceOf: PPLManufacturedItemDefinition
* status = #active
* manufacturedDoseForm = $200000000004#100000143499 "Sublingual spray, solution"
* unitOfPresentation = $200000000014#200000022801 "Canister"

Instance: VoltarenT50mgFilmtablet-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(VoltarenT50mgFilmtablet-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073380 "Coated tablet"
* producedFrom = Reference(VoltarenT50mgFilmtablet-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Zoladex-10.8mg-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Zoladex-10.8mg-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073874 "Implant"
* producedFrom = Reference(Zoladex-10.8mg-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000075249 "Implantation"

Instance: TPTDteva-2080-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(TPTDteva-2080-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(TPTDteva-2080-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073633 "Subcutaneous use"

Instance: TramadolRetardHexal100mgdepot-SE-PLC-AdminProductDef
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(TramadolRetardHexal100mgdepot-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(TramadolRetardHexal100mgdepot-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Oxascand-15mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Oxascand-15mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(Oxascand-15mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"



Instance: TrimonilR-200mg-PRTablet-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(TrimonilR-200mg-PRTablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(TrimonilR-200mg-PRTablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: TrimonilR-150mg-PRTablet-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(TrimonilR-150mg-PRTablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(TrimonilR-150mg-PRTablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Triolif-Orange-Lozenge-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Triolif-Orange-Lozenge-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073703 "Lozenge"
* producedFrom = Reference(Triolif-Orange-Lozenge-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073621 "Oropharyngeal use"
* routeOfAdministration[+].code = $100000073345#100000073620 "Oromucosal use"

Instance: TegretolR-400mg-PRTablet-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(TegretolR-400mg-PRTablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(TegretolR-400mg-PRTablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Tegretol-200mg-Tablet-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Tegretol-200mg-Tablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(Tegretol-200mg-Tablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Tegretol-20mgml-Suspension-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Tegretol-20mgml-Suspension-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073362 "Oral suspension"
* producedFrom = Reference(Tegretol-20mgml-Suspension-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: TrimonilR-400mg-PRTablet-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(TrimonilR-400mg-PRTablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(TrimonilR-400mg-PRTablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Xylocain-2-Gel-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Xylocain-2-Gel-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073726 "Gel"
* producedFrom = Reference(Xylocain-2-Gel-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073628 "Rectal use"
* routeOfAdministration[+].code = $100000073345#100000073638 "Urethral use"

Instance: Xylo10-Adr5-InjSol-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Xylo10-Adr5-InjSol-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Xylo10-Adr5-InjSol-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073624 "Perineural use"
* routeOfAdministration[+].code = $100000073345#100000073572 "Epidural use"
* routeOfAdministration[+].code = $100000073345#100000075248 "Inflitration"

Instance: Xylocain-10mgml-InjSol-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Xylocain-10mgml-InjSol-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Xylocain-10mgml-InjSol-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073572 "Epidural use"
* routeOfAdministration[+].code = $100000073345#100000073624 "Perineural use"

Instance: Triolif-HonLem-Lozenge-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Triolif-HonLem-Lozenge-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073703 "Lozenge"
* producedFrom = Reference(Triolif-HonLem-Lozenge-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073621 "Oropharyngeal use"
* routeOfAdministration[+].code = $100000073345#100000073620 "Oromucosal use"

Instance: Tapin-2525-Plaster-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Tapin-2525-Plaster-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073714 "Medicated plaster"
* producedFrom = Reference(Tapin-2525-Plaster-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: LidPrilAlterNova-2525-Cream-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(LidPrilAlterNova-2525-Cream-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073712 "Cream"
* producedFrom = Reference(LidPrilAlterNova-2525-Cream-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: LidokainAgu-20mgml-InjSol-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(LidokainAgu-20mgml-InjSol-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(LidokainAgu-20mgml-InjSol-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073595 "Intradermal use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075554 "Submucosal use"

Instance: Tapin-2525-Cream-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Tapin-2525-Cream-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073712 "Cream"
* producedFrom = Reference(Tapin-2525-Cream-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: Xylocain-Dental-Adrenalin-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Xylocain-Dental-Adrenalin-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Xylocain-Dental-Adrenalin-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073624 "Perineural use"
* routeOfAdministration[+].code = $100000073345#100000075248 "Infiltration"

Instance: Yaz-0023mg-tablet-SE-AJ-AdministrableProductDefinition01
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Yaz-0023mg-tablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(Yaz-0023mg-tablet-SE-AJ-ManufacturedItemDefinition01)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Xylocain-WOP-2-Gel-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Xylocain-WOP-2-Gel-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073726 "Gel"
* producedFrom = Reference(Xylocain-WOP-2-Gel-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073628 "Rectal use"
* routeOfAdministration[+].code = $100000073345#100000073638 "Urethral use"

Instance: Lido4-Fluor25-EyeDropsSol-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Lido4-Fluor25-EyeDropsSol-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073759 "Eye drops, solution"
* producedFrom = Reference(Lido4-Fluor25-EyeDropsSol-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073617 "Ocular use"

Instance: LidoMylan-10mgml-InjSol-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(LidoMylan-10mgml-InjSol-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(LidoMylan-10mgml-InjSol-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073572 "Epidural use"
* routeOfAdministration[+].code = $100000073345#100000073624 "Perineural use"

Instance: Yasminelle28-tablet-SE-AJ-AdministrableProductDefinition01
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Yasminelle28-tablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(Yasminelle28-tablet-SE-AJ-ManufacturedItemDefinition01)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: LidokainAgu-10mgml-InjSol-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(LidokainAgu-10mgml-InjSol-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(LidokainAgu-10mgml-InjSol-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073595 "Intradermal use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075554 "Submucosal use"

Instance: Xylocain-WOP-10mgml-InjSol-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Xylocain-WOP-10mgml-InjSol-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Xylocain-WOP-10mgml-InjSol-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073572 "Epidural use"
* routeOfAdministration[+].code = $100000073345#100000073624 "Perineural use"

Instance: Xylocard-20mgml-InjSol-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Xylocard-20mgml-InjSol-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Xylocard-20mgml-InjSol-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073611 "Intravenous use"

Instance: TegretolR-200mg-PRTablet-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(TegretolR-200mg-PRTablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(TegretolR-200mg-PRTablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Tegretol-400mg-Tablet-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Tegretol-400mg-Tablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(Tegretol-400mg-Tablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Tegretol-100mg-Tablet-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Tegretol-100mg-Tablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(Tegretol-100mg-Tablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Xylocain-20mgml-InjSol-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Xylocain-20mgml-InjSol-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Xylocain-20mgml-InjSol-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073572 "Epidural use"
* routeOfAdministration[+].code = $100000073345#100000073624 "Perineural use"

Instance: Xylocain-100mgml-cutspray-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Xylocain-100mgml-cutspray-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073729 "Cutaneous spray, solution"
* producedFrom = Reference(Xylocain-100mgml-cutspray-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: Xyloproct-RectalOintment-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Xyloproct-RectalOintment-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073828 "Rectal Ointment"
* producedFrom = Reference(Xyloproct-RectalOintment-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073628 "Rectal use"

Instance: LidoAcc-20mgml-InjSol-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(LidoAcc-20mgml-InjSol-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(LidoAcc-20mgml-InjSol-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073572 "Epidural use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000073600 "Intramuscular use"

Instance: Triolif-Mint-Lozenge-SE-AJ-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Triolif-Mint-Lozenge-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073703 "Lozenge"
* producedFrom = Reference(Triolif-Mint-Lozenge-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073621 "Oropharyngeal use"
* routeOfAdministration[+].code = $100000073345#100000073620 "Oromucosal use"



Instance: Fragmin-7500IE-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Fragmin-7500IE-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Fragmin-7500IE-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075556 "Extracorporeal use"


Instance: Fragmin-15000IE-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Fragmin-15000IE-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Fragmin-15000IE-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075556 "Extracorporeal use"

Instance: Fragmin-2500IEml-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Fragmin-2500IEml-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Fragmin-2500IEml-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075556 "Extracorporeal use"

Instance: Fragmin-5000IE-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Fragmin-5000IE-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Fragmin-5000IE-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075556 "Extracorporeal use"

Instance: Fragmin-10000IE-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Fragmin-10000IE-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Fragmin-10000IE-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075556 "Extracorporeal use"

Instance: Fragmin-18000IE-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Fragmin-18000IE-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Fragmin-18000IE-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075556 "Extracorporeal use"

Instance: Fragmin-10000IEml-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Fragmin-10000IEml-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Fragmin-10000IEml-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075556 "Extracorporeal use"


Instance: Fragmink-10000IE-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Fragmink-10000IE-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Fragmink-10000IE-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075556 "Extracorporeal use"

Instance: Fragmink-25000IE-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Fragmink-25000IE-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Fragmin-2500IE-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075556 "Extracorporeal use"

Instance: Fragmin-2500IE-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Fragmink-25000IE-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Fragmin-2500IE-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075556 "Extracorporeal use"

Instance: Fragmin-12500IE-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: PPLAdministrableProductDefinition
* status = #active
* formOf = Reference(Fragmink-12500IE-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(Fragmin-12500IE-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration[+].code = $100000073345#100000075556 "Extracorporeal use"


Instance: Fragmink-25000IE-Solution-SE-IS-ManufacturedItemDefinition
InstanceOf: PPLManufacturedItemDefinition
* status = #active
* manufacturedDoseForm = $200000000004#100000073863 "Solution for injection"
* unitOfPresentation = $200000000014#200000002158 "Vial"

Instance: MetforminAristo-1000mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #example
* status = #active
* formOf = Reference(MedicinalProductDefinition/MetforminAristo-1000mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MetforminAristo-1000mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MorfinAlt-20mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MorfinAlt-20mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MorfinAlt-20mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MFABECE-50mcg-Suspension-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MFABECE-50mcg-Suspension-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000174018 "Suspension for spray"
* producedFrom = Reference(ManufacturedItemDefinition/MFABECE-50mcg-Suspension-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073615 "Nasal use"

Instance: Dolcontin-5mg-Tablet-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Dolcontin-5mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Dolcontin-5mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Norspan-15h-Transderm-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Norspan-15h-Transderm-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073741 "Transdermal patch"
* producedFrom = Reference(ManufacturedItemDefinition/Norspan-15h-Transderm-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073637 "Transdermal use"

Instance: IMAmylan-400mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/IMAmylan-400mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/IMAmylan-400mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MorfinMeda-10mgml-Solution-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MorfinMeda-10mgml-Solution-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/MorfinMeda-10mgml-Solution-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"

Instance: Maxilene-40mg-cream-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Maxilene-40mg-cream-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073712 "Cream"
* producedFrom = Reference(ManufacturedItemDefinition/Maxilene-40mg-cream-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: BuprenorSTADA-10perh-Transderm-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/BuprenorSTADA-10perh-Transderm-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073741 "Transdermal patch"
* producedFrom = Reference(ManufacturedItemDefinition/BuprenorSTADA-10perh-Transderm-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073637 "Transdermal use"

Instance: BuprenorSTADA-5h-Transderm-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/BuprenorSTADA-5h-Transderm-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073741 "Transdermal patch"
* producedFrom = Reference(ManufacturedItemDefinition/BuprenorSTADA-5h-Transderm-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073637 "Transdermal use"

Instance: Glucophage-850mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Glucophage-850mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Glucophage-850mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DZPorifarm-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DZPorifarm-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/DZPorifarm-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: IMASTADA-600mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/IMASTADA-600mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/IMASTADA-600mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MorfinMeda-10mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MorfinMeda-10mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MorfinMeda-10mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Sendolor-1mgml-InfSolution-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Sendolor-1mgml-InfSolution-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073870 "Solution for infusion"
* producedFrom = Reference(ManufacturedItemDefinition/Sendolor-1mgml-InfSolution-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073572 "Epidural use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073608 "Intrathecal use"

Instance: AMLteva-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLteva-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLteva-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: ITZSTADA-100mg-Cap-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/ITZSTADA-100mg-Cap-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073375 "Capsule, hard"
* producedFrom = Reference(ManufacturedItemDefinition/ITZSTADA-100mg-Cap-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MetforminOri-500mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MetforminOri-500mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MetforminOri-500mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MetforminAuro-500mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MetforminAuro-500mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MetforminAuro-500mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Citodon-500mg30mg-EffTablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Citodon-500mg30mg-EffTablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073646 "Oral solution"
* producedFrom = Reference(ManufacturedItemDefinition/Citodon-500mg30mg-EffTablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Dolcontin-30mg-Tablet-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Dolcontin-30mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Dolcontin-30mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MetforminSandoz-500mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MetforminSandoz-500mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MetforminSandoz-500mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: InfluvacTetra-0.5ml-Suspension-SE-AJ-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/InfluvacTetra-0.5ml-Suspension-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073864 "Suspension for injection"
* producedFrom = Reference(ManufacturedItemDefinition/InfluvacTetra-0.5ml-Suspension-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration[0].code = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration[+].code = $100000073345#100000073633 "Subcutaneous use"

Instance: MetforminActavis-1000mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MetforminActavis-1000mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MetforminActavis-1000mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Alvedon500mgBrustablett-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Alvedon500mgBrustablett-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073646 "Oral solution"
* producedFrom = Reference(ManufacturedItemDefinition/Alvedon500mgBrustablett-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DicTratiopharma25mgFilmtablet-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DicTratiopharma25mgFilmtablet-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/DicTratiopharma25mgFilmtablet-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: AMLmedvalley-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLmedvalley-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLmedvalley-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Panocod-500mg30mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Panocod-500mg30mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Panocod-500mg30mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: BuprenorphineOri-2mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/BuprenorphineOri-2mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073698 "Sublingual tablet"
* producedFrom = Reference(ManufacturedItemDefinition/BuprenorphineOri-2mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073634 "Sublingual use"

Instance: AMLbluefish-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLbluefish-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLbluefish-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: IMAkoanaa-400mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/IMAkoanaa-400mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/IMAkoanaa-400mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: EnalaprilSandoz-20mg-Tablet-SE-AJ-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/EnalaprilSandoz-20mg-Tablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "tablet"
* producedFrom = Reference(ManufacturedItemDefinition/EnalaprilSandoz-20mg-Tablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: ISOactavis-10mg-Capsule-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/ISOactavis-10mg-Capsule-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073660 "Capsule, soft"
* producedFrom = Reference(ManufacturedItemDefinition/ISOactavis-10mg-Capsule-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: IMASTADA-100mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/IMASTADA-100mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/IMASTADA-100mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DiklofenakABECE116mgggel-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DiklofenakABECE116mgggel-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073726 "Gel"
* producedFrom = Reference(ManufacturedItemDefinition/DiklofenakABECE116mgggel-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: CefStragen-750mg-Powder-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/CefStragen-750mg-Powder-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000074038 "Solution for injection/infusion"
* producedFrom = Reference(ManufacturedItemDefinition/CefStragen-750mg-Powder-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"

Instance: Cortimyk20mgml10mgmlkram-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Cortimyk20mgml10mgmlkram-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073712 "Cream"
* producedFrom = Reference(ManufacturedItemDefinition/Cortimyk20mgml10mgmlkram-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: ITZactavis-100mg-Cap-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/ITZactavis-100mg-Cap-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073375 "Capsule, hard"
* producedFrom = Reference(ManufacturedItemDefinition/ITZactavis-100mg-Cap-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: BupropionSandoz-150mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/BupropionSandoz-150mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073668 "Modified-release tablet"
* producedFrom = Reference(ManufacturedItemDefinition/BupropionSandoz-150mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: IMAsandoz-100mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/IMAsandoz-100mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/IMAsandoz-100mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"


Instance: IMAkrkadd-100mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/IMAkrkadd-100mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/IMAkrkadd-100mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: SimvastatinBluefish-80mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/SimvastatinBluefish-80mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/SimvastatinBluefish-80mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: EnalaprilSandoz-10mg-Tablet-SE-AJ-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/EnalaprilSandoz-10mg-Tablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "tablet"
* producedFrom = Reference(ManufacturedItemDefinition/EnalaprilSandoz-10mg-Tablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: AMLbluefish-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLbluefish-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLbluefish-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: PKEvolan-500mg30mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/PKEvolan-500mg30mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/PKEvolan-500mg30mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: SertralineSUN100mgfilmtablett-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/SertralineSUN100mgfilmtablett-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/SertralineSUN100mgfilmtablett-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: IMAgrindeks-100mg-Capsule-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/IMAgrindeks-100mg-Capsule-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073375 "Capsule, hard"
* producedFrom = Reference(ManufacturedItemDefinition/IMAgrindeks-100mg-Capsule-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Norspan-5h-Transderm-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Norspan-5h-Transderm-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073741 "Transdermal patch"
* producedFrom = Reference(ManufacturedItemDefinition/Norspan-5h-Transderm-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073637 "Transdermal use"

Instance: DiklofenakOrifarm25Enterotablett-SE-PLC-AdminProdDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DiklofenakOrifarm25Enterotablett-SE-PLC-MedProdDef)
* administrableDoseForm = $200000000004#100000073667 "Gastro-resistant tablet"
* producedFrom = Reference(ManufacturedItemDefinition/DiklofenakOrifarm25Enterotablett-SE-PLC-ManItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MetforminAuro-1000mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MetforminAuro-1000mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MetforminAuro-1000mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: AMLsandoz-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLsandoz-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLsandoz-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: AMLvitabalans-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLvitabalans-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLvitabalans-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: ISOorifarm-20mg-Capsule-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/ISOorifarm-20mg-Capsule-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073660 "Capsule, soft"
* producedFrom = Reference(ManufacturedItemDefinition/ISOorifarm-20mg-Capsule-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: HermolepsinR-300mg-PRTablet-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/HermolepsinR-300mg-PRTablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(ManufacturedItemDefinition/HermolepsinR-300mg-PRTablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: EnalaprilSandoz-5mg-Tablet-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/EnalaprilSandoz-5mg-Tablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "tablet"
* producedFrom = Reference(ManufacturedItemDefinition/EnalaprilSandoz-5mg-Tablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: AMLkrka-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLkrka-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLkrka-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DZPdesitin-10mg-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DZPdesitin-10mg-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073829 "Rectal solution"
* producedFrom = Reference(ManufacturedItemDefinition/DZPdesitin-10mg-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073628 "Rectal use"

Instance: MetforminSandoz-1000mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MetforminSandoz-1000mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MetforminSandoz-1000mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Panodil60mgsuppositorium-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Panodil60mgsuppositorium-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073843 "Suppository"
* producedFrom = Reference(ManufacturedItemDefinition/Panodil60mgsuppositorium-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073628 "Rectal use"

Instance: Norspan-30h-Transderm-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Norspan-30h-Transderm-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073741 "Transdermal patch"
* producedFrom = Reference(ManufacturedItemDefinition/Norspan-30h-Transderm-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073637 "Transdermal use"

Instance: Concerta-36mg-PRTablet-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Concerta-36mg-PRTablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Concerta-36mg-PRTablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: SimvastatinBluefish-20mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/SimvastatinBluefish-20mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/SimvastatinBluefish-20mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Aprokam-50mg-Powder-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Aprokam-50mg-Powder-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/Aprokam-50mg-Powder-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000125763 "Intracameral use"

Instance: EMLA-2525-Plaster-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/EMLA-2525-Plaster-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073714 "Medicated plaster"
* producedFrom = Reference(ManufacturedItemDefinition/EMLA-2525-Plaster-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: Airomir0.1Spray-SE-PLC-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Airomir0.1Spray-SE-PLC-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073838 "Pressurised inhalation, suspension"
* producedFrom = Reference(ManufacturedItemDefinition/Airomir0.1Spray-SE-PLC-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073584 "Inhalation use"

Instance: Panodil500mgoralsolutionsachet-SE-PLC-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Panodil500mgoralsolutionsachet-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073646 "Oral solution"
* producedFrom = Reference(ManufacturedItemDefinition/Panodil500mgoralsolutionsachet-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Herceptin-150mg-Powder-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Herceptin-150mg-Powder-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073870 "Solution for infusion"
* producedFrom = Reference(ManufacturedItemDefinition/Herceptin-150mg-Powder-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073611 "Intravenous use"

Instance: Anafranil-25mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Anafranil-25mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073380 "Coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Anafranil-25mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Panocod-500mg30mg-EffTablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Panocod-500mg30mg-EffTablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073646 "Oral solution"
* producedFrom = Reference(ManufacturedItemDefinition/Panocod-500mg30mg-EffTablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: AMLteva-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLteva-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLteva-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DiklofenakNET232mgggel-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DiklofenakNET232mgggel-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073726 "Gel"
* producedFrom = Reference(ManufacturedItemDefinition/DiklofenakNET232mgggel-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: Dolcontin-60mg-Tablet-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Dolcontin-60mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Dolcontin-60mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Sandimmun50mgmlkoncentrat-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Sandimmun50mgmlkoncentrat-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073870 "Solution for infusion"
* producedFrom = Reference(ManufacturedItemDefinition/Sandimmun50mgmlkoncentrat-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073611 "Intravenous use"

Instance: SandimmunNeoral100mgmlorallos-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/SandimmunNeoral100mgmlorallos-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073646 "Oral solution"
* producedFrom = Reference(ManufacturedItemDefinition/SandimmunNeoral100mgmlorallos-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MFteva-50mcg-Suspension-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MFteva-50mcg-Suspension-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000174018 "Suspension for spray"
* producedFrom = Reference(ManufacturedItemDefinition/MFteva-50mcg-Suspension-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073615 "Nasal use"

Instance: AMLmedvalley-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLmedvalley-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLmedvalley-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Denela-2525-Cream-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Denela-2525-Cream-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073712 "Cream"
* producedFrom = Reference(ManufacturedItemDefinition/Denela-2525-Cream-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: MorphineUni-1mgml-Solution-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MorphineUni-1mgml-Solution-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/MorphineUni-1mgml-Solution-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073572 "Epidural use"

Instance: Dolcontin-10mg-Tablet-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Dolcontin-10mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Dolcontin-10mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: SimvastatinBluefish-40mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/SimvastatinBluefish-40mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/SimvastatinBluefish-40mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: CefuroximMIP-750mg-Powder-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/CefuroximMIP-750mg-Powder-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/CefuroximMIP-750mg-Powder-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"

Instance: MetforminAristo-500mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MetforminAristo-500mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MetforminAristo-500mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: AMLaurobindo-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLaurobindo-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLaurobindo-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DiklofenakTApofri50mgFilmtablet-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DiklofenakTApofri50mgFilmtablet-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/DiklofenakTApofri50mgFilmtablet-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: SandimmunNeoral25mgkapselmjuk-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/SandimmunNeoral25mgkapselmjuk-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073660 "Capsule, soft"
* producedFrom = Reference(ManufacturedItemDefinition/SandimmunNeoral25mgkapselmjuk-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Ignorin50mgFilmtablet-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Ignorin50mgFilmtablet-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Ignorin50mgFilmtablet-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MorfinEpMeda-10mgml-Solution-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MorfinEpMeda-10mgml-Solution-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/MorfinEpMeda-10mgml-Solution-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073572 "Epidural use"

Instance: BuprenorSTADA-20h-Transderm-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/BuprenorSTADA-20h-Transderm-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073741 "Transdermal patch"
* producedFrom = Reference(ManufacturedItemDefinition/BuprenorSTADA-20h-Transderm-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073637 "Transdermal use"

Instance: BuprenorphineOri-8mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/BuprenorphineOri-8mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073698 "Sublingual tablet"
* producedFrom = Reference(ManufacturedItemDefinition/BuprenorphineOri-8mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073634 "Sublingual use"

Instance: MetforminActavis-500mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MetforminActavis-500mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MetforminActavis-500mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DiklofenakOrifarm50Enterotablett-SE-PLC-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DiklofenakOrifarm50Enterotablett-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073667 "Gastro-resistant tablet"
* producedFrom = Reference(ManufacturedItemDefinition/DiklofenakOrifarm50Enterotablett-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Mydrane-InjSol-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Mydrane-InjSol-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/Mydrane-InjSol-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000125763 "Intracameral use"

Instance: SertralinTeva50mgfilmtablett-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/SertralinTeva50mgfilmtablett-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/SertralinTeva50mgfilmtablett-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MorfinAbcur-10mgml-Solution-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MorfinAbcur-10mgml-Solution-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/MorfinAbcur-10mgml-Solution-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"

Instance: ISOsandoz-10mg-Capsule-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/ISOsandoz-10mg-Capsule-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073660 "Capsule, soft"
* producedFrom = Reference(ManufacturedItemDefinition/ISOsandoz-10mg-Capsule-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: EMLA-2525-Cream-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/EMLA-2525-Cream-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073712 "Cream"
* producedFrom = Reference(ManufacturedItemDefinition/EMLA-2525-Cream-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: MorfinKalceks-10mgml-Solution-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MorfinKalceks-10mgml-Solution-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/MorfinKalceks-10mgml-Solution-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"

Instance: AnafranilRet-75mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AnafranilRet-75mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AnafranilRet-75mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MForion-50mcg-Suspension-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MForion-50mcg-Suspension-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000174018 "Suspension for spray"
* producedFrom = Reference(ManufacturedItemDefinition/MForion-50mcg-Suspension-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073615 "Nasal use"

Instance: SimvastatinBluefish-10mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/SimvastatinBluefish-10mg-Tablet-SE-BS-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/SimvastatinBluefish-10mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DiklofenakTeva116mgggelSE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DiklofenakTeva116mgggel-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073726 "Gel"
* producedFrom = Reference(ManufacturedItemDefinition/DiklofenakTeva116mgggel-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: Anafranil-12mgml-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Anafranil-12mgml-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/Anafranil-12mgml-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"

Instance: Norspan-40h-Transderm-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Norspan-40h-Transderm-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073741 "Transdermal patch"
* producedFrom = Reference(ManufacturedItemDefinition/Norspan-40h-Transderm-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073637 "Transdermal use"

Instance: Glucophage-1000mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Glucophage-1000mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Glucophage-1000mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: HydrokortisonOrifarm20mgTablett-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/HydrokortisonOrifarm20mgTablett-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/HydrokortisonOrifarm20mgTablett-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: EnalaprilSandoz-2.5mg-Tablet-SE-AJ-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/EnalaprilSandoz-2.5mg-Tablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "tablet"
* producedFrom = Reference(ManufacturedItemDefinition/EnalaprilSandoz-2.5mg-Tablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: AMLaccord-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLaccord-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLaccord-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: PinexJordgubb250mggranulat-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/PinexJordgubb250mggranulat-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073372 "Granules"
* producedFrom = Reference(ManufacturedItemDefinition/PinexJordgubb250mggranulat-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: ISOorifarm-10mg-Capsule-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/ISOorifarm-10mg-Capsule-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073660 "Capsule, soft"
* producedFrom = Reference(ManufacturedItemDefinition/ISOorifarm-10mg-Capsule-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DiklofenakApofri116gel-SE-PLC-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DiklofenakApofri116gel-SE-PLC-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073726 "Gel"
* producedFrom = Reference(ManufacturedItemDefinition/DiklofenakApofri116gel-SE-PLC-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: DZPdesitin-5mg-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DZPdesitin-5mg-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073829 "Rectal solution"
* producedFrom = Reference(ManufacturedItemDefinition/DZPdesitin-5mg-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073628 "Rectal use"

Instance: Instillagel-209-Gel-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Instillagel-209-Gel-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073726 "Gel"
* producedFrom = Reference(ManufacturedItemDefinition/Instillagel-209-Gel-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073638 "Urethral use"

Instance: Nitrolingual04mgdossublingualspray-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Nitrolingual04mgdossublingualspray-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000143499 "Sublingual spray, solution"
* producedFrom = Reference(ManufacturedItemDefinition/Nitrolingual04mgdossublingualspray-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073634 "Sublingual use"

Instance: CoversylNovum-5mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/CoversylNovum-5mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/CoversylNovum-5mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Norspan-10h-Transderm-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Norspan-10h-Transderm-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073741 "Transdermal patch"
* producedFrom = Reference(ManufacturedItemDefinition/Norspan-10h-Transderm-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073637 "Transdermal use"

Instance: Amlodistad-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Amlodistad-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Amlodistad-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Anafranil-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Anafranil-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073380 "Coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Anafranil-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Elvanse-50mg-Capsule-SE-AJ-AdministrableProductDefinition01
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Elvanse-50mg-Capsule-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073375 "Capsule, hard"
* producedFrom = Reference(ManufacturedItemDefinition/Elvanse-50mg-Capsule-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Elvanse-50mg-Capsule-SE-AJ-AdministrableProductDefinition02
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Elvanse-50mg-Capsule-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073646 "Oral solution"
* producedFrom = Reference(ManufacturedItemDefinition/Elvanse-50mg-Capsule-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: CiklosporinIVAX25mgkapselmjuk-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/CiklosporinIVAX25mgkapselmjuk-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073660 "Capsule, soft"
* producedFrom = Reference(ManufacturedItemDefinition/CiklosporinIVAX25mgkapselmjuk-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: HermolepsinR-100mg-PRTablet-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/HermolepsinR-100mg-PRTablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(ManufacturedItemDefinition/HermolepsinR-100mg-PRTablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Mommox-50mcg-Suspension-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Mommox-50mcg-Suspension-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000174018 "Suspension for spray"
* producedFrom = Reference(ManufacturedItemDefinition/Mommox-50mcg-Suspension-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073615 "Nasal use"

Instance: CefuroximStragen-1.5g-Powder-SE-IS-AdminProdDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/CefuroximStragen-1.5g-Powder-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000074038 "Solution for injection/infusion"
* producedFrom = Reference(ManufacturedItemDefinition/CefuroximStragen-1.5g-Powder-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"

Instance: DiklofenakApofri232mgggel-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DiklofenakApofri232mgggel-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073726 "Gel"
* producedFrom = Reference(ManufacturedItemDefinition/DiklofenakApofri232mgggel-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: Nobligan100mgmloraladropparlos-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Nobligan100mgmloraladropparlos-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073642 "Oral drops, solution"
* producedFrom = Reference(ManufacturedItemDefinition/Nobligan100mgmloraladropparlos-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: HermolepsinR-200mg-PRTablet-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/HermolepsinR-200mg-PRTablet-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073683 "Prolonged-release tablet"
* producedFrom = Reference(ManufacturedItemDefinition/HermolepsinR-200mg-PRTablet-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: AMLsandoz-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLsandoz-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLsandoz-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MetforminActavis-850mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MetforminActavis-850mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MetforminActavis-850mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Altermol-500mg30mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Altermol-500mg30mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Altermol-500mg30mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Citodon-1g60mg-Suppository-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Citodon-1g60mg-Suppository-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073843 "Suppository"
* producedFrom = Reference(ManufacturedItemDefinition/Citodon-1g60mg-Suppository-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073628 "Rectal use"

Instance: HydrokortisonEvolan10mgpergsalva-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/HydrokortisonEvolan10mgpergsalva-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073713 "Ointment"
* producedFrom = Reference(ManufacturedItemDefinition/HydrokortisonEvolan10mgpergsalva-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: Alburex-200g-L-Solution-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Alburex-200g-L-Solution-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073870 "solution for infusion"
* producedFrom = Reference(ManufacturedItemDefinition/Alburex-200g-L-Solution-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073611 "Intravenous use"

Instance: NitroglycerinAbicurinfu-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/NitroglycerinAbicurinfu-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073870 "Solution for infusion"
* producedFrom = Reference(ManufacturedItemDefinition/NitroglycerinAbicurinfu-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073611 "Intravenous use"

Instance: Norvasc-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Norvasc-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Norvasc-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: ABASAGLAR-100eml-Solution-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/ABASAGLAR-100eml-Solution-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/ABASAGLAR-100eml-Solution-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073633 "Subcutaneous use"

Instance: AMLaccord-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLaccord-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLaccord-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: IMASTADA-400mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/IMASTADA-400mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/IMASTADA-400mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: CefStragen-250mg-Powder-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/CefStragen-250mg-Powder-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/CefStragen-250mg-Powder-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"

Instance: Glucophage-500mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Glucophage-500mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Glucophage-500mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DZPorifarm-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DZPorifarm-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/DZPorifarm-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Sendolor-1mgml-Solution-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Sendolor-1mgml-Solution-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/Sendolor-1mgml-Solution-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code.coding[0] = $100000073345#100000073633 "Subcutaneous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073600 "Intramuscular use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073611 "Intravenous use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073572 "Epidural use"
* routeOfAdministration.code.coding[+] = $100000073345#100000073608 "Intrathecal use"

Instance: IMAkoanaa-100mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/IMAkoanaa-100mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/IMAkoanaa-100mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: AMLjubilant-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLjubilant-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLjubilant-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: CitodonEv-500mg30mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/CitodonEv-500mg30mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/CitodonEv-500mg30mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: IMAkrkadd-400mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/IMAkrkadd-400mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/IMAkrkadd-400mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Momenex-50mcg-Suspension-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Momenex-50mcg-Suspension-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000174018 "Suspension for spray"
* producedFrom = Reference(ManufacturedItemDefinition/Momenex-50mcg-Suspension-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073615 "Nasal use"

Instance: Amlodistad-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Amlodistad-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Amlodistad-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DicTratiopharma50mgFilmtablet-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DicTratiopharma50mgFilmtablet-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/DicTratiopharma50mgFilmtablet-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Nobligan50mgkapselhard-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Nobligan50mgkapselhard-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073375 "Capsule, hard"
* producedFrom = Reference(ManufacturedItemDefinition/Nobligan50mgkapselhard-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Dicuno50mgFilmtablet-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Dicuno50mgFilmtablet-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Dicuno50mgFilmtablet-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MorfinSpecial-2mgml-Solution-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MorfinSpecial-2mgml-Solution-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073863 "Solution for injection"
* producedFrom = Reference(ManufacturedItemDefinition/MorfinSpecial-2mgml-Solution-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073572 "Epidural use"

Instance: ISOactavis-20mg-Capsule-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/ISOactavis-20mg-Capsule-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073660 "Capsule, soft"
* producedFrom = Reference(ManufacturedItemDefinition/ISOactavis-20mg-Capsule-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DiclofenacOrifarm116mgggel-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DiclofenacOrifarm116mgggel-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073726 "Gel"
* producedFrom = Reference(ManufacturedItemDefinition/DiclofenacOrifarm116mgggel-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073566 "Cutaneous use"

Instance: Norvasc-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Norvasc-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Norvasc-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MFapofri-50mcg-Suspension-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MFapofri-50mcg-Suspension-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000174018 "Suspension for spray"
* producedFrom = Reference(ManufacturedItemDefinition/MFapofri-50mcg-Suspension-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073615 "Nasal use"

Instance: IMAmylan-100mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/IMAmylan-100mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/IMAmylan-100mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: AMLvitabalans-5mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLvitabalans-5mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLvitabalans-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: AMLjubilant-10mg-Tablet-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/AMLjubilant-10mg-Tablet-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/AMLjubilant-10mg-Tablet-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: DepoMedrolcumLido-4010-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/DepoMedrolcumLido-4010-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073864 "Suspension for injection"
* producedFrom = Reference(ManufacturedItemDefinition/DepoMedrolcumLido-4010-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073623 "Periarticular use"

Instance: Glytrin04mgdossublingualspray-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Glytrin04mgdossublingualspray-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000143499 "Sublingual spray, solution"
* producedFrom = Reference(ManufacturedItemDefinition/Glytrin04mgdossublingualspray-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073634 "Sublingual use"

Instance: Aphiahsone-50mcg-Suspension-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Aphiahsone-50mcg-Suspension-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000174018 "Suspension for spray"
* producedFrom = Reference(ManufacturedItemDefinition/Aphiahsone-50mcg-Suspension-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073615 "Nasal use"


Instance: MorfinMeda-20mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MorfinMeda-20mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MorfinMeda-20mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Alvedon250mgMunsonderTablett-SE-PLC-AdminProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Alvedon250mgMunsonderTablett-SE-PLC-MedicinalProductDef)
* administrableDoseForm = $200000000004#100000073666 "Orodispersible tablet"
* producedFrom = Reference(ManufacturedItemDefinition/Alvedon250mgMunsonderTablett-SE-PLC-ManufacturedItemDef)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Isotracin-10mg-Capsule-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Isotracin-10mg-Capsule-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073660 "Capsule, soft"
* producedFrom = Reference(ManufacturedItemDefinition/Isotracin-10mg-Capsule-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: MorfinAlt-10mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MorfinAlt-10mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073664 "Tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MorfinAlt-10mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: Nasonex-50mcg-Suspension-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Nasonex-50mcg-Suspension-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000174018 "Suspension for spray"
* producedFrom = Reference(ManufacturedItemDefinition/Nasonex-50mcg-Suspension-SE-IS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073615 "Nasal use"

Instance: Alburex-50g-L-Solution-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Alburex-50g-L-Solution-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073870 "solution for infusion"
* producedFrom[0] = Reference(ManufacturedItemDefinition/Alburex-50g-L-Solution-SE-AJ-ManufacturedItemDefinition01)
* producedFrom[+] = Reference(ManufacturedItemDefinition/Alburex-50g-L-Solution-SE-AJ-ManufacturedItemDefinition02)
* routeOfAdministration.code = $100000073345#100000073611 "Intravenous use"

Instance: MetforminSandoz-850mg-Tablet-SE-BS-AdministrableProductDef
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/MetforminSandoz-850mg-Tablet-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073665 "Film-coated tablet"
* producedFrom = Reference(ManufacturedItemDefinition/MetforminSandoz-850mg-Tablet-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073619 "Oral use"

Instance: CBZEssPharm-125mg-Supp-SE-AJ-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/CBZEssPharm-125mg-Supp-SE-AJ-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073843 "Suppository"
* producedFrom = Reference(ManufacturedItemDefinition/CBZEssPharm-125mg-Supp-SE-AJ-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073628 "Rectal use"

Instance: Norspan-20h-Transderm-SE-BS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Norspan-20h-Transderm-SE-BS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073741 "Transdermal patch"
* producedFrom = Reference(ManufacturedItemDefinition/Norspan-20h-Transderm-SE-BS-ManufacturedItemDefinition)
* routeOfAdministration.code = $100000073345#100000073637 "Transdermal use"



Instance: Curocef1500mgPulver-A-HL-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(MedicinalProductDefinition/Curocef1500mgPulver-A-HL-MedicinalProductDefinition)
* administrableDoseForm = $200000000004_1#100000074038 "Solution for injection/infusion"
* unitOfPresentation = $200000000014#200000002164 "Ampoule"
* routeOfAdministration[0].code = $100000073345_1#100000073600 "Intramuscular use"
* routeOfAdministration[+].code = $100000073345_1#100000073611 "Intravenous use"


Instance: Smofkabiven-Emulsion-SE-IS-AdministrableProductDefinition
InstanceOf: AdministrableProductDefinition
Usage: #inline
* status = #active
* formOf = Reference(Smofkabiven-Emulsion-SE-IS-MedicinalProductDefinition)
* administrableDoseForm = $200000000004#100000073858 "Emulsion for infusion"
* unitOfPresentation = $200000000014#200000002164 "Ampoule"
* routeOfAdministration[+].code = $100000073345#100000073611 "Intravenous use"
* producedFrom = Reference(Smofkabiven-Emulsion-SE-IS-ManufacturedItemDefinition)

        """
)
f.close()


# clean the target folder
f = open(org_file, "w")
f.truncate()
f.close()

list_of_locs = []


def create_org(regauth):
    # print(regauth)
    instance_value = re.search(r"Instance:\s*(\S+)", regauth)
    if instance_value:
        value = instance_value.group(1)
    #  print(value)
    ### get loc value
    if "* holder.identifier.value" in regauth:
        loc_value = re.search(r"\* holder.identifier.value = \"\s?(\S+)\s?\"", regauth)
        if loc_value:
            loc = loc_value.group(1)

        print(loc)
    else:
        print(
            "no loc --------------------------------------------------------------------------"
        )
        return regauth
    ### get loc value
    if "* holder.display" in regauth:
        disp_value = re.search(r"\* holder.display = \"(.+)\"", regauth)
        if disp_value:
            disp = disp_value.group(1)
            # print(disp)
    else:
        disp = "No name"
    if loc not in list_of_locs:
        f = open(org_file, "a")

        f.write("""Instance:""")
        f.write(" " + loc)
        f.write(
            """\nInstanceOf: PPLOrganization
Usage: #example
Description: "Marketing Authorisation Holder / Organisation"

* identifier[loc].value = """
        )
        f.write('"' + loc + '"\n' + '* name = "' + disp + '"\n\n')
        # f.write(contents)
        f.close()
        list_of_locs.append(loc)

    regauth = re.sub("\* holder.+ = .+\n", "", regauth)
    regauth += "\n* holder = Reference(" + loc + ")\n"
    # print(regauth)

    return regauth


for file in listdir(FOLDER):
    print(file)
    res = file.split("-")[-1].split(".")[0]
    # print(res)

    resname = file.rsplit("-", 1)[0]
    # print(resname)
    with open(FOLDER + "/" + file) as f:
        contents = f.read()
        #   print(contents)

        # Find the value after "Instance:" using regex
        instance_value = re.search(r"Instance:\s*(\S+)", contents)
        if instance_value:
            value = instance_value.group(1)
            # print("Original value:", value)

            # Check the length of the value
            if len(value) > 64:
                # Generate a hash and replace the value
                hashed_value = hashlib.sha256(value.encode()).hexdigest()
                contents = contents.replace(value, hashed_value)
                # print("Replaced value:", hashed_value)
                # print(contents)
        contents = re.sub(r"\* meta.versionId = \"(\S+)\"", "", contents)
        contents = re.sub(r"\* meta.lastUpdated = \"(.+)\"\n", "", contents)
        contents = contents.replace("$220000000060_1", "$220000000060")

        contents = contents.replace("Usage: #inline\n", "")

        ##non just numeric ids
        contents = re.sub(r"Reference\((\d{3,20})\)\n", r"Reference(j\1) \n", contents)
        contents = re.sub(r"resource = (\d{3,20})\n", r"resource = j\1 \n", contents)
        contents = re.sub(r"Instance: (\d{3,20})\n", r"Instance: j\1 \n", contents)

        # Instance: 20170630100020

        #  if any(blacklist_ids in contents):
        #      print(contents)
        contents = contents.replace(
            '* holder = Reference(1) "Glaxosmithkline Produtos Farmaceuticos Lda."',
            '//DUMMY\n* holder = Reference(LOC-100000549) "Glaxosmithkline Produtos Farmaceuticos Lda."',
        )
        contents = contents.replace("$220000000060_1", "$220000000060")
        contents = contents.replace("$200000000004_1", "$200000000004")
        contents = contents.replace("$100000000004_1", "$100000000004")
        contents = contents.replace("$100000072051_1", "$100000072051")
        contents = contents.replace("$100000000002_1", "$100000000002")
        contents = contents.replace("$100000072049_1", "$100000072049")
        contents = contents.replace("$200000000014_1", "$200000000014")
        contents = contents.replace("$100000093533_1", "$100000093533")
        contents = contents.replace("$100000072050_1", "$100000072050")
        contents = contents.replace("$100000154441_1", "$100000154441")
        contents = contents.replace("$100000154442_1", "$100000154442")
        contents = contents.replace("$100000072052_1", "$100000072052")
        contents = contents.replace("Inflitration", "Infiltration")
        contents = contents.replace(
            '$100000073345#100000073628 "Retal use"',
            '$100000073345#100000073628 "Rectal use"',
        )
        contents = contents.replace("$100000073345_1", "$100000073345")
        contents = contents.replace("$atc_1", "$atc")
        contents = contents.replace("$SubstanceDefinition_1", "$SubstanceDefinition")
        contents = contents.replace("-AdministrableProductDefinition", "-APD")
        contents = contents.replace("-ManufacturedItemDefinition", "-MID")
        contents = contents.replace("-PackagedProductDefinition", "-PPD")
        contents = contents.replace("-MedicinalProductDefinition", "-MPD")
        contents = contents.replace("-Ingredient", "-ING")
        contents = contents.replace("-AdministrableProductDef", "-APD")
        contents = contents.replace("-AdminProductDef", "-APD")
        contents = contents.replace("-ManufacturedItemDef", "-MID")
        contents = contents.replace("-PackagedProductDef", "-PPD")
        contents = contents.replace("-PackageProductDef", "-PPD")
        contents = contents.replace("-MedicinalProductDef", "-MPD")
        contents = contents.replace("-RegulatedAuthorization", "-RA")
        contents = contents.replace(
            '$100000000002#100000000535 "Sweden"',
            '$100000000002#100000000535 "Kingdom of Sweden"',
        )
        contents = contents.replace(
            "ProductnameStrengthPharmaceuticaldoseform-SE-PLC-ManufacturedItemDef",
            "Glytrin04mgdossublingualspray-SE-PLC-MID",
        )
        # contents = contents.replace()
        contents = contents.replace("[0].", "[+].")

        if '.coding.code = "' in contents:  ###gofsh error?
            contents = re.sub(
                r'.coding.code = "(\w+)"', r".coding.code = #\1", contents
            )
        if ".amount.code = " in contents:  ###gofsh error?
            contents = re.sub(
                r'.amount.code = "(\w+)"', r".amount.code = #\1", contents
            )
        if ".code = " in contents:  ###gofsh error?
            contents = re.sub(r'.code = "(\w+)"', r".code = #\1", contents)

        ####### Administrable PRODUCT DEFINITION ####################################
        if "InstanceOf: AdministrableProductDefinition" in contents:
            # print("yes")
            contents = contents.replace(
                "InstanceOf: AdministrableProductDefinition",
                "InstanceOf: PPLAdministrableProductDefinition",
            )
            # print(contents)

            contents = re.sub(
                r"formOf = Reference\(\w+\/(.+)\)",
                r"formOf = Reference(\1)",
                contents,
            )
            contents = re.sub(
                r"producedFrom = Reference\(\w+\/(.+)\)",
                r"producedFrom = Reference(\1)",
                contents,
            )
            # print("Original value:", value)
        # * formOf = Reference(MedicinalProductDefinition/Amlodistad-5mg-Tablet-SE-IS-MedicinalProductDefinition)
        # * administrableDoseForm = $200000000004#100000073664 "Tablet"
        # * producedFrom = Reference(ManufacturedItemDefinition/Amlodistad-5mg-Tablet-SE-IS-ManufacturedItemDefinition)
        ####### MEDICINAL PRODUCT DEFINITION ####################################

        if "InstanceOf: MedicinalProductDefinition" in contents:
            #    print("yes")
            contents = contents.replace(
                "InstanceOf: MedicinalProductDefinition",
                "InstanceOf: PPLMedicinalProductDefinition",
            )
            contents = contents.replace(
                "name.countryLanguage.country",
                "name.usage.country",
            )
            contents = contents.replace(
                "name.countryLanguage.language",
                "name.usage.language",
            )
            contents = contents.replace(
                "name.namePart",
                "name.part",
            )
            contents = contents.replace(
                '* marketingStatus.status.coding[0] = xx#xx "xx"',
                '//DUMMY\n* marketingStatus.status.coding[0] = $100000072052#100000072083 "Marketed"',
            )

            if "* legalStatusOfSupply" not in contents:
                contents += '\n//DUMMY\n* legalStatusOfSupply = $100000072051#100000072084 "Medicinal product subject to medical prescription"'

            if "* domain" not in contents:
                contents += (
                    '\n//DUMMY\n* domain = $100000000004#100000000012 "Human use"'
                )

            if (
                'extension.url = "http://ema.europa.eu/fhir/extension/authorisedDoseForm"'
                in contents
            ):
                if "* extension.valueCoding " in contents:
                    contents = contents.replace(
                        "* extension.valueCoding", "* combinedPharmaceuticalDoseForm"
                    )
            if "* combinedPharmaceuticalDoseForm" not in contents:
                contents += '\n//DUMMY\n* combinedPharmaceuticalDoseForm = $200000000004#100000116186 "Powder for solution for injection/infusion"'

            contents = contents.replace(
                """* legalStatusOfSupply.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* legalStatusOfSupply.coding.extension.valueInteger = 1""",
                "",
            )
            contents = contents.replace(
                """* domain.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* domain.coding.extension.valueInteger = 1""",
                "",
            )
            contents = contents.replace(
                """* combinedPharmaceuticalDoseForm.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* combinedPharmaceuticalDoseForm.extension.valueInteger = 1""",
                "",
            )
            contents = contents.replace(
                """* classification[+].coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* classification[=].coding.extension.valueInteger = 1""",
                "",
            )

            contents = contents.replace(
                """* classification[=].coding = $200000000324#200000003517 "Other"\n""",
                """* classification[+].coding = $200000000324#200000003517 "Other"\n""",
            )
            contents = contents.replace(
                '* extension.url = "http://ema.europa.eu/fhir/extension/authorisedDoseForm"',
                "",
            )
            contents = contents.replace(
                '* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"',
                "",
            )
            contents = contents.replace(
                """* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072288 "Swedish"\n""",
                "",
            )

            contents = contents.replace(
                """* attachedDocument = Reference(DocumentReference/Curocef1500mgPulver-A-HL-DocumentReference01)
* masterFile = Reference(mfl1)
* contact[+].type.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* contact[=].type.coding.extension.valueInteger = 1
* contact[=].type.coding = $100000154441#100000155057 "Qualified Person in the EEA for Pharmacovigilance"
* contact[=].contact = Reference(qppv1)
* contact[+].type.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* contact[=].type.coding.extension.valueInteger = 3
* contact[=].type.coding = $100000154441#200000017719
* contact[=].contact = Reference(phvenq1)""",
                "",
            )

            contents = contents.replace(
                "http://spor.ema.europa.eu/v1/lists/100000000002",
                "https://spor.ema.europa.eu/v1/lists/100000000002",
            )
            ###language
            contents = contents.replace(
                """* name.usage.language.coding.system = "http://spor.ema.europa.eu/v1/lists/100000072057"
* name.usage.language.coding.code = #100000072288
* name.usage.language.coding.display = "Swedish\"""",
                """* name.usage.language = urn:ietf:bcp:47#sv "Swedish\" """,
            )
            contents = contents.replace(
                """* name.usage.language.coding.system = "http://spor.ema.europa.eu/v1/lists/100000072057"
* name.usage.language.coding.code = #100000072172
* name.usage.language.coding.display = "Estonian\"""",
                """* name.usage.language = urn:ietf:bcp:47#et "Estonian\" """,
            )
            contents = contents.replace(
                """* name.usage.language.coding.system = "https://spor.ema.europa.eu/v1/lists/100000072057/terms/100000072251"
* name.usage.language.coding.code = "100000072251"
* name.usage.language.coding.display = "Portuguese\"""",
                """* name.usage.language = urn:ietf:bcp:47#pt "Portuguese\" """,
            )
            contents = contents.replace(
                """* name.usage.language.coding.system = "https://spor.ema.europa.eu/v1/lists/100000072057"
* name.usage.language.coding.code = #100000072178
* name.usage.language.coding.display = "German\"""",
                """* name.usage.language = urn:ietf:bcp:47#de "German\"\n""",
            )
            contents = contents.replace(
                """* name.usage.language.coding.system = "https://spor.ema.europa.eu/v1/lists/100000072057"
* name.usage.language.coding.code = "100000072149"
* name.usage.language.coding.display = "Finnish\"""",
                """* name.usage.language = urn:ietf:bcp:47#fi "Finnish\" """,
            )

            contents = contents.replace(
                "https://hl7.org/fhir/publication-status",
                "http://hl7.org/fhir/publication-status",
            )
            if '* name.usage.country.coding.display = "Sweden"':
                contents = contents.replace(
                    '* name.usage.country.coding.display = "Sweden"',
                    '* name.usage.country.coding.display = "Kingdom of Sweden"',
                )
            contents += '\n* name.usage.country.coding.display = "Kingdom of Sweden"\n* name.usage.language = urn:ietf:bcp:47#sv "Swedish"\n'
            contents = contents.replace(
                '* classification = $100000093533#100000094031 "A10BA02"',
                '* classification = $100000093533#100000094031 "metformin"',
            )
            contents = contents.replace(
                '* classification = $100000093533#100000095104 "C09AA02"',
                '* classification = $100000093533#100000095104 "enalapril"',
            )
            contents = contents.replace(
                '* classification = $100000093533#100000095169 "C10AA01"',
                '* classification = $100000093533#100000095169 "simvastatin"',
            )
            contents = contents.replace(
                '* classification = $100000093533#100000097139 "N02AA01"',
                '* classification = $100000093533#100000097139 "morphine"',
            )
            contents = contents.replace(
                '* classification = $100000093533#100000095104 "C09AA02"',
                '* classification = $100000093533#100000095104 "enalapril"',
            )
            contents = contents.replace(
                '* classification = $100000093533#100000098065 "R03AC02"',
                '* classification = $100000093533#100000098065 "salbutamol"',
            )
            contents = contents.replace(
                '* classification = $100000093533#100000094266 "B01AB05"',
                '* classification = $100000093533#100000094266 "enoxaparin"',
            )
            contents = contents.replace(
                '* classification = $100000093533#100000097495 "N07BC01"',
                '* classification = $100000093533#100000097495 "buprenorphine"',
            )
            contents = contents.replace(
                '* classification = $100000093533#100000097705 "N06AX12"',
                '* classification = $100000093533#100000097705 "bupropion"',
            )
            contents = contents.replace(
                '* classification = $100000093533#100000097377 "N03AF01"',
                '* classification = $100000093533#100000097377 "carbamazepine"',
            )
        ####### INGREDIENT ############################################################################################################
        if "InstanceOf: Ingredient" in contents:
            #    print("yes")
            contents = contents.replace(
                "InstanceOf: Ingredient",
                "InstanceOf: PPLIngredient",
            )
            contents = contents.replace(
                '* role = $100000072072#100000072072 "Active"',
                '* role = $100000072050#100000072072 "Active"',
            )

            contents = contents.replace(
                """* substance.strength.presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"\n""",
                "",
            )
            contents = contents.replace(
                """* substance.strength.referenceStrength[=].strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"
* substance.strength.referenceStrength[=].strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"\n""",
                "",
            )

            contents = contents.replace(
                """* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"\n""",
                "",
            )

            if "substance.strength" not in contents:
                contents += """\n* substance.strength.concentrationRatio.numerator = 0 http://spor.ema.europa.eu/v1/lists/100000110633#100000110655 "milligram(s)"\n
                //DUMMY\n
* substance.strength.concentrationRatio.denominator = 0 http://spor.ema.europa.eu/v1/lists/100000110633#100000110756 "unit(s)" """

            contents = contents.replace(
                '* substance.strength.concentrationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"',
                "",
            )
            contents = contents.replace(
                '* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"',
                "",
            )
            contents = contents.replace(
                '* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000165006 "quantity sufficient"',
                "",
            )
            contents = contents.replace(
                '* substance.strength.concentrationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000052 "less than or equal to"',
                "",
            )

            contents = contents.replace(
                '* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator""',
                "",
            )
            contents = contents.replace(
                '* substance.strength.referenceStrength.strengthRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000049 "equal to"',
                "",
            )

            contents = contents.replace(
                '* substance.strength.presentationRatio.numerator.comparator.extension.valueCoding = $100000000008#100000000051 "more than"',
                "",
            )

            contents = contents.replace(
                '* substance.strength.presentationRatio.numerator.comparator.extension.url = "http://ema.europa.eu/fhir/extension/comparator"',
                "",
            )

            if (
                "* substance.strength.concentrationRatio.numerator " in contents
                and "* substance.strength.concentrationRatio.denominator"
                not in contents
            ):
                contents += '\n* substance.strength.concentrationRatio[=].denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#200000025238 "dose"'

            if (
                "* substance.strength.referenceStrength.strengthRatio.numerator "
                in contents
                and "* substance.strength.referenceStrength.strengthRatio.denominator"
                not in contents
            ):
                contents += '\n* substance.strength.referenceStrength.strengthRatio[=].denominator = 1 http://spor.ema.europa.eu/v1/lists/100000110633#200000025238 "dose"'

            if (
                '* extension.url = "http://ema.europa.eu/fhir/extension/subject"'
                in contents
            ):
                contents = contents.replace(
                    '* extension.url = "http://ema.europa.eu/fhir/extension/subject"',
                    "",
                )
                # print(contents)
                ref_value = re.search(r"\* extension.valueReference = (.+)", contents)
                if ref_value:
                    ref = ref_value.group(1)
                    contents += "\n* for[+] = " + ref
                # contents = contents.replace("* extension.valueReference", "* for[+]")

                contents = re.sub(r"\* extension.valueReference = (.+)", "", contents)

            contents = re.sub(
                r"Reference\(AdministrableProductDefinition\/(.+)\)",
                r"Reference(\1)",
                contents,
            )

            contents = re.sub(
                r"Reference\(AdministrableProductDefinition(.+)\)",
                r"Reference(\1)",
                contents,
            )
            contents = re.sub(
                r"Reference\(MedicinalProductDefinition\/(.+)\)",
                r"Reference(\1)",
                contents,
            )
        ####### MANUFACTURED ITEM DEFINITION ############################################################################################################

        if "InstanceOf: ManufacturedItemDefinition" in contents:
            #   print("yes")
            contents = contents.replace(
                "InstanceOf: ManufacturedItemDefinition",
                "InstanceOf: PPLManufacturedItemDefinition",
            )

            if "unitOfPresentation" not in contents:
                contents += '\n//DUMMY\n* unitOfPresentation = $200000000014#200000002152 "Tablet"'

            contents = contents.replace(
                """* unitOfPresentation.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* unitOfPresentation.coding.extension.valueInteger = 1\n""",
                "",
            )

            contents = contents.replace(
                """* manufacturedDoseForm.coding.extension.url = "http://ema.europa.eu/fhir/extension/termVersion"
* manufacturedDoseForm.coding.extension.valueInteger = 1\n""",
                "",
            )
            contents = contents.replace(
                '* extension.url = "http://ema.europa.eu/fhir/extension/subject"', ""
            )
            contents = re.sub(
                r"\* extension.valueReference = Reference\(.+\)", "", contents
            )

        ####### PACKAGED PRODUCT DEFINITION ####################################

        if "InstanceOf: PackagedProductDefinition" in contents:
            #   print("yes")
            contents = contents.replace(
                "InstanceOf: PackagedProductDefinition",
                "InstanceOf: PPLPackagedProductDefinition",
            )
            contents = contents.replace(
                "package.package",
                "packaging.packaging",
            )
            contents = contents.replace(
                "package.",
                "packaging.",
            )

            if (
                'extension.url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"'
                in contents
            ):
                if "extension.valueQuantity" in contents:
                    contents = contents.replace(
                        "extension.valueQuantity", "containedItemQuantity"
                    )
            if (
                'extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity'
                in contents
            ):
                if "extension.valueQuantity" in contents:
                    contents = contents.replace(
                        "extension.valueQuantity", "containedItemQuantity"
                    )
            if (
                'extension[+].url = "http://ema.europa.eu/fhir/extension/containedItemQuantity'
                in contents
            ):
                if "extension[=].valueQuantity" in contents:
                    contents = contents.replace(
                        "extension[=].valueQuantity", "containedItemQuantity"
                    )
            contents = contents.replace(
                "http://hl7.org/fhir/ValueSet/packaging-type",
                "https://spor.ema.europa.eu/v1/lists/100000073346",
            )

            contents = contents.replace(
                '* packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346/terms/100000073498"',
                '* packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"',
            )
            contents = contents.replace(
                '* marketingStatus.status.coding[0] = xx#xx "xx"',
                '//DUMMY\n* marketingStatus.status.coding[0] = $100000072052#100000072083 "Marketed"',
            )

            contents = contents.replace(
                '* packaging.packaging.type.coding[=].code = "?"',
                "* packaging.packaging.type.coding[=].code = #?",
            )

            contents = contents.replace(
                """* extension[+].url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"
* extension[=].valueQuantity = 6 http://spor.ema.europa.eu/v1/lists/200000000014#200000002137 "Pessary"
* extension[+].url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"
* extension[=].valueQuantity = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002156 "Tube"\n""",
                """* containedItemQuantity = 1 http://spor.ema.europa.eu/v1/lists/200000000014#200000002156 "Tube"\n""",
            )
            contents = contents.replace(
                '* extension.url = "http://hl7.org/fhir/5.0/StructureDefinition/extension-PackagedProductDefinition.containedItemQuantity"',
                "",
            )
            contents = contents.replace(
                '* extension.url = "http://ema.europa.eu/fhir/extension/containedItemQuantity"',
                "",
            )
            contents = contents.replace(
                """* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072288 "Swedish"\n""",
                "",
            )
            contents = contents.replace(
                """* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072172 "Estonian"\n""",
                "",
            )
            contents = contents.replace(
                """* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072251#100000072251 "Portuguese"\n""",
                "",
            )
            contents = contents.replace(
                """* description.extension.url = "http://ema.europa.eu/fhir/extension/language"
* description.extension.valueCoding = $100000072057#100000072178 "German"\n""",
                "",
            )
            if "* description" not in contents:
                contents += '\n//DUMMY\n* description = "dummy"'

            contents = re.sub(
                r'packaging.containedItem.item.reference.reference = "ManufacturedItemDefinition/(.+)"',
                r"packaging.containedItem.item.reference = Reference(\1)",
                contents,
            )
            ###temporarily remove until further notice
            contents = re.sub(
                r"^\* packaging\.shelfLifeStorage.*\n?",
                "",
                contents,
                flags=re.MULTILINE,
            )

            if "* packaging" not in contents:
                contents += """\n//DUMMY\n* packaging.type.coding.system = "https://spor.ema.europa.eu/v1/lists/100000073346"
* packaging.type.coding.code = #100000073498
* packaging.type.coding.display = "Box"
* packaging.quantity = 1"""
        ####### RegulatedAuthorization ########################################################################

        if "InstanceOf: RegulatedAuthorization" in contents:
            #   print("yes")
            # print(contents)
            contents = contents.replace(
                "InstanceOf: RegulatedAuthorization",
                "InstanceOf: PPLRegulatedAuthorization",
            )

            contents = contents.replace(
                '* identifier.system = "http://ema.europa.eu/fhir/MarketingAuthorizationNumber',
                '* identifier.system = "http://ema.europa.eu/fhir/marketingAuthorizationNumber',
            )

            if "* identifier" not in contents:
                contents += '\n//DUMMY\n* identifier.value = "dummy"'

            if "* status" not in contents:
                contents += '\n//DUMMY\n* status = $100000072049#200000017708 "Valid - Renewed/Varied"'

            if "* region" not in contents:
                contents += '\n//DUMMY\n* region = $100000000002#100000000388 "Republic of Estonia"'

            contents.replace("$220000000061#220000000061", "$220000000060#220000000061")

            contents = contents.replace(
                '* type = $100000072055#100000072062 "Marketing Authorisation"',
                '* type = $220000000060#220000000061 "Marketing Authorisation"',
            )
            contents = contents.replace(
                '* type = $220000000061#220000000061 "Marketing Authorisation"',
                '* type = $220000000060#220000000061 "Marketing Authorisation"',
            )
            contents = create_org(contents)
        if "InstanceOf: Bundle" in contents:
            contents = contents.replace(
                "* type = #transaction",
                "* type = #collection",
            )
            contents = contents.replace(
                "* entry[=].request.method = #PUT",
                "",
            )
            contents = re.sub(r"\* entry\[=\].request.url = \"(.+)\"", "", contents)
        # print(target_folder + file)
        f = open(target_folder + file, "w")
        f.write(contents)
        f.close()

### clean up not needed files
blacklist_ids = [
    "Fragmin-10000IEml-Solution-SE-IS-MedicinalProductDef-BBDL.fsh",
    "Fragmin-10000IEml-Solution-SE-IS-MedicinalProductDef.fsh",
    "JMJ-Humalog-Mix50-Kwikpen-product-example",
    "JMJ-Monuril-product-example",
    "d37bfa6f-ea90-4645-8be4-e7c649dd64f2",
    "bb8c2306-04c5-42df-94c9-aa6d6e68050b",  # PT
    "7f81d47e-9a74-44b3-8ed7-07990093d878",
]
for file in listdir(target_folder):
    # print(file)
    res = file.split("-")[-1].split(".")[0]
    if file not in [
        "aliases.fsh",
        "codesystems.fsh",
        "valuesets.fsh",
        "missing.fsh",
        "Organization.fsh",
    ]:
        if "-SE-" not in file or file in blacklist_ids:
            remove(target_folder + file)
            print("remove", file)


###aliases
f = open(target_folder + "aliases.fsh", "w")

f.write(
    """Alias: $200000000004~200000000006~200000000007~200000000008 = https://spor.ema.europa.eu/v1/lists/200000000004~200000000006~200000000007~200000000008
Alias: $100000000004 = https://spor.ema.europa.eu/v1/lists/100000000004
Alias: $200000005003 = https://spor.ema.europa.eu/v1/lists/200000005003
Alias: $100000072051 = https://spor.ema.europa.eu/v1/lists/100000072051
Alias: $100000116677 = https://spor.ema.europa.eu/v1/lists/100000116677
Alias: $220000000060 = https://spor.ema.europa.eu/v1/lists/220000000060
Alias: $100000000002 = https://spor.ema.europa.eu/v1/lists/100000000002
Alias: $100000072049 = https://spor.ema.europa.eu/v1/lists/100000072049
Alias: $authorisation-date-type = https://ema.europa.eu/fhir/code-systems/authorisation-date-type
Alias: $100000072057 = https://spor.ema.europa.eu/v1/lists/100000072057
Alias: $100000072052 = https://spor.ema.europa.eu/v1/lists/100000072052
Alias: $200000000004 = https://spor.ema.europa.eu/v1/lists/200000000004
Alias: $200000000014 = https://spor.ema.europa.eu/v1/lists/200000000014

Alias: $100000093533 = https://spor.ema.europa.eu/v1/lists/100000093533

Alias: $authorisationDateType = https://ema.europa.eu/fhir/authorisationDateType


Alias: $100000154442 = https://spor.ema.europa.eu/v1/lists/100000154442
Alias: $100000160962 = https://spor.ema.europa.eu/v1/lists/100000160962
Alias: $100000155526 = https://spor.ema.europa.eu/v1/lists/100000155526
Alias: $100000072050 = https://spor.ema.europa.eu/v1/lists/100000072050 // Ingredient Role
Alias: $SubstanceDefinition = https://spor.azure-api.net/sms/api/v2/SubstanceDefinition
Alias: $100000000008 = https://spor.ema.europa.eu/v1/lists/100000000008
Alias: $atc = https://www.whocc.no/atc
Alias: $200000003186 = https://spor.ema.europa.eu/v1/lists/200000003186
Alias: $publication-status = https://hl7.org/fhir/publication-status
Alias: $additionalMonitoringIndicator = https://ema.europa.eu/fhir/additionalMonitoringIndicator
Alias: $200000000010 = https://spor.ema.europa.eu/v1/lists/200000000010
Alias: $country = https://hl7.org/fhir/ValueSet/country
Alias: $200000000008 = https://spor.ema.europa.eu/v1/lists/200000000008
Alias: $paediatricUseIndicator = https://ema.europa.eu/fhir/paediatricUseIndicator
Alias: $200000000324 = https://spor.ema.europa.eu/v1/lists/200000000324
Alias: $100000116045 = https://spor.ema.europa.eu/v1/lists/100000116045
Alias: $100000154441 = https://spor.ema.europa.eu/v1/lists/100000154441
Alias: $100000160406 = https://spor.ema.europa.eu/v1/lists/100000160406
Alias: $200000004983 = https://spor.ema.europa.eu/v1/lists/200000004983
Alias: $100000155688 = https://spor.ema.europa.eu/v1/lists/100000155688
Alias: $riskOfSupplyShortage = https://ema.europa.eu/fhir/riskOfSupplyShortage
Alias: $200000000007 = https://spor.ema.europa.eu/v1/lists/200000000007
Alias: $100000073345 = https://spor.ema.europa.eu/v1/lists/100000073345
Alias: $200000003554 = https://spor.ema.europa.eu/v1/lists/200000003554
Alias: $medicinal-product-type = https://hl7.org/fhir/medicinal-product-type
Alias: $200000025915 = https://spor.ema.europa.eu/v1/lists/200000025915
Alias: $medicinal-product-domain = https://hl7.org/fhir/medicinal-product-domain
Alias: $legal-status-of-supply = https://hl7.org/fhir/legal-status-of-supply
Alias: $ = https://www.whocc.no/atc_ddd_index/
Alias: $100000072055 = https://spor.ema.europa.eu/v1/lists/100000072055
Alias: $iso3166-1edition2 = https://terminology.hl7.org/CodeSystem/iso3166-1edition2
Alias: $standardterms = https://standardterms.edqm.eu/

Alias: $200000000006 = https://spor.ema.europa.eu/v1/lists/200000000006
Alias: $200000004946 = https://spor.ema.europa.eu/v1/lists/200000004946
Alias: $100000096162 = https://spor.ema.europa.eu/v1/lists/100000093533/terms/100000096162
Alias: $220000000061 = https://spor.ema.europa.eu/v1/lists/220000000060/terms/220000000061
Alias: $100000072251 = https://spor.ema.europa.eu/v1/lists/100000072057/terms/100000072251
Alias: $100000073665 = https://spor.ema.europa.eu/v1/lists/200000000004/terms/100000073665
Alias: $100000072072 = https://spor.ema.europa.eu/v1/lists/100000072050/terms/100000072072


Alias: $100000073345 = https://spor.ema.europa.eu/v1/lists/100000073345
Alias: $200000002152 = https://spor.ema.europa.eu/v1/lists/200000000014/terms/200000002152
Alias: $100000073619 = https://spor.ema.europa.eu/v1/lists/100000073345/terms/100000073619
Alias: $100000110633 = https://spor.ema.europa.eu/v1/lists/100000110633

"""
)
f.close()
