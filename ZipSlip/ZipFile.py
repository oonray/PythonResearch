from zipfile import ZipFile,ZipInfo

"""
Create Zip Folder
"""
with ZipFile("./File.zip","w") as mZipFile:
    mZipFile.write("./README.md")


"""
Extract Zipfile
"""
with ZipFile("./File.zip","r") as mZipFile:
    mZipFile.printdir()
    file_list = mZipFile.infolist()
    for i in file_list:
        print("[+] Extracting {}".format(i.filename))
        mZipFile.extract(i)

    #mZipFile.extractall()