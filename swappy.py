def swapFileData():
    file1=input("enter file name:")
    file2=input("enter the file to swap with:")
    with open(file1,'r') as a :
        data_a = a.read()
    
    with open(file2,'r') as b :
        data_b = a.read()

    with open(file2,'w') as b:
        a.write(data_b)

    with open(file1,'w') as a:
        b.write(data_a)

    with open(file2,'w') as b:
        a.write(data_b)
    