import os


mainFolder = "movie-review-HW2/aclImdb/test"
for subdirs in os.listdir(mainFolder):
     folder = os.path.join(mainFolder, subdirs)
     for filename in os.listdir(folder):
            temp1 = os.path.join(folder, filename)
            files1 = open(temp1, 'r', encoding= 'utf-8')
          ...................
           files1.close()