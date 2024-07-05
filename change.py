import os
import sys

def update_file(file_path):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # replacement
    updated_content = content.replace(
        "https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2",
        "https://dumps.wikimedia.your.org/enwiki/20220820/enwiki-20220820-pages-articles.xml.bz2"
    ).replace(
        "'wikicorpus_en.xml.bz2'",
        "'enwiki-latest-pages-articles.xml.bz2'"
    )


    with open(file_path, 'w') as file:
        file.write(updated_content)

if __name__ == "__main__":
    # Check if the file path is provided as an argument
    if len(sys.argv) < 2:
        print("Usage: python update_script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Checking the file path 
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    # Update the file
    update_file(file_path)
    print("File updated successfully.")
