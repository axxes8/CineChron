import glob
<<<<<<< HEAD
for f in glob.glob('\Users\dylan\Documents.*', recursive=True):
    print(f)
=======
import os
 
movieList = []
# This is the path
path="Z:/**/*.*"
 
# Recursivly searches through path finding all files and returns the path for each file.
for file in glob.iglob(path, recursive=True):
    # Strip off the path and append the file name to 'movieList'
    movieList.append(os.path.basename(file))
    # print(os.path.basename(file))
    
print(movieList)
print("Found", len(movieList), "files.")
>>>>>>> d922671114c93e58fd8dfaad9e3d6ba73f9776d8
