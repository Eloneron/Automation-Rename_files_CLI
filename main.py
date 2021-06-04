# Work started - 20.05.2021
# Batch rename with CLI - initial release - 04.06.2021
# Rename files of given extension in given dir, disregard folders (with CLI)

import os
import argparse

parser = argparse.ArgumentParser(description='Batch rename files in directory')

parser.add_argument("search", type=str, help="Text to replace")
parser.add_argument("replace", type=str, help="Text to replace with")
parser.add_argument(
    "--path",  # '--' indicates that this argument is optional, if not provided it will be set to 'default'
    type=str,
    default='.',
    help='Directory path that contains files to be renamed',
)
parser.add_argument(
    "--filetype",  # '--' indicates that this argument is optional, if not provided it will be set to 'default'
    type=str,
    default=None,
    help='Only rename files with this extension (e.g .txt, default - rename all files)',
)

args = parser.parse_args()  # get hold of args provided by user in format: python main.py --path /files

print(args)

# what we want to replace
search = args.search
replace = args.replace
extension = args.filetype
path = args.path

print(f'Renaming files at path {path}')

# get files from given directory
print(f'Current working directory: {os.getcwd()}')
dir_content = os.listdir(path)

# display dir contents:
for doc in dir_content:
    print(doc)

path_dir_content = [os.path.join(path, doc) for doc in dir_content]
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
renamed = 0

print(f"{len(docs)} of {len(path_dir_content)} elements are files.")

# Iterate through all files and check if their name contains 'search':
for doc in docs:
    #check if extension is right:
    full_doc_path, filetype = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)
    # print(doc_path)
    # print(doc_name)

    if extension != None and filetype != extension:
        continue


    # neat way to check if name contains 'search' string:
    if search in doc_name:
        new_doc_name = doc_name.replace(search, replace)
        new_doc_path = os.path.join(doc_path, new_doc_name) + filetype
        print(new_doc_path)
        os.rename(doc, new_doc_path)
        renamed += 1

        print(f"Renamed file '{doc}' to '{new_doc_path}'.")

print(f"Renamed {renamed} files out of {len(docs)} files.")
