import json
from os.path import exists
from os import listdir, getcwd, mkdir, system, rmdir, removedirs, remove
import subprocess
import shutil


FOLDER = "ufis/ufis-fhir/"

#FOLDER = "pt-PPLCreator/fhir-data/"
# FOLDER = "ufis-swe/ufis-fhir/"

print(getcwd())
# mkdir package
if not exists("package"):
    mkdir("package")
# mkdir example inside
if not exists("package/example"):
    mkdir("package/example")
# cp fsh-generated/*.json example

for path in listdir(FOLDER + "fsh-generated/resources/"):
    # print(path)
    shutil.copy(FOLDER + "fsh-generated/resources/" + path, "package/example")
#
# add package.json

data = {
    "name": "unicom.fhir.pt.examples",
    "version": "0.1.0",
    "tools-version": 3,
    "type": "Examples",
    "date": "20231126080447",
    "license": "CC0-1.0",
    "canonical": "http://unicom-project.github.io/unicom-tools",
    "notForPublication": True,
    "url": "file://C:\\work\\ImplementationGuides\\examples\\output",
    "fhirVersions": ["5.0.0"],
    "dependencies": {
        "hl7.terminology.r5": "5.3.0",
        "hl7.fhir.uv.extensions.r5": "1.0.0",
    },
    "author": "UNICOM",
    "maintainers": [{"name": "UNICOM", "url": "http://unicom-project.eu"}],
    "directories": {"lib": "package", "example": "example"},
}

with open("package/package.json", "w") as outfile:  # save as a json just because
    outfile.write(json.dumps(data, indent=2))

# tar -cvzf ufis.tgz package/
# rm -rf examples

filename = FOLDER.split("/")[0]
result = subprocess.run(
    [
        "tar",
        "-cvzf",
        filename + ".tgz",
        "package/",
    ],
    stdout=subprocess.PIPE,
)

# rmdir("package")
shutil.rmtree("package")
