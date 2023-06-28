
 








 

Instance: ingredient-cbe80905b70d091f3f3dab2bc7a38360
InstanceOf: PPLIngredient
Title: "kaaliumklavulanaat AUGMENTIN FRUIT 11.4mg First Pharma OÜ"
Description: "ingredient kaaliumklavulanaat with strength 11.4mg for AUGMENTIN FRUIT"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 11.4mg
* substance.strength.presentationRatio.numerator = 13.58  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:1
//full: 11.4mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 11.4 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//AUGMENTIN FRUITSuukaudse suspensiooni pulber11.4mg+80mg/ml
* for[0] = Reference(mp-aef16e777350a038f9907b2f30d0cd3e)
* for[+] = Reference(ap-aef16e777350a038f9907b2f30d0cd3e)
* for[+] = Reference(mid-aef16e777350a038f9907b2f30d0cd3e) 








 

Instance: ingredient-e7bce9e9092748397d747f574508f791
InstanceOf: PPLIngredient
Title: " amoksitsilliintrihüdraat AUGMENTIN FRUIT 80mg/ml First Pharma OÜ"
Description: "ingredient  amoksitsilliintrihüdraat with strength 80mg/ml for AUGMENTIN FRUIT"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 80mg/ml
* substance.strength.presentationRatio.numerator = 91.84  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:1
//full: 80mg/ml
* substance.strength.referenceStrength.strengthRatio.numerator  = 80 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//AUGMENTIN FRUITSuukaudse suspensiooni pulber11.4mg+80mg/ml
* for[0] = Reference(mp-aef16e777350a038f9907b2f30d0cd3e)
* for[+] = Reference(ap-aef16e777350a038f9907b2f30d0cd3e)
* for[+] = Reference(mid-aef16e777350a038f9907b2f30d0cd3e)
 








 

Instance: ingredient-ad91ffac4e5598f73ba7cdabd8ae3f7f
InstanceOf: PPLIngredient
Title: "amoksitsilliintrihüdraat AUGMENTIN FRUIT 80mg Ideal Trade Links UAB"
Description: "ingredient amoksitsilliintrihüdraat with strength 80mg for AUGMENTIN FRUIT"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 80mg
* substance.strength.presentationRatio.numerator = 91.84  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:2
//full: 11.4mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 11.4 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//AUGMENTIN FRUITSuukaudse suspensiooni pulber80mg+11.4mg/ml
* for[0] = Reference(mp-63f5adb8aee673b5cbc8f5e123ede45b)
* for[+] = Reference(ap-63f5adb8aee673b5cbc8f5e123ede45b)
* for[+] = Reference(mid-63f5adb8aee673b5cbc8f5e123ede45b) 








 

Instance: ingredient-9421745f21aa637c9b862556fc89e0e9
InstanceOf: PPLIngredient
Title: " kaaliumklavulanaat AUGMENTIN FRUIT 11.4mg/ml Ideal Trade Links UAB"
Description: "ingredient  kaaliumklavulanaat with strength 11.4mg/ml for AUGMENTIN FRUIT"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 11.4mg/ml
* substance.strength.presentationRatio.numerator = 13.58  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:2
//full: 80mg/ml
* substance.strength.referenceStrength.strengthRatio.numerator  = 80 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//AUGMENTIN FRUITSuukaudse suspensiooni pulber80mg+11.4mg/ml
* for[0] = Reference(mp-63f5adb8aee673b5cbc8f5e123ede45b)
* for[+] = Reference(ap-63f5adb8aee673b5cbc8f5e123ede45b)
* for[+] = Reference(mid-63f5adb8aee673b5cbc8f5e123ede45b)
 








 

