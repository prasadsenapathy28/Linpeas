
import json

# Load the JSON data from the file
with open('linjson.json', 'r') as json_file:
    data = json.load(json_file)

# Function to recursively extract clean text from sections and lines
def extract_clean_text(item):
    clean_text_list = []
    if 'clean_text' in item:
        clean_text_list.append(item['clean_text'])
    if 'sections' in item:
        for section_key, section_value in item['sections'].items():
            clean_text_list.extend(extract_clean_text(section_value))
    if 'lines' in item:
        for line in item['lines']:
            clean_text_list.extend(extract_clean_text(line))
    return clean_text_list

# Extract clean text from the 'Users Information' section
users_info = data['Users Information']
clean_text_info = extract_clean_text(users_info)

# Create a dictionary to store the extracted clean text
output_data = {
    'clean_text_info': clean_text_info
}

# Write the output data to a JSON file
with open('usermac.json', 'w') as output_file:
    json.dump(output_data, output_file, indent=4)