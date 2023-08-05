import os
import shutil

# Create directory name "destination" in the folder from where script is executing
def list_items_in_directory(directory_path):
    try:
       
        items = os.listdir(directory_path)
        for dirs in items:
            #print(dirs)
            if "." in dirs or "destination" in dirs:
                continue
            else:
                os.chdir(dirs)
                files = os.listdir(os.getcwd())
                print(files)
                print(os.getcwd())
                for item in files:
                    if ".cpp" in item:
                        print(os.getcwd()+"\\"+item)
                        source_file_path = os.getcwd()+"\\"+item
                        destination_file_path = directory_path+"\\destination"
                        try:
                            shutil.copy(source_file_path, destination_file_path)
                            print("File moved successfully!")
                        except shutil.Error as e:
                            print(f"Error while moving the file: {e}")
                        except FileNotFoundError:
                            print("Source file not found.")
            os.chdir(directory_path)

    except OSError as e:
        print(f"An error occurred: {e}")

 
 

path_to_directory = os.getcwd()
list_items_in_directory(path_to_directory)