Instance: ingredient-f6a54149d0b7c6ce1947907c4d9d8f24
InstanceOf: PPLIngredient
Title: "amoksitsilliintrihüdraat AUGMENTIN 125mg First Pharma OÜ"
Description: "ingredient amoksitsilliintrihüdraat with strength 125mg for AUGMENTIN"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 125mg
* substance.strength.presentationRatio.numerator = 143.51  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:3
//full: 125mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 125 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//AUGMENTINÕhukese polümeerikattega tablett125mg+500mg
* for[0] = Reference(mp-ae0f709e7d41e835a22b84e847a7aa95)
* for[+] = Reference(ap-ae0f709e7d41e835a22b84e847a7aa95)
* for[+] = Reference(mid-ae0f709e7d41e835a22b84e847a7aa95) 








 

Instance: ingredient-7a30d8e289fd63bf21726d0b2b3ad2a6
InstanceOf: PPLIngredient
Title: " kaaliumklavulanaat AUGMENTIN 500mg First Pharma OÜ"
Description: "ingredient  kaaliumklavulanaat with strength 500mg for AUGMENTIN"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 500mg
* substance.strength.presentationRatio.numerator = 595.63  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:3
//full: 500mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 500 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//AUGMENTINÕhukese polümeerikattega tablett125mg+500mg
* for[0] = Reference(mp-ae0f709e7d41e835a22b84e847a7aa95)
* for[+] = Reference(ap-ae0f709e7d41e835a22b84e847a7aa95)
* for[+] = Reference(mid-ae0f709e7d41e835a22b84e847a7aa95)
 








 

Instance: ingredient-91b83954e5f67b9cc73c577387bf4036
InstanceOf: PPLIngredient
Title: "amoksitsilliinnaatrium AMOKSIKLAV 0.2g Sandoz Pharmaceuticals d.d."
Description: "ingredient amoksitsilliinnaatrium with strength 0.2g for AMOKSIKLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000090113 "Amoxicillin sodium"

//full: 0.2g
* substance.strength.presentationRatio.numerator = 0.23  $100000110633#100000110654  "g"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:4
//full: 0.2g
* substance.strength.referenceStrength.strengthRatio.numerator  = 0.2 $100000110633#100000110654 "g"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//AMOKSIKLAVSüste-/infusioonilahuse pulber0.2g+1g
* for[0] = Reference(mp-0c3865762feeeda0cda92ded3764200c)
* for[+] = Reference(ap-0c3865762feeeda0cda92ded3764200c)
* for[+] = Reference(mid-0c3865762feeeda0cda92ded3764200c) 








 

Instance: ingredient-2abb10a4ba0a0c61bff23a248a9657a8
InstanceOf: PPLIngredient
Title: " kaaliumklavulanaat AMOKSIKLAV 1g Sandoz Pharmaceuticals d.d."
Description: "ingredient  kaaliumklavulanaat with strength 1g for AMOKSIKLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 1g
* substance.strength.presentationRatio.numerator = 1.19  $100000110633#100000110654  "g"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:4
//full: 1g
* substance.strength.referenceStrength.strengthRatio.numerator  = 1 $100000110633#100000110654 "g"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//AMOKSIKLAVSüste-/infusioonilahuse pulber0.2g+1g
* for[0] = Reference(mp-0c3865762feeeda0cda92ded3764200c)
* for[+] = Reference(ap-0c3865762feeeda0cda92ded3764200c)
* for[+] = Reference(mid-0c3865762feeeda0cda92ded3764200c)
 








 

Instance: ingredient-ea97a54b130fc7904eb651fa2b0e370c
InstanceOf: PPLIngredient
Title: "amoksitsilliintrihüdraat AUGMENTIN 125mg GlaxoSmithKline (Ireland) Limited"
Description: "ingredient amoksitsilliintrihüdraat with strength 125mg for AUGMENTIN"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 125mg
* substance.strength.presentationRatio.numerator = 143.51  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:5
//full: 125mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 125 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//AUGMENTINÕhukese polümeerikattega tablett125mg+875mg
* for[0] = Reference(mp-cc91bd35cacafbd07310b5140b983ca2)
* for[+] = Reference(ap-cc91bd35cacafbd07310b5140b983ca2)
* for[+] = Reference(mid-cc91bd35cacafbd07310b5140b983ca2) 








 

