def swapFileData():
    file1 = "C:/WhiteHat/Python/file1.txt"
    file2 = "C:/WhiteHat/Python/file2.txt"


    with open("C:/WhiteHat/Python/file1.txt", 'r') as a:
        data_a = a.read()

    with open("C:/WhiteHat/Python/file2.txt", 'r') as b:
        data_b = b.read()

    with open("C:/WhiteHat/Python/file1.txt", 'w') as a:
        a.write(data_b)

    with open("C:/WhiteHat/Python/file2.txt", 'w') as b:
        b.write(data_a)

swapFileData()

        

        

        
    
