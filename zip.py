import zipfile
import glob

path = "/home/tenkawa/PycharmProjects/work/test/"
zip_list = glob.glob(path+"*")
#zip
with zipfile.ZipFile(path + "test3.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    zf.write(path + "/test.txt", "test.txt")

