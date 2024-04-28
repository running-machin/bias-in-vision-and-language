import os
import re
import json
import requests

def extract_info_from_script(script_path):
    script_info = {"folder_name": (os.path.basename(os.path.dirname(os.path.dirname(script_path)))),
                   "subfolder_name": os.path.basename(os.path.dirname(script_path)),
                   "wget_commands": []}

    with open(script_path, 'r') as script_file:
        script_content = script_file.read()
        wget_cmds = re.findall(r'wget .*', script_content)

        for wget_cmd in wget_cmds:
            match = re.search(r'-O\s+([\w.-]+)', wget_cmd)
            if match:
                image_name = match.group(1)
                url_match = re.search(r'(https?://\S+)', wget_cmd)
                if url_match:
                    url = url_match.group(1)
                    script_info["wget_commands"].append({"image_name": image_name, "url": url})

    return script_info

def process_folder(folder_path):
    folder_info = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file == "get.sh":
                script_path = os.path.join(root, file)
                folder_info.append(extract_info_from_script(script_path))
    return folder_info

def main(folder_path):
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    folder_info = process_folder(folder_path)
    # print(folder_info)
    with open("output.json", "w") as json_file:
        json.dump(folder_info, json_file, indent=4)

if __name__ == "__main__":
    # folder_path = input("Enter the path to the folder: ")
    folder_path = "data/google-images/"
    main(folder_path)
