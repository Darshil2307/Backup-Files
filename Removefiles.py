import os 
import shutil
import time

def main():
    deleted_folders=0
    deleted_files=0
    path="Path name"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
       for rootFolders, folders, files in path:
           if seconds>=getFileOrFolderAge(rootFolders):
               removeFolder(rootFolders)
               deleted_folders+=1

               break
           else:
                for folder in folders:
                    folder_path=os.path.join(rootFolders,folder)
                    if seconds>=getFileOrFolderAge(folder_path):
                        removeFolder(folder_path)
                        deleted_folders+=1

                for file in files:
                    file_path=os.path.join(rootFolders,file)
                    if seconds>=getFileOrFolderAge(file_path):
                        removeFolder(file_path)
                        deleted_files+=1
       else:
        if seconds>=getFileOrFolderAge(path):
            removeFolder(path)
            deleted_files += 1

    else:
		   print(f'"{path}" is not found')
		   deleted_files += 1 

    print(f"Total folders deleted: {deleted_folders}")
    print(f"Total files deleted: {deleted_files}")

def removeFolder(path):
	if not shutil.rmtree(path):
		print(f"{path} is removed successfully")

	else:
		print(f"Unable to delete the "+path)



def removeFile(path):


	if not os.remove(path):
			print(f"{path} is removed successfully")

	else:
		print("Unable to delete the "+path)


def getFileOrFolderAge(path):

	ctime = os.stat(path).st_ctime

	return ctime


if __name__ == '__main__':
	main()