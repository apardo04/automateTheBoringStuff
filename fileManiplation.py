import os
#os.chdir('C:')
sheet = open('.\\fileManipulationDir\\sheet.tsv')
print(sheet.readlines())

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
#for filename in myFiles:
#     print(os.path.join('C:','Users','asweig
# art',filename)) #will work for any os