Instance: ingredient-af51c1006fbcc4eb0e7db633aa0cb617
InstanceOf: PPLIngredient
Title: " kaaliumklavulanaat AUGMENTIN 875mg GlaxoSmithKline (Ireland) Limited"
Description: "ingredient  kaaliumklavulanaat with strength 875mg for AUGMENTIN"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 875mg
* substance.strength.presentationRatio.numerator = 1042.35  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:5
//full: 875mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 875 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//AUGMENTINÕhukese polümeerikattega tablett125mg+875mg
* for[0] = Reference(mp-cc91bd35cacafbd07310b5140b983ca2)
* for[+] = Reference(ap-cc91bd35cacafbd07310b5140b983ca2)
* for[+] = Reference(mid-cc91bd35cacafbd07310b5140b983ca2)
 








 

Instance: ingredient-1a1b41f2e7e25b608d1f6d5fc4a40b3a
InstanceOf: PPLIngredient
Title: "kaaliumklavulanaat AMOKSIKLAV 875mg Sandoz Pharmaceuticals d.d."
Description: "ingredient kaaliumklavulanaat with strength 875mg for AMOKSIKLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 875mg
* substance.strength.presentationRatio.numerator = 1042.35  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:6
//full: 875mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 875 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//AMOKSIKLAVÕhukese polümeerikattega tablett875mg+125mg
* for[0] = Reference(mp-6c440b58a82f2b326e5d2212bc4c28f3)
* for[+] = Reference(ap-6c440b58a82f2b326e5d2212bc4c28f3)
* for[+] = Reference(mid-6c440b58a82f2b326e5d2212bc4c28f3) 








 

Instance: ingredient-138785cee6ebc84d74b4faf5ec34f9fe
InstanceOf: PPLIngredient
Title: " amoksitsilliintrihüdraat AMOKSIKLAV 125mg Sandoz Pharmaceuticals d.d."
Description: "ingredient  amoksitsilliintrihüdraat with strength 125mg for AMOKSIKLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 125mg
* substance.strength.presentationRatio.numerator = 143.51  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:6
//full: 125mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 125 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//AMOKSIKLAVÕhukese polümeerikattega tablett875mg+125mg
* for[0] = Reference(mp-6c440b58a82f2b326e5d2212bc4c28f3)
* for[+] = Reference(ap-6c440b58a82f2b326e5d2212bc4c28f3)
* for[+] = Reference(mid-6c440b58a82f2b326e5d2212bc4c28f3)
 








 

Instance: ingredient-7be57e791ef42453f7e902db117e0795
InstanceOf: PPLIngredient
Title: "kaaliumklavulanaat AMOKSIKLAV 80mg Sandoz Pharmaceuticals d.d."
Description: "ingredient kaaliumklavulanaat with strength 80mg for AMOKSIKLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 80mg
* substance.strength.presentationRatio.numerator = 95.3  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:7
//full: 80mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 80 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//AMOKSIKLAVSuukaudse suspensiooni pulber80mg+11.4mg/ml
* for[0] = Reference(mp-8395fd1100b827d4553f55467401cec1)
* for[+] = Reference(ap-8395fd1100b827d4553f55467401cec1)
* for[+] = Reference(mid-8395fd1100b827d4553f55467401cec1) 








 

Instance: ingredient-7bb917533e5b16f4a1e7007da5e10a98
InstanceOf: PPLIngredient
Title: " amoksitsilliintrihüdraat AMOKSIKLAV 11.4mg/ml Sandoz Pharmaceuticals d.d."
Description: "ingredient  amoksitsilliintrihüdraat with strength 11.4mg/ml for AMOKSIKLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 11.4mg/ml
* substance.strength.presentationRatio.numerator = 13.09  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:7
//full: 11.4mg/ml
* substance.strength.referenceStrength.strengthRatio.numerator  = 11.4 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//AMOKSIKLAVSuukaudse suspensiooni pulber80mg+11.4mg/ml
* for[0] = Reference(mp-8395fd1100b827d4553f55467401cec1)
* for[+] = Reference(ap-8395fd1100b827d4553f55467401cec1)
* for[+] = Reference(mid-8395fd1100b827d4553f55467401cec1)
 








 

