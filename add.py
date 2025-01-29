def add_https_to_sites(input_file='website.txt', output_file='site.txt'):
    try:
        with open(input_file, 'r') as f:
            sites = f.readlines()
        
        with open(output_file, 'w') as f:
            for site in sites:
                site = site.strip()
                if not site.startswith("https://"):
                    site = "https://" + site
                f.write(site + '\n')
        
        print(f"Updated sites have been saved to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    add_https_to_sites()