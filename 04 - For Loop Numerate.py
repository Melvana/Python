#For Loop, built-in enumerate function, new style formatting

family = ['Fouad', 'Caroline', 'Nadine', 'Mae', 'Sami']
for i, name in enumerate(family):
    print "Family number {iteration} is {name}".format(iteration=i+1, name=name)
