with open("iwrite.txt", "r") as file1:
    myline1 = file1.readline()
    file1.seek(0)
    mylines = file1.readlines()

    print(myline1)
    print(mylines[3])

    for line in mylines:
        print(line)




  #  myfile = file1.read()
   # print(myfile)

  #  file1.seek(0)

 #   myfile=file1.read()
   # print(myfile)
  #  print("dagiiiiiiiiiiiii")
 #   print(type(myfile))
 #   print(myline1[2])
   # file1.close()

