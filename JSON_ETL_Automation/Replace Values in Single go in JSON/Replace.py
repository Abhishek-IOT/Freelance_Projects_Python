import os

# Path to your folder
folder_path = '//folder//Path'  # Replace with your path

# Loop through each JSON file
for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)

        # Read the file as a plain string
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace all occurrences of "abhishek" with "Abhi"
        updated_content = content.replace("Ann", "Abhishek")

        # Overwrite the same file with updated content
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"✅ Replaced in: {filename}")

print("🎯 All JSON files updated using string replacement.")
