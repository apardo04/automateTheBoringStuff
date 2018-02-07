from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("C:\Globalrose Bitbucket\/amp.globalrose.com\wholesale") if isfile(join("D:\Globalrose Bitbucket\/amp.globalrose.com\wholesale", f))]

for file in onlyfiles:
    print(file)