#!/bin/bash

# File to modify
file="/opt/conda/lib/python3.8/site-packages/lddl/download/wikipedia.py"

# New content to replace the function body
new_content='''def _get_url(lang):
    return ("https://dumps.wikimedia.your.org/enwiki/20220820/enwiki-20220820-pages-articles.xml.bz2")
'''

# Flag to track if we are inside the function
inside_function=0

# Read the file line by line
while IFS= read -r line; do
    # Check if we are inside the function
    if [[ $line == "def _get_url(lang):" ]]; then
        inside_function=1

        echo "$new_content"
    elif [[ $inside_function -eq 1 && $line == "" ]]; then
        inside_function=0
    fi

    # Output the current line if we are not inside the function
    if [[ $inside_function -eq 0 ]]; then
        echo "$line"
    fi
done < "$file" > tmpfile && mv tmpfile "$file"









