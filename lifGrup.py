import json
from pprint import pprint

# Create the base object with constant fields
base_object = {
 
        "COMPANYCODE": "00003",
            "FUNDTYPE": "SIF",
            "LINENO":1,
            "INSUREDCODE":"IP000000088042",
            "SERIALNO": 1,
            "PARENTDOCUMENTNO":"JSV2004-35",
            "DOCUMENTNO": "199400172",
            "ENDORSEMENTCOUNT": 1,
            "LATESTENDORSEMENTCOUNT": 2,
            "TRANSCODE":"11",
            "EFFECTIVEFROM": "2008-2-2",
            "EFFECTIVETO": "2008-11-9",
            "CHANGETYPE": "M",
            "SCHEMETYPE": "NSTND",
            "SCHEMENATURE": "FLATR",
            "SCHEMECLASS":"",
            "SCHEMENAME": "NON-STANDARD",
            "DESCRIPTION": "SCHEME-3",
            "SUMINSURED": 750000.0,
            "FOREIGNSUMINSURED": 750000.0,
            "PREMIUMAMOUNT": 25750.0,
            "FOREIGNPREMIUMAMOUNT": 25750.0,
            "PREVIOUSANNUALPREMIUMAMOUNT": 20000.0,
            "FRGPREVIOUSANNUALPREMIUMAMOUNT": 10000.0,
            "ANNUALPREMIUMAMOUNT": 50000.0,
            "FOREIGNANNUALPREMIUMAMOUNT": 50000.0,
            "EXCHANGERATE":1,
            "SCHEMESUMINSURED": 52.0,
            "SCHEMEFOREIGNSUMINSURED": 78.0,
            "SCHEMEPREMIUMAMOUNT": 789.0,
            "SCHEMEFOREIGNPREMIUMAMOUNT": 456.0,
            "SCHEMEFRGANNUALPREMIUMAMOUNT": 452.0,
            "SCHEMEANNUALPREMIUMAMOUNT": 4502.0
}

# Generate 100 objects with increasing SERIALNO
json_objects = []
for i in range(1, 1001):
    # Create a copy of the base object and update the SERIALNO field
    obj = base_object.copy()
    obj["SERIALNO"] = i
    # Add the object to the list of JSON objects
    json_objects.append(obj)

# Save the list of JSON objects to a file
with open('lifgrp.json', 'w') as f:
    json.dump(json_objects, f, indent=4)

# Print the list of JSON objects in a formatted way
pprint(json_objects, indent=4)
