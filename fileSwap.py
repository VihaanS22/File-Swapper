def fileSwapper():

    print("")
    print("Welcome to the File Swapper")
    print("")

    file1 = input("Enter your file path : ")
    print("")
    file2 = input("Enter the path of the file you want to swap it with : ")
    print("")
    print("File Swapped Successfully!! Thanks for using file swapper.")
    print("")
    

    
    with open(file1, "r") as a:
        data_a = a.read()
    with open(file2, "r") as b:
        data_b = b.read()


    with open(file1, "w+") as a:
        a.write(data_b)
    with open(file2, "w+") as b:
       b.write(data_a)

fileSwapper()

 

