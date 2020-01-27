import os
import zipfile
import tarfile
import hashlib
from datetime import datetime as dt

tar_compression = "bz2"
backup_dir = "backup"
files = os.listdir("files")


def test_size():
    pass

def make_backup_dir(dirname):
    """
    @param dirname (str) The name of the backup directory
    @brief makes a backup directory
    """
    if os.path.exists(dirname):
        print("Direcotry {} Exists".format(dirname))
        return False
    else:
        os.mkdir(dirname)
        return True

def make_tar(filename,files,compression):
    """
    @param filename (str) The name of the archive.
    @param files (list) The files that are to be compressed
    @param compression (str) The compression to use.
    @brief Makes a TAR file from the provided files.
    """
    name = "{}.tar.{}".format(filename,compression)

    if os.path.exists(name):
        if tarfile.is_tarfile(name):
            print("Tarfile Exits!")
            return False
        else:
            print("File is not a tar file")
            return None
    else:
        with tarfile.open(name,"w:{}".format(compression)) as tar:
            if type(files) != list:
                raise ValueError("The parameter files needs to be a list")
            for f in files:
                tar.add(f)
                return True

def make_zip(filename,files):
    """
    @param filename (str) The name of the archive.
    @param files (list) The files that are to be compressed

    @brief Makes a ZIP file from the provided files.
    """
    name = "{}.zip".format(filename)
    if os.path.exists(name):
        if zipfile.is_zipfile(name):
            print("Zipfile {} Exists".format(name))
            return False
        else:
            return None
    else:
        with zipfile.ZipFile(name,"w",compression=zipfile.ZIP_BZIP2) as zipf:
            for f in files:
                zipf.write(f)
            return True


if __name__ == "__main__":
    if make_backup_dir(backup_dir):   # Returns true if Folder Was Created
        if not make_backup_dir(backup_dir): #Returns false if folder exists
            print("Directory Created!")

    files = ["{}/{}".format("files",f) for f in files]
    t = dt.today()
    ts = t.strftime("%d:%m:%Y-%H:%M")

    if make_tar("{}/{}".format(backup_dir,ts),files,tar_compression):
            if not make_tar("{}/{}".format(backup_dir,ts),files,tar_compression):
                print("Tar Archive Created!")

    if make_zip("{}/{}".format(backup_dir,ts),files):
        if not make_zip("{}/{}".format(backup_dir,ts),files):
            print("Zip Arcive Created!")

