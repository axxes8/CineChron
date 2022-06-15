import glob
import os
import json
 
# movieList = []
# This is the path
path = "Z:/**/*.*"
 
stripped_path = path.strip('"')
print(stripped_path)
json_movieList = []
    
## Recursivly searches through path finding all files and returns the path for each file.
for file in glob.iglob(stripped_path, recursive=True):
    ## Strip off the path and file extention, brackets and single quotations, then append the file name to 'json_movieList'
    filename = str(os.path.basename(file).split('.')[:-1]).strip('[]').strip('\'')
    filepath = str(os.path.abspath(file))

    json_movieList.append({'Title': filename, 'path': filepath})
## Convert list to JSON
json_dump = json.dumps(json_movieList)

## Print json_dump and number of movies found to the console.
print(json_dump)
print("Found", len(json_movieList), "files.")
