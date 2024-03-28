import os
import sys
def get_image_list():
    f = open('images.txt','r')
    imagenumbers = f.readlines()
    newlist = []
    for image in imagenumbers:
        newlist.append(image.strip())
    f.close()
    return newlist
def list_text_files(directory, imagelist):
    text_files = []
    for filename in os.listdir(directory):
        for image in imagelist: 
            if filename.endswith(".txt") and "cpos" in filename and image in filename:
                filepath = os.path.join(directory, filename)
                text_files.append(filepath)

    print(text_files)
    return text_files

def read_text_file(filepath):
    with open(filepath, 'r') as file:
        content = file.readlines()
    return content

def write_to_text_file(filepath, lines_to_write):
    with open(filepath, 'w') as file:
        file.writelines(lines_to_write)

def main():
    image_list = get_image_list()
    directories = ["01","02","03","04","05", "06", "07", "08", "09", "10"]
    for directory in directories:
        # directory = sys.argv[1]  # Replace this with your directory path
        newdirectory = sys.argv[1] + "/" + directory
        text_files = list_text_files(newdirectory, image_list)
        
        # print("Text files found in directory with size greater than 1000 bytes:")
        for file_path in text_files:
            filename = os.path.basename(file_path)
            
            lines = read_text_file(file_path)
            
            # Processing lines
            processed_lines = []
            for line in lines:
                
                # Split the line into numbers
                numbers = line.split()
                # Increase the first three integers by 20%
                try:
                    modified_numbers = [str(int(float(numbers[0]) * 1.5)),str(int(float(numbers[1]) * 1.5)) ]
                    modified_line = ' '.join(modified_numbers) + '\n'
                # Append the modified line to the list
                    processed_lines.append(modified_line)
                except:
                    continue
                # Join the modified numbers back into a line
               
            
            # Write the processed lines back to the same file

            write_to_text_file(file_path, processed_lines)
            
            # print("Processed data written to", filename)
            # print()

if __name__ == "__main__":
    main()