import urllib.parse
from pymongo import MongoClient
import json


# Load the JSON data from the file
with open('linjson.json', 'r') as json_file:
    data = json.load(json_file)

# Extract the clean text from the nested JSON structure
clean_text_data = {}
network_information = data['Network Information']
for section_key, section_data in network_information['sections'].items():
    for line in section_data['lines']:
        if 'clean_text' in line:
            clean_text_parts = line['clean_text'].split(":")
            if len(clean_text_parts) >= 2:
                clean_text_data[clean_text_parts[0].strip()] = clean_text_parts[1].strip()

# Count the occurrences of specific keywords
keywords_to_count = ['tcp', 'udp', 'Static', 'Dynamic', 'Invalid']
keyword_counts = {keyword: 0 for keyword in keywords_to_count}

for key in clean_text_data.keys():
    for keyword in keywords_to_count:
        if keyword in key:
            keyword_counts[keyword] += 1

# Save the keyword counts into a new JSON file
with open('net.json', 'w') as output_file:
    json.dump(keyword_counts, output_file, indent=4)

print("Keyword counts saved to net.json")

# # Replace with your MongoDB Atlas connection details
# mongodb_url = "mongodb+srv://urstrulyprithu:" + urllib.parse.quote(
#     "test@123") + "@securelycluster.wlxqkq6.mongodb.net/?retryWrites=true&w=majority"

# collection_name = "NetworkCollection"

# # Connect to MongoDB Atlas
# client = MongoClient(mongodb_url)
# database = client.get_database("Test")
# collection = database[collection_name]

# # Insert the dictionary data into the collection
# inserted_id = collection.insert_one(keyword_counts).inserted_id

# print(f"Data inserted with ID: {inserted_id}")

# # Close the MongoDB connection
# client.close()