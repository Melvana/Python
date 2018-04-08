#Matches all of the filenames which begin with “Python”, have one more character of any type, then end with ”.py”
import glob
for name in glob.glob('Python*?.py'):
    print (name)
