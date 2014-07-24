import glob

master_file = open("master.txt", 'w')
for f in glob.glob("*.txt"):
    read = open(f, 'r')
    master_file.writelines(read.readlines())
