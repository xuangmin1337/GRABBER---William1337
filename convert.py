def format_urls(input_file, output_file):
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            for line in infile:
                # Remove whitespace and trailing characters
                url = line.strip()
                # Skip empty lines
                if not url:
                    continue
                # Ensure URL ends correctly and prepend 'https://'
                if url.endswith('...'):
                    url = url[:-3]
                formatted_url = f"https://{url}"
                # Write to output file
                outfile.write(formatted_url + "\n")
        print(f"URLs have been formatted and saved to {output_file}")
    except FileNotFoundError:
        print(f"File {input_file} not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # File containing the list of URLs
    input_file = "listweb.txt"
    # File to save the formatted URLs
    output_file = "formatted_listweb.txt"
    format_urls(input_file, output_file)