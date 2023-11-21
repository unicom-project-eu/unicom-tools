import re

missing_list = []
# 1. Open the file for reading
file_path = "../validation_output.txt"
with open(file_path, "r") as file:
    # 2. Read the contents of the file
    file_contents = file.read()

    # 3. Define the regular expression pattern
    pattern = r' Does not contain resource type - (.+)"'

    # 4. Find all matches of the pattern in the file contents
    matches = re.findall(pattern, file_contents)

    # 5. Print or store the matched patterns
    for match in matches:
        # print(match)
        m = match.replace("</td></tr></table></div>", "")
        missing_list.append(m)

#    "diagnostics": "HAPI-0505: Invalid resource reference found at path[Ingredient.for] - Does not contain resource type - Klexane100000IEinjektion-SE-PLC-AdminProductDef"

print(list(set(missing_list)))
