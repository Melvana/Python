import glob, collections
python_files = glob.glob('*.py')
for file_name in sorted(python_files):
    print ('' + file_name)
    with open(file_name) as f:
        for line in f:
        	line = line.rstrip()
def unique_list(l): return list(OrderedSet(l))