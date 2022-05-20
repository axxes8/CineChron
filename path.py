import glob
for f in glob.glob('\Users\dylan\Documents.*', recursive=True):
    print(f)