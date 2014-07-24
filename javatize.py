
master_file = open("master.txt", 'r')
java_class_file = open("javaclass.txt", 'w')

def createJava(line):
	strings = line.split('\t')
	java_class_file.write("new Quote(\"%s\", \"%s\", \"%s\");\n" % (strings[0], strings[1], strings[2][:-1]) )

for line in master_file:
	createJava(line)