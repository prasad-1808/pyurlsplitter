import sys

mylist = []
Duplicated_lst = []

wordlist = ''
outputFile = 'output.txt'

def printHelp():
	tool_name = "URL splitter"
	
	print("USAGE:")
	print("  gazillionsplitterpython -t <url-list> -o <outputFile>")
	
	print("OPTIONS:")
	print("  -t <worlist>: Specify the path to the URL list.")
	print("  -o <outputFile>: Specify the output file name.")
	print("  -h: Display this help message.")
	
	print("EXAMPLE:")
	print("gazillionsplitterpython -t wordlist.txt -o output.txt")
	print("gazillionsplitterpython -t list.txt -o output.txt")

def printUsage():
	tool_name = "URL splitter"
	print(tool_name)
	print("Use -h to check the help window")

def readList(wordlist):
	global targetList
	with open(wordlist,"r") as targetfile:
		targetList = targetfile.readlines()
	writeList(outputFile)
	
def writeList(outputFile):
    global Duplicated_lst
    with open(outputFile,"w") as outputfile:
        for i in targetList:
            outputfile.write("Sub directory list for " + i + "\n")
            l1 = i.split("/")
            dum_lst = []

            for j in l1:
                if j != '' and ".com" not in j and j != "https:":
                    dum_lst.append(j)
            domain = l1[0] + "//" + l1[2]

            s = domain
            outputfile.write(s + "\n")
            for i in dum_lst:
                s += "/" + i
                outputfile.write(s + "\n")
                if(len(s)!=0 and s!="\n"):
                    Duplicated_lst.append(s.strip()+"\n")
        
        Duplicated_lst = sorted(Duplicated_lst)
        outputfile.write("\n\nAfter removal of duplicated urls:\n")
        for i in Duplicated_lst:
            outputfile.write(i)
			

def main():
	if len(sys.argv) <= 1:
		printUsage()
		sys.exit(1)
	for i in range(1,len(sys.argv),2):
		if sys.argv[i] == '-t' or sys.argv[i] == '--target':
			wordlist = sys.argv[i+1]
		elif sys.argv[i] == '-o' or sys.argv[i] == '--output':
			outputFile = sys.argv[i+1]
		elif sys.argv[i] == '-h' or sys.argv[i] == '--help':
			printHelp()
			sys.exit(1)
		else:
			printUsage()
	readList(wordlist)

if __name__ == "__main__":
	main()