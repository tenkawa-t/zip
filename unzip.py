import zipfile
import glob
path = "/home/tenkawa/PycharmProjects/work/test/"
#unzip
zip_list = glob.glob(path+"*.zip")
for zip in zip_list:
    with zipfile.ZipFile(zip) as zf:
        zf.extractall()