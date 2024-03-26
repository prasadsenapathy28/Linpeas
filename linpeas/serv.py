import json

# Read the contents from the JSON file
with open('ex.json', 'r') as json_file:
    data = json.load(json_file)

# Extract clean text for each section and store them in a dictionary
clean_text_dict = {}
for section_key, section_value in data['Services Information']['sections'].items():
    clean_text_dict[section_key] = []
    for line in section_value['lines']:
        clean_text_dict[section_key].append(line['clean_text'])

# Write the clean text dictionary to a new JSON file
with open('Service.json', 'w') as service_json_file:
    json.dump(clean_text_dict, service_json_file, indent=4)

print("Clean text extracted and saved in Service.json file.")
