import urllib.parse
from pymongo import MongoClient
import json

# Load the JSON data from the file
with open('linjson.json', 'r') as json_file:
    data = json.load(json_file)

# Function to recursively extract user and group information from sections and lines
def extract_user_group_info(item):
    user_group_info_dict = {}
    if 'clean_text' in item:
        clean_text = item['clean_text']
        if 'uid=' in clean_text and 'gid=' in clean_text and 'groups=' in clean_text:
            parts = clean_text.split()
            username = None
            num_groups = 0
            for part in parts:
                if 'uid=' in part:
                    uid_part = part.split('=')[1]
                    if '(' in uid_part and ')' in uid_part:
                        username = uid_part.split('(')[1].split(')')[0]
                elif 'groups=' in part:
                    groups = part.split('=')[1].split(',')
                    num_groups = len(groups)
            if username:
                user_group_info_dict[username] = num_groups
    if 'sections' in item:
        for section_key, section_value in item['sections'].items():
            user_group_info_dict.update(extract_user_group_info(section_value))
    if 'lines' in item:
        for line in item['lines']:
            user_group_info_dict.update(extract_user_group_info(line))
    return user_group_info_dict

# Extract user and group information from the 'Users Information' section
users_info = data['Users Information']
user_group_info = extract_user_group_info(users_info)

# Write the output data to a JSON file
with open('user_group_info.json', 'w') as output_file:
    json.dump(user_group_info, output_file, indent=4)

# # Replace with your MongoDB Atlas connection details
# mongodb_url = "mongodb+srv://urstrulyprithu:" + urllib.parse.quote(
#     "test@123") + "@securelycluster.wlxqkq6.mongodb.net/?retryWrites=true&w=majority"

# collection_name = "UserCollection"

# # Connect to MongoDB Atlas
# client = MongoClient(mongodb_url)
# database = client.get_database("Test")
# collection = database[collection_name]

# # Insert the dictionary data into the collection
# inserted_id = collection.insert_one(user_group_info).inserted_id

# print(f"Data inserted with ID: {inserted_id}")

# # Close the MongoDB connection
# client.close()