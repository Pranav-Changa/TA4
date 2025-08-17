#reading file and exception handling
try:
    file1=open("sample.txt","r")
    lines=file1.read()
    print(lines)
    file1.close()
except:
    print("Error: The file 'sample.txt' was not found.")
