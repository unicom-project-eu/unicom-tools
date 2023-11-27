from os import listdir
import re

FOLDER = "pt-PPLCreator/fhir-data/input/fsh/pt/"

ORDER_LIST = [
    "Ingredient",
]
start_instance = False
REGEX_PATTERN = "Instance: \w+"
for file in listdir(FOLDER):
    print(file)
    res = file.split(".")[0]
    print(res)
    for item in ORDER_LIST:
        if res == item:
            print(res)
            with open(FOLDER + "/" + file, "r") as f:
                for line in f:
                    if re.search(REGEX_PATTERN, line):
                        print(line)
                        start_instance = True
                    if start_instance and re.search(
                        "\* for\[.+\] = Reference(\S+)", line
                    ):
                        match = re.search(REGEX_PATTERN, line)
                    if match:
                        instance = match.group(1)  # Extract
                        print(line)
