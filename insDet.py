import json
from pprint import pprint

# Create the base object with constant fields
base_object = {
 
      "COMPANYCODE": "00003",
  "FUNDTYPE": "SIF",
  "INSTALLMENTNUMBER": 4,
  "DUEDATE": "2003-7-3",
  "GROSSPREMIUM": 2421.0,
  "FOREIGNGROSSPREMIUM": 584.02,
  "NETPREMIUM": 680.92,
  "FOREIGNNETPREMIUM": 2421.0
}

# Generate 100 objects with increasing SERIALNO
json_objects = []
for i in range(1, 1001):
    # Create a copy of the base object and update the SERIALNO field
    obj = base_object.copy()
    obj["INSTALLMENTNUMBER"] = i
    # Add the object to the list of JSON objects
    json_objects.append(obj)

# Save the list of JSON objects to a file
with open('insDet.json', 'w') as f:
    json.dump(json_objects, f, indent=4)

# Print the list of JSON objects in a formatted way
pprint(json_objects, indent=4)
