import json

# Read JSON data from 'MacPEASjson.json' file
with open('MacPEASjson.json', 'r') as json_file:
    data = json.load(json_file)

# Extract "clean_text" values with specific keys
extracted_data = {}
for line in data["System Information"]["sections"]["Operative system"]["lines"]:
    parts = line["clean_text"].split(":")
    if len(parts) >= 2:
        key = parts[0].strip()
        value = ":".join(parts[1:]).strip()
        extracted_data[key] = value

# Retrieve required information
os_name = extracted_data.get("System Version", "N/A")
os_version = extracted_data.get("Kernel Version", "N/A")
host_name = extracted_data.get("Computer Name", "N/A")

date_uptime_section = data["System Information"]["sections"]["Date & uptime"]["lines"]
current_time_line = date_uptime_section[0]["clean_text"]
current_time = current_time_line.split("up")[-1].strip()

# Create a dictionary for the extracted information
extracted_info = {
    "OS Name": os_name,
    "OS Version": os_version,
    "Host Name": host_name,
    "Current Time": current_time
}

# Save the extracted data to a new JSON file
with open("macsys.json", "w") as outfile:
    json.dump(extracted_info, outfile, indent=2)

print("Extracted data has been stored in 'extractedInfo.json' file.")
