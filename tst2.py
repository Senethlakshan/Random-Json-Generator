import random
import string
import json

data = []

for i in range(1000):
    endorsement_type = ''.join(random.choices(string.ascii_uppercase, k=4))
    user_object = {
        "COMPANYCODE": "00003",
        "FUNDTYPE": "SIF",
        "PARENTDOCUMENTNO": "JSV2004-35",
        "DOCUMENTNO": "199400172",
        "ENDORSEMENTCOUNT": 1,
        "ENDORSEMENTTYPE": endorsement_type,
        "CODE": "VCSL1"
    }
    data.append(user_object)

# Format the data as JSON
formatted_data = json.dumps(data, indent=4)

# Print the formatted data to the console
print(formatted_data)

# Save the formatted data to a file
with open("output.json", "w") as outfile:
    outfile.write(formatted_data)