Instance: ingredient-83338562124bdf119c7173a3d0ca427f
InstanceOf: PPLIngredient
Title: "amoksitsilliintrihüdraat AMOKSIKLAV 500mg Sandoz Pharmaceuticals d.d."
Description: "ingredient amoksitsilliintrihüdraat with strength 500mg for AMOKSIKLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 500mg
* substance.strength.presentationRatio.numerator = 574.03  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:8
//full: 500mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 500 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//AMOKSIKLAVÕhukese polümeerikattega tablett500mg+125mg
* for[0] = Reference(mp-a183d02763ad3ec233f3868e33c3a7c1)
* for[+] = Reference(ap-a183d02763ad3ec233f3868e33c3a7c1)
* for[+] = Reference(mid-a183d02763ad3ec233f3868e33c3a7c1) 








 

Instance: ingredient-dadc25d7c0e562b9b27f1ca1e5d6a6d3
InstanceOf: PPLIngredient
Title: " kaaliumklavulanaat AMOKSIKLAV 125mg Sandoz Pharmaceuticals d.d."
Description: "ingredient  kaaliumklavulanaat with strength 125mg for AMOKSIKLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 125mg
* substance.strength.presentationRatio.numerator = 148.91  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:8
//full: 125mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 125 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//AMOKSIKLAVÕhukese polümeerikattega tablett500mg+125mg
* for[0] = Reference(mp-a183d02763ad3ec233f3868e33c3a7c1)
* for[+] = Reference(ap-a183d02763ad3ec233f3868e33c3a7c1)
* for[+] = Reference(mid-a183d02763ad3ec233f3868e33c3a7c1)
 








 

Instance: ingredient-f712b96b22ede7d530d86b3bdc7a7509
InstanceOf: PPLIngredient
Title: "kaaliumklavulanaat AMOKSIKLAV 125mg Sandoz Pharmaceuticals d.d."
Description: "ingredient kaaliumklavulanaat with strength 125mg for AMOKSIKLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 125mg
* substance.strength.presentationRatio.numerator = 148.91  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:10
//full: 125mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 125 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//AMOKSIKLAVDispergeeruv tablett125mg+875mg
* for[0] = Reference(mp-3db2464750d10c42a5def393db852f42)
* for[+] = Reference(ap-3db2464750d10c42a5def393db852f42)
* for[+] = Reference(mid-3db2464750d10c42a5def393db852f42) 








 

Instance: ingredient-71381ba2c54b3edff70e0f7d6b4f5f2d
InstanceOf: PPLIngredient
Title: " amoksitsilliintrihüdraat AMOKSIKLAV 875mg Sandoz Pharmaceuticals d.d."
Description: "ingredient  amoksitsilliintrihüdraat with strength 875mg for AMOKSIKLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 875mg
* substance.strength.presentationRatio.numerator = 1004.55  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:10
//full: 875mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 875 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//AMOKSIKLAVDispergeeruv tablett125mg+875mg
* for[0] = Reference(mp-3db2464750d10c42a5def393db852f42)
* for[+] = Reference(ap-3db2464750d10c42a5def393db852f42)
* for[+] = Reference(mid-3db2464750d10c42a5def393db852f42)
 








 

