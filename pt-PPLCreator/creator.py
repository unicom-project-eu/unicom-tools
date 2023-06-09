from os import listdir, mkdir
from os.path import exists
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import sys
import re
import datetime
import hashlib

# total arguments
n = len(sys.argv)
if n < 3:
    raise Exception(
        "Please provide the path to the input file and the path to the output file"
    )


DATA_FILE = sys.argv[1]
TEMPLATE_FOLDER = sys.argv[2]
OUTPUT_FOLDER = sys.argv[3]


env = Environment(loader=FileSystemLoader(TEMPLATE_FOLDER), trim_blocks=True)

# Custom filter method
def regex_replace(s, find, replace):
    """A non-optimal implementation of a regex filter"""
    return re.sub(find, replace, s)


env.filters["regex_replace"] = regex_replace


def format_datetime(s, format_="%d.%m.%Y"):
    """Date Time format"""
    if s == "nan":
        return ""
    return datetime.datetime.strptime(s, format_).strftime("%Y-%m-%d")


env.filters["format_datetime"] = format_datetime


def hash_id(string):
    hash_object = hashlib.md5(bytes(string, "utf-8"))
    return str(hash_object.hexdigest())


env.filters["create_hash_id"] = hash_id


def get_data_dictionary_info(word, data_dictionary, target, input_col):
    df = dict_data[str(data_dictionary)]
    # print(df)
    # return df[df["RMS nimi eesti keeles"] == "Tablett"]["RMS termini id"].values[0]
    try:
        return df[df[input_col] == word][target].values[0]
    except:
        return None


env.filters["get_data_dictionary_info"] = get_data_dictionary_info


def get_by_regex(string, pattern):
    if len(string) == 0:
        return ""
    # print(string)
    return "".join(re.findall(pattern, string))


env.filters["get_by_regex"] = get_by_regex


def strip_spaces(string):
    return string.strip()


env.filters["strip_spaces"] = strip_spaces


def get_data_from_sheet(
    input_value,
    data,
    sheet,
    target,
    input_col,
):
    df = data[sheet]
    # print(df)
    #  if sheet == "ATC_EXTRA":
    #     print(sheet, input_value, target, input_col)
    # return df[df["RMS nimi eesti keeles"] == "Tablett"]["RMS termini id"].values[0]
    try:
        return df[df[input_col] == input_value][target].values[0]
    except:
        return None


env.filters["get_data_from_sheet"] = get_data_from_sheet


# Custom filter method
def validate_data(word, data):
    """validate data from another issue"""
    # df = pd.read_csv(DATA_FILE, encoding="utf-8", sep=";", skiprows=[1])
    # print(word)
    # print(len(df[df["Müügiloa number"] == word]))
    if len(data[data["MED ID"] == word]) > 0:
        return True
    else:
        return False


env.filters["validate_data"] = validate_data


excel_data = {}


def create_from_template(DATA_FILE, TEMPLATE_FOLDER, OUTPUT_FOLDER):
    elements = [
        "Titular-Medicine",
        "ManufacturedItem",
        "Package",
        "Pharmaceutical Product",
        "Ingredient",
        "Pharm Form | U. of Presenta.",
        "Substances",
        "ATC",
        "Routes of Adm.",
        "Measurement Units",
        "Recipient",
        "Extra",
        "ATC_EXTRA",
        "SPOR_EN",
    ]

    # create temp_folder:
    print(DATA_FILE, TEMPLATE_FOLDER, OUTPUT_FOLDER)

    if TEMPLATE_FOLDER[-1] != "/":
        TEMPLATE_FOLDER += "/"
    if OUTPUT_FOLDER[-1] != "/":
        OUTPUT_FOLDER += "/"

    # temp_folder = getcwd() + "/temp/"

    major_name = "pt"
    real_output_folder = OUTPUT_FOLDER + "pt/"
    print(real_output_folder)
    if not exists(real_output_folder):
        mkdir(real_output_folder)
    for sheet in elements:
        if sheet == "Package":
            excel_data[sheet] = pd.DataFrame(
                pd.read_excel(DATA_FILE, sheet_name=sheet, skiprows=1)
            )

        else:
            excel_data[sheet] = pd.DataFrame(pd.read_excel(DATA_FILE, sheet_name=sheet))

    data_dict = {"MajorName": major_name}  # if needed
    data = {"dictionary": data_dict, "turn": "1"}

    for file in listdir(TEMPLATE_FOLDER):
        print(file)
        t = env.get_template(file)
        #  print(file)
        # iso8859_13
        print(DATA_FILE)

        #  print(df.columns)

        data["data"] = excel_data
        t.stream(data=data).dump(real_output_folder + file)


