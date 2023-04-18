import random
import json

data = []

for i in range(1000):
    family_no = random.randint(1, 5)
    user_object = {
        "COMPANYCODE": "00003",
        "FUNDTYPE": "SIF",
        "LINENO": 1,
        "SERIALNO": i + 1,
        "ITEMSERIALNO": 5444,
        "FAMILYNO": family_no,
        "PARENTLINKID": "POL2004126824",
        "PARENTDOCUMENTNO": "JSV2004-35",
        "DOCUMENTNO": "199400172",
        "ENDORSEMENTCOUNT": 1,
        "LATESTENDORSEMENTCOUNT": 2,
        "DOCUMENTTYPE": "POL",
        "TRANSCODE": "11",
        "EFFECTIVEFROM": "2008-2-2",
        "EFFECTIVETO": "2008-11-9",
        "CHANGETYPE": "M",
        "NAME": "Smith",
        "CATEGORY": "DEP",
        "TITLE": "Mr.",
        "SEX": "M",
        "DATEOFBIRTH": "1980-01-01",
        "AGE": "38",
        "INSUREDCODE": "IP000000088042"
    }
    data.append(user_object)

# Format the data as JSON
formatted_data = json.dumps(data, indent=4)

# Print the formatted data to the console
print(formatted_data)

# Save the formatted data to a file
with open("grpmem.json", "w") as outfile:
    outfile.write(formatted_data)
