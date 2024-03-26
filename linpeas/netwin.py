import json

# Load the input JSON data from the given 'peas.json' file
with open('peas.json', 'r') as input_file:
    data = json.load(input_file)

# Extract the clean text from the JSON data
clean_text = data["Clean Text"]

# Write the clean text to a new JSON file
with open('clean_text.json', 'w') as output_file:
    json.dump({"Clean Text": clean_text}, output_file, indent=4)

print("Clean text extracted and saved to 'clean_text.json' file.")