def validate_data(DATA_FILE, OUTPUT_FOLDER):

    if OUTPUT_FOLDER[-1] != "/":
        OUTPUT_FOLDER += "/"

    major_name = DATA_FILE.lower().split("/")[-1].split(".")[0]

    real_output_folder = OUTPUT_FOLDER + "pt/"
    # writing to file
    erros = {}
    description = []

    for path in listdir(real_output_folder):
        print(path)
        file = open(real_output_folder + "/" + path, "r")

        Lines = file.readlines()
        error_count = 0
        count = 0
        final_count = {}
        ids_to_skip = {}
        # Strips the newline character
        for line in Lines:
            count += 1
            if "// ERROR" in line:
                # print(line)
                error_nr = re.search("ERROR\[\d{1,2}\]", line)
                id_ = re.search("INDEX:(\d{1,7})", line)
                # print(id_[0])
                message = re.findall("- (.+) INDEX:", line)
                # print(message[0])
                description.append(str(message[0]) + " " + str(id_[0]))

                #   print(id_[0], message)
                # print(error_nr[0])
                if error_nr[0] in final_count.keys():
                    final_count[error_nr[0]] += 1
                else:
                    final_count[error_nr[0]] = 1
                if id_[0] not in ids_to_skip.keys():
                    ids_to_skip[id_[0]] = message[0]
                else:
                    ids_to_skip[id_[0]] += " ||| " + message[0]

                    # print("{} @{}".format( line.strip(),count))
                error_count += 1
        erros[path] = error_count
    # print(erros)

    # print(description)
    # print(messages)
    f = open("validation_output.txt", "w")
    for k, v in erros.items():
        f.write(k + ":" + str(v))
        f.write("\n")
    f.write("\n")
    for el in description:
        f.write(el)
        f.write("\n")

    f.close()


# remove duplicates


def remove_duplicate(DATA_FILE, OUTPUT_FOLDER):
    if OUTPUT_FOLDER[-1] != "/":
        OUTPUT_FOLDER += "/"

    major_name = "pt"
    real_output_folder = OUTPUT_FOLDER + "pt/"

    # writing to file

    for path in listdir(real_output_folder):
        print(path)
        file = open(real_output_folder + path, "r")
        # with open(file) as f:
        lines = file.readlines()
        unique_df = []
        clean_data = []
        to_delete = False
        for line in lines:

            if line.startswith("Instance: "):
                hash_ = line.replace("Instance: ", "").strip()
                if hash_ not in unique_df:
                    unique_df.append(hash_)
                    to_delete = False
                    clean_data.append(line)

                else:
                    # delete
                    to_delete = True
            else:
                if not to_delete:
                    clean_data.append(line)
        #  print(unique_df)
        with open(file=real_output_folder + path, mode="w") as f:
            f.writelines("".join(clean_data))


def remove_double_lines(DATA_FILE, OUTPUT_FOLDER):
    if OUTPUT_FOLDER[-1] != "/":
        OUTPUT_FOLDER += "/"

    major_name = DATA_FILE.lower().split("/")[-1].split(".")[0]

    real_output_folder = OUTPUT_FOLDER + major_name + "-automatic/"

    # writing to file
    unique_df = []
    clean_data = []
    to_delete = False
    for path in listdir(real_output_folder):
        print(path)
        # file = open(real_output_folder + "/" + path, "r")
        with open(real_output_folder + "/" + path) as f:
            entire_file = f.read()
        entire_file = entire_file.replace("\n\n", "\n")
        with open(file=real_output_folder + "/" + path, mode="w") as f:
            f.write(entire_file)


def quality_checks(DATA_FILE, OUTPUT_FOLDER):
    if OUTPUT_FOLDER[-1] != "/":
        OUTPUT_FOLDER += "/"

    major_name = DATA_FILE.lower().split("/")[-1].split(".")[0]
    print(OUTPUT_FOLDER, major_name)
    real_output_folder = OUTPUT_FOLDER + "pt"

    # writing to file

    for path in listdir(real_output_folder):
        print(path)
        file = open(real_output_folder + "/" + path, "r")
        # with open(file) as f:
        lines = file.readlines()
        for idx, line in enumerate(lines):
            if "None" in line:
                print("None on line: ", str(idx), "file ->", path)
                print(line)
            if "nan" in line:
                print("nan on line: ", str(idx), "file ->", path)
                print(line)
            if re.search("\#\d+\.0", line):
                print("float on line: ", str(idx), "file ->", path)
                print(line)


if __name__ == "__main__":

    create_from_template(DATA_FILE, TEMPLATE_FOLDER, OUTPUT_FOLDER)
    validate_data(DATA_FILE=DATA_FILE, OUTPUT_FOLDER=OUTPUT_FOLDER)
    # remove_double_lines(DATA_FILE=DATA_FILE, OUTPUT_FOLDER=OUTPUT_FOLDER)
    remove_duplicate(DATA_FILE=DATA_FILE, OUTPUT_FOLDER=OUTPUT_FOLDER)
    quality_checks(DATA_FILE, OUTPUT_FOLDER)