Instance: ingredient-9d559fe2b989e40be7dcb8bccc8a1f2f
InstanceOf: PPLIngredient
Title: "kaaliumklavulanaat MEDOCLAV 1000mg Medochemie Limited"
Description: "ingredient kaaliumklavulanaat with strength 1000mg for MEDOCLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 1000mg
* substance.strength.presentationRatio.numerator = 1191.25  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:11
//full: 1000mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 1000 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//MEDOCLAVSüste-/infusioonilahuse pulber1000mg+200mg
* for[0] = Reference(mp-fe9d30ca141748f551f66c0b61345011)
* for[+] = Reference(ap-fe9d30ca141748f551f66c0b61345011)
* for[+] = Reference(mid-fe9d30ca141748f551f66c0b61345011) 








 

Instance: ingredient-8e1d8361e14686fbd447d490eecf2d96
InstanceOf: PPLIngredient
Title: " amoksitsilliinnaatrium  MEDOCLAV 200mg Medochemie Limited"
Description: "ingredient  amoksitsilliinnaatrium  with strength 200mg for MEDOCLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000090113 "Amoxicillin sodium"

//full: 200mg
* substance.strength.presentationRatio.numerator = 229.61  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:11
//full: 200mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 200 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//MEDOCLAVSüste-/infusioonilahuse pulber1000mg+200mg
* for[0] = Reference(mp-fe9d30ca141748f551f66c0b61345011)
* for[+] = Reference(ap-fe9d30ca141748f551f66c0b61345011)
* for[+] = Reference(mid-fe9d30ca141748f551f66c0b61345011)
 








 

Instance: ingredient-fa7274d597954958bae319fc27a0a68d
InstanceOf: PPLIngredient
Title: "amoksitsilliintrihüdraat AMOXICILLIN/CLAVULANIC ACID ACTAVIS 125mg Teva B.V."
Description: "ingredient amoksitsilliintrihüdraat with strength 125mg for AMOXICILLIN/CLAVULANIC ACID ACTAVIS"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 125mg
* substance.strength.presentationRatio.numerator = 143.51  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:12
//full: 125mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 125 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//AMOXICILLIN/CLAVULANIC ACID ACTAVISÕhukese polümeerikattega tablett125mg+875mg
* for[0] = Reference(mp-3274dad3c464912ca6b376ec36383c72)
* for[+] = Reference(ap-3274dad3c464912ca6b376ec36383c72)
* for[+] = Reference(mid-3274dad3c464912ca6b376ec36383c72) 








 

Instance: ingredient-ce07af7747300597433e90beb84a51d7
InstanceOf: PPLIngredient
Title: " kaaliumklavulanaat AMOXICILLIN/CLAVULANIC ACID ACTAVIS 875mg Teva B.V."
Description: "ingredient  kaaliumklavulanaat with strength 875mg for AMOXICILLIN/CLAVULANIC ACID ACTAVIS"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 875mg
* substance.strength.presentationRatio.numerator = 1042.35  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:12
//full: 875mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 875 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//AMOXICILLIN/CLAVULANIC ACID ACTAVISÕhukese polümeerikattega tablett125mg+875mg
* for[0] = Reference(mp-3274dad3c464912ca6b376ec36383c72)
* for[+] = Reference(ap-3274dad3c464912ca6b376ec36383c72)
* for[+] = Reference(mid-3274dad3c464912ca6b376ec36383c72)
 








 

Instance: ingredient-62fb978dbfa6654192d79e93a38bb47c
InstanceOf: PPLIngredient
Title: "amoksitsilliintrihüdraat BETAKLAV 125mg KRKA, d.d., Novo mesto"
Description: "ingredient amoksitsilliintrihüdraat with strength 125mg for BETAKLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 125mg
* substance.strength.presentationRatio.numerator = 143.51  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:13
//full: 125mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 125 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//BETAKLAVÕhukese polümeerikattega tablett125mg+875mg
* for[0] = Reference(mp-fb141b1fc2fa85a52c41173030cd9869)
* for[+] = Reference(ap-fb141b1fc2fa85a52c41173030cd9869)
* for[+] = Reference(mid-fb141b1fc2fa85a52c41173030cd9869) 








 

