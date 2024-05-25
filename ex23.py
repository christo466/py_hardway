import sys

# Unpack command-line arguments
script, encoding, error = sys.argv

def main(language_file, encoding, errors):
    # Read one line from the language file
    line = language_file.readline()
    
    # If the line is not empty, process and print it
    if line:
        print_line(line, encoding, errors)
        # Recursively call main to process the next line
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # Strip leading/trailing whitespace from the line
    next_lang = line.strip()
    
    # Encode the stripped line into bytes using the specified encoding and error handling
    raw_bytes = next_lang.encode(encoding, errors=errors)
    
    # Decode the bytes back into a string using the same encoding and error handling
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    
    # Print the raw bytes and the decoded string
    print(raw_bytes, "<===>", cooked_string)

# Open the languages file with UTF-8 encoding
languages = open("languages.txt", encoding="utf-8")

# Start processing the file
main(languages, encoding, error)
