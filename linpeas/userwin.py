import urllib.parse
from pymongo import MongoClient
import json

# Load the JSON data from the file
with open('peas.json', 'r') as json_file:
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

# Initialize dictionary to store user and group information
user_group_info = {}

# Process each line in the clean text
current_user = None
for line in clean_text_info:
    if line.startswith("DESKTOP-"):
        current_user = line.split("\\")[1].split(":")[0]
    elif "|->Groups:" in line and current_user is not None:
        num_groups = len(line.split(","))
        user_group_info[current_user] = num_groups

# Save the output to a JSON file
with open("user_group_info_output.json", "w") as json_file:
    json.dump(user_group_info, json_file, indent=4)

print("User and group information saved to user_group_info_output.json")


# Replace with your MongoDB Atlas connection details
mongodb_url = "mongodb+srv://urstrulyprithu:" + urllib.parse.quote(
    "test@123") + "@securelycluster.wlxqkq6.mongodb.net/?retryWrites=true&w=majority"

collection_name = "UserCollection"

# Connect to MongoDB Atlas
client = MongoClient(mongodb_url)
database = client.get_database("Test")
collection = database[collection_name]

# Insert the dictionary data into the collection
inserted_id = collection.insert_one(user_group_info).inserted_id

print(f"Data inserted with ID: {inserted_id}")

# Close the MongoDB connection
client.close()