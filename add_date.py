import os
import datetime
import argparse

def add_date_to_filenames(directory):
    # Get today's date in YYYY-MM-DD format
    today_date = datetime.date.today().strftime("%Y-%m-%d")
    
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    # List all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Only process files (skip directories)
        if os.path.isfile(file_path):
            # Avoid adding the date twice if the script is run multiple times
            if not filename.startswith(today_date):
                new_filename = f"{today_date}-{filename}"
                new_file_path = os.path.join(directory, new_filename)
                
                # Rename the file
                os.rename(file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")
            else:
                print(f"Skipped: {filename} (already starts with today's date)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add today's date (YYYY-MM-DD) to the beginning of filenames in a folder.")
    parser.add_argument("folder", nargs="?", default=".", help="Path to the folder (default: current directory)")
    
    args = parser.parse_args()
    add_date_to_filenames(args.folder)
