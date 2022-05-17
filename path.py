import glob
for f in glob.glob('Users\Taylor\Videos.*', recursive=True):
    print(f)