Instance: ingredient-b3c398346431ddb7279edd4093ad5d5f
InstanceOf: PPLIngredient
Title: " kaaliumklavulanaat BETAKLAV 875mg KRKA, d.d., Novo mesto"
Description: "ingredient  kaaliumklavulanaat with strength 875mg for BETAKLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 875mg
* substance.strength.presentationRatio.numerator = 1042.35  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:13
//full: 875mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 875 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//BETAKLAVÕhukese polümeerikattega tablett125mg+875mg
* for[0] = Reference(mp-fb141b1fc2fa85a52c41173030cd9869)
* for[+] = Reference(ap-fb141b1fc2fa85a52c41173030cd9869)
* for[+] = Reference(mid-fb141b1fc2fa85a52c41173030cd9869)
 








 

Instance: ingredient-7fabaf050270a5d838deeeeae993f66a
InstanceOf: PPLIngredient
Title: "kaaliumklavulanaat AUGMENTIN 125mg First Pharma OÜ"
Description: "ingredient kaaliumklavulanaat with strength 125mg for AUGMENTIN"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 125mg
* substance.strength.presentationRatio.numerator = 148.91  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:14
//full: 125mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 125 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//AUGMENTINÕhukese polümeerikattega tablett125mg+875mg
* for[0] = Reference(mp-ddbfe1991540036d24c62d77a8ff9c0c)
* for[+] = Reference(ap-ddbfe1991540036d24c62d77a8ff9c0c)
* for[+] = Reference(mid-ddbfe1991540036d24c62d77a8ff9c0c) 








 

Instance: ingredient-9dd12aa5e0283c7503dcead56b1a5c04
InstanceOf: PPLIngredient
Title: " amoksitsilliintrihüdraat AUGMENTIN 875mg First Pharma OÜ"
Description: "ingredient  amoksitsilliintrihüdraat with strength 875mg for AUGMENTIN"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 875mg
* substance.strength.presentationRatio.numerator = 1004.55  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:14
//full: 875mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 875 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//AUGMENTINÕhukese polümeerikattega tablett125mg+875mg
* for[0] = Reference(mp-ddbfe1991540036d24c62d77a8ff9c0c)
* for[+] = Reference(ap-ddbfe1991540036d24c62d77a8ff9c0c)
* for[+] = Reference(mid-ddbfe1991540036d24c62d77a8ff9c0c)
 








 

Instance: ingredient-d5e6b8da85fb45701d5839ccddf62115
InstanceOf: PPLIngredient
Title: "amoksitsilliintrihüdraat MEDOCLAV 80mg Medochemie Limited"
Description: "ingredient amoksitsilliintrihüdraat with strength 80mg for MEDOCLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 80mg
* substance.strength.presentationRatio.numerator = 91.84  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:15
//full: 80mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 80 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//MEDOCLAVSuukaudse suspensiooni pulber80mg+11.4mg/ml
* for[0] = Reference(mp-8946929ce94a7eb4ba6090b17bfedf25)
* for[+] = Reference(ap-8946929ce94a7eb4ba6090b17bfedf25)
* for[+] = Reference(mid-8946929ce94a7eb4ba6090b17bfedf25) 








 

Instance: ingredient-6315e7963b8179e16980a3a83d92b4c1
InstanceOf: PPLIngredient
Title: " kaaliumklavulanaat MEDOCLAV 11.4mg/ml Medochemie Limited"
Description: "ingredient  kaaliumklavulanaat with strength 11.4mg/ml for MEDOCLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 11.4mg/ml
* substance.strength.presentationRatio.numerator = 13.58  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:15
//full: 11.4mg/ml
* substance.strength.referenceStrength.strengthRatio.numerator  = 11.4 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//MEDOCLAVSuukaudse suspensiooni pulber80mg+11.4mg/ml
* for[0] = Reference(mp-8946929ce94a7eb4ba6090b17bfedf25)
* for[+] = Reference(ap-8946929ce94a7eb4ba6090b17bfedf25)
* for[+] = Reference(mid-8946929ce94a7eb4ba6090b17bfedf25)
 








 

