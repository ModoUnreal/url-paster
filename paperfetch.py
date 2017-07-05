url = input("Input the url you wish to save: ")
file_obj = open("test.txt", "a")
file_obj.write("\n" + url)
