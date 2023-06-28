{% for index,row in data["data"].iterrows() %}
{% if row["skip"] not in ['y', 'Y', 'x', 'X'] %}

{% for idx in range(0,row["Toimeaine"].count(",")+1) %} 

{% set ns = namespace() %}
{% set ns.ingone = row['Toimeaine'].split(",")[idx] %}
{% set ns.ingtwo = row["Ravimi nimetus"] %}

{% if "," in row['Ravimi tugevus'] %}
{% set ns.parser = "," %}
{% elif "+" in row['Ravimi tugevus'] %}
{% set ns.parser = "+" %}
{% else %}
{% set ns.parser = "," %}
{% endif %}

{% set ns.ingthree= row['Ravimi tugevus'].split(ns.parser)[idx] %}


{% set ns.ingfour= row['Müügiloa hoidja organisatsioon'] %}



{% set ns.ing_name_to_has= ns.ingone ~ " "~ns.ingtwo~" " ~ns.ingthree ~" "~ns.ingfour %}

{% set ns.one = row['Ravimi nimetus'] %}
{% set ns.two = row['Ravimvorm'] %}
{% set ns.three= row['Ravimi tugevus'] %}
{% set ns.name_to_has= ns.one ~ ns.two ~ns.three  %}


{% if row["Ravimis sisalduva toimeaine tugevus"]|string == "nan" %}
{% set ns.num_value =  row["Ravimi tugevus"].split(ns.parser)[idx]| calculate_stregngth(row["referenceWeight"].split(",")[idx])   %}


{% else %}
{% set ns.num_value =  row["Ravimis sisalduva toimeaine tugevus"].split(",")[idx]| get_by_regex("(\d+|\.)")   %}
{% endif %}
{% if "/" in row["Ravimi tugevus"].split(ns.parser)[idx] %}
{% set ns.num_unit = row["Ravimi tugevus"].split(ns.parser)[idx]|splitpart(0,"/")| get_by_regex("[a-z]+")|get_data_dictionary_info(100000110633,"RMS termini id","Termini sümbol") %}
{% set ns.num_unit_desc = row["Ravimi tugevus"].split(ns.parser)[idx]|splitpart(0,"/")| get_by_regex("[a-z]+") %}
{% else %}
{% set ns.num_unit = row["Ravimi tugevus"].split(ns.parser)[idx]| get_by_regex("[a-z]+")|get_data_dictionary_info(100000110633,"RMS termini id","Termini sümbol") %}
{% set ns.num_unit_desc = row["Ravimi tugevus"].split(ns.parser)[idx]| get_by_regex("[a-z]+") %}
{% endif %}

{% set ns.ref_num_value =  row["Referentstoimeaine tugevus"].split(ns.parser)[idx]| get_by_regex("(\d+|\.)")   %}
{% if "/" in row["Referentstoimeaine tugevus"].split(ns.parser)[idx] %}
{% set ns.ref_num_unit = row["Referentstoimeaine tugevus"].split(ns.parser)[idx]|splitpart(0,"/")| get_by_regex("[a-z]+")|get_data_dictionary_info(100000110633,"RMS termini id","Termini sümbol") %}
{% set ns.ref_num_unit_desc = row["Referentstoimeaine tugevus"].split(ns.parser)[idx]|splitpart(0,"/")| get_by_regex("[a-z]+") %}
{% else %}
{% set ns.ref_num_unit = row["Referentstoimeaine tugevus"].split(ns.parser)[idx]|splitpart(0,"/")| get_by_regex("[a-z]+")|get_data_dictionary_info(100000110633,"RMS termini id","Termini sümbol") %}
{% set ns.ref_num_unit_desc = row["Referentstoimeaine tugevus"].split(ns.parser)[idx]| get_by_regex("[a-z]+") %}
{% endif %}

{% set ns.concept_id = row["Toimeaine"].split(",")[idx]|strip_spaces|get_data_dictionary_info("substance","Concept Code","National Description")  %}
{% set ns.concept = row["Toimeaine"].split(",")[idx]|strip_spaces|get_data_dictionary_info("substance","Description (FSN)","National Description")  %}


{% set ns.ref_concept_id = row["Referentstoimeaine"].split(",")[idx]|strip_spaces|get_data_dictionary_info("substance","Concept Code","National Description") %} 
{% set ns.ref_concept = row["Referentstoimeaine"].split(",")[idx]|strip_spaces|get_data_dictionary_info("substance","Description (FSN)","National Description") %}



Instance: ingredient-{{ ns.ing_name_to_has| create_hash_id}}
InstanceOf: PPLIngredient
Title: "{{ ns.ing_name_to_has}}"
Description: "ingredient {{row["Toimeaine"].split(",")[idx]}} with strength {{ row["Ravimi tugevus"].split(ns.parser)[idx]}} for {{ row["Ravimi nimetus"]}}"
Usage: #example

* role = $100000072050#100000072072 "active"
* status = #active
* substance.code.concept = $sms#{{ ns.concept_id }} "{{ns.concept}}"

{{ "// ERROR[4] - strengths and principles are wrong for INDEX:{}".format(index+1) if row["Toimeaine"].split(",")|length != row["Ravimi tugevus"].split("+")|length }}
//full: {{row["Ravimi tugevus"].split(ns.parser)[idx]}}

* substance.strength.presentationRatio.numerator = {{ns.num_value}}  $100000110633#{{ ns.num_unit}}  "{{ ns.num_unit_desc }}"
* substance.strength.presentationRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"

{{"// ERROR[5] - reference strengths and principles are wrong for INDEX:{}".format(index+1) if row["Referentstoimeaine"].split(ns.parser)|length != row["Referentstoimeaine tugevus"].split(ns.parser)|length }}
//full: {{row["Referentstoimeaine tugevus"].split(ns.parser)[idx]}}
* substance.strength.referenceStrength.strengthRatio.numerator  = {{ ns.ref_num_value  }} $100000110633#{{ ns.ref_num_unit}} "{{ ns.ref_num_unit_desc }}"
* substance.strength.referenceStrength.strengthRatio.denominator = 1  $200000000014#100000110662  "millilitre(s)"

* substance.strength.referenceStrength.substance.concept = $sms#{{ ns.ref_concept_id }} "{{ns.ref_concept}}"

// Reference to products item
//{{ ns.name_to_has}}
* for[0] = Reference(mp-{{row["Müügiloa number"]|trim| create_hash_id}})
* for[+] = Reference(ap-{{row["Müügiloa number"]|trim| create_hash_id}})
* for[+] = Reference(mid-{{row["Müügiloa number"]|trim|create_hash_id}})


{%- endfor %}

{%- endif %}
{%- endfor %}