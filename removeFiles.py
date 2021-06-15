import os
import shutil
import time

 

def main():
    deleted_folders_count=0
    deleted_files_count=0

    #specify path
    path="/PATH)TO_DELETE"

    #specofy days
    days=30

    #converting days to seconds
    #time.time() returns current time in seconds
    seconds=time.time() - (days* 24 * 60 * 60) #h24 huors into minuted into seconds
    
    if os.path.exists(path):
        
        #iterating over each and every folder, files, etc.
        for root_folder,folders,files in os.walk(path):

            #comparing days
            if seconds>= get_file_or_folder_age(root_folder):
                
                #removing folder
                remove_folder(root_folder)
                deleted_folders_count+=1 

                #breaking after removing root_folder
                break

            else:

                #checking folder from the root_folder
                for folder in folders:

                    #folder path

                    folder_path=os.path.join(root_folder, folder)

                    #comparing with the days
                    if seconds>= get_file_or_folder_age(folder_path):
                        deleted_folders_count+=1

                #checking current directory files

                for file in files:

                    #file path
                    file_path=os.path.join(root_folder, file)

                    #comparing the days
                    if seconds>= get_file_or_folder_age(file_path):
                        deleted_files_count+=1

                else:

                #if the path is ot directory
                #comparing with the days

                    if seconds>= get_file_or_folder_age(path):

                        #invoking the file
                        remove_file(path)
                        deleted_files_count+=1
    else:
        print(f"{path}" "is not found")
        deleted_files_count+=1


        print(f"Total folders deleted: {deleted_folders_count}")
        print(f"Total files deleted: {deleted_files_count}")


def remove_folder(path):

    #removing the folder
    if not shutil.rmtree(path):

        #success message
        print(f"{path} is removed succesfully")
    else:

        #failuer message

        print(f"Unable to delete the folder: {path}")


def remove_file(path):
    
    #removing the folder
    if not os.rmtree(path):

        #success message
        print(f"{path} is removed succesfully")
    else:

        #failuer message

        print(f"Unable to delete the file: {path}")


def get_file_or_folder_age(path):
    ctime=os.stat(path).st_ctime
    
    #returning the time
    return ctime
        

               



