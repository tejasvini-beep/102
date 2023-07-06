import os
import shutil

from_dir="D:/Tenorshare/Tenorshare 4uKey/image_files"
to_dir="C:/Users/tejas/OneDrive/Desktop/mystory"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    if extension==" ":
     continue
    if(extension in [".pdf"]):
      path1=from_dir+"/"+file_name
      path2=to_dir+"/"+"PDF_files"
      path3=to_dir+"/"+"PDF_files"+"/"+file_name
      print("path1", path1)
      print("path3", path3)
      if os.path.exists(path2):
          print("moving")
          shutil.move(path1,path3)
    
      else:
          os.makedirs(path2)
          print("moving")
          shutil.move(path1,path3)
     