from zipfile import ZipFile

with ZipFile("./File.zip","w") as mZipFile:
    mZipFile.write("./README.md")