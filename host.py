# -*- coding: utf-8 -*-

# file operator create

f = open('hosts','r')
anotherf = open('hosts-shadowrocket-v2','w')

# define a new empty variable to temporary save result
result =list()

# a big big loop for edit string
for line in f.readlines() :

	line = line.strip()
	if line.startswith('#') or not len(line) :
		pass
	else :
		linelist = line.split()

		# exchange two list element for justfy the synax rule of shadowrocket app
		temp = linelist[0]
		linelist[0] = linelist[1]
		linelist[1] = temp

		line = ' = '.join(linelist)
	result.append(line)

# create string to write to file
hosts = '\n'.join(result)
anotherf.write(hosts)

# close file operator
f.close()
anotherf.close()

# exit
exit(0)