Instance: ingredient-8ebc12fd344b346a6521fc77736ba6cc
InstanceOf: PPLIngredient
Title: "kaaliumklavulanaat AUGMENTIN FRUIT 11.4mg GlaxoSmithKline Trading Services Limited"
Description: "ingredient kaaliumklavulanaat with strength 11.4mg for AUGMENTIN FRUIT"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 11.4mg
* substance.strength.presentationRatio.numerator = 13.58  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:16
//full: 11.4mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 11.4 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//AUGMENTIN FRUITSuukaudse suspensiooni pulber11.4mg+80mg/ml
* for[0] = Reference(mp-697d34dff506a59ef85855f0b5abfa39)
* for[+] = Reference(ap-697d34dff506a59ef85855f0b5abfa39)
* for[+] = Reference(mid-697d34dff506a59ef85855f0b5abfa39) 








 

Instance: ingredient-d97122104e464817f4d01a957d2c993b
InstanceOf: PPLIngredient
Title: " amoksitsilliintrihüdraat AUGMENTIN FRUIT 80mg/ml GlaxoSmithKline Trading Services Limited"
Description: "ingredient  amoksitsilliintrihüdraat with strength 80mg/ml for AUGMENTIN FRUIT"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 80mg/ml
* substance.strength.presentationRatio.numerator = 91.84  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:16
//full: 80mg/ml
* substance.strength.referenceStrength.strengthRatio.numerator  = 80 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//AUGMENTIN FRUITSuukaudse suspensiooni pulber11.4mg+80mg/ml
* for[0] = Reference(mp-697d34dff506a59ef85855f0b5abfa39)
* for[+] = Reference(ap-697d34dff506a59ef85855f0b5abfa39)
* for[+] = Reference(mid-697d34dff506a59ef85855f0b5abfa39)
 








 

Instance: ingredient-9c12544bd5997f419401f98b385badbc
InstanceOf: PPLIngredient
Title: "amoksitsilliintrihüdraat MEDOCLAV 875mg Medochemie Limited"
Description: "ingredient amoksitsilliintrihüdraat with strength 875mg for MEDOCLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000092629 "Amoxicillin trihydrate"

//full: 875mg
* substance.strength.presentationRatio.numerator = 1004.55  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:17
//full: 875mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 875 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000091596 "Amoxicillin"
// Reference to products item
//MEDOCLAVÕhukese polümeerikattega tablett875mg+125mg
* for[0] = Reference(mp-4da3cdc94188d30935c062b4e8c9353a)
* for[+] = Reference(ap-4da3cdc94188d30935c062b4e8c9353a)
* for[+] = Reference(mid-4da3cdc94188d30935c062b4e8c9353a) 








 

Instance: ingredient-bba780c1c28f88520d9fe2949bb316d5
InstanceOf: PPLIngredient
Title: " kaaliumklavulanaat MEDOCLAV 125mg Medochemie Limited"
Description: "ingredient  kaaliumklavulanaat with strength 125mg for MEDOCLAV"
Usage: #example
* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#100000093061 "Potassium clavulanate"

//full: 125mg
* substance.strength.presentationRatio.numerator = 148.91  $100000110633#100000110655  "mg"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
// ERROR[5] - reference strengths and principles are wrong for INDEX:17
//full: 125mg
* substance.strength.referenceStrength.strengthRatio.numerator  = 125 $100000110633#100000110655 "mg"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"
* substance.strength.referenceStrength.substance.concept = $sms#100000089842 "Clavulanic acid"
// Reference to products item
//MEDOCLAVÕhukese polümeerikattega tablett875mg+125mg
* for[0] = Reference(mp-4da3cdc94188d30935c062b4e8c9353a)
* for[+] = Reference(ap-4da3cdc94188d30935c062b4e8c9353a)
* for[+] = Reference(mid-4da3cdc94188d30935c062b4e8c9353a)