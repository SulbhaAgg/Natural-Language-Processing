import os


def reviewsIntoFile(mainFolder , fileName ):
    outFile = open( fileName , "w", encoding="utf8")
    for subdirs in os.listdir(mainFolder):
         folder = os.path.join(mainFolder, subdirs)
         for filename in os.listdir(folder):
            temp1 = os.path.join(folder, filename)
            inputFile = open(temp1, 'r', encoding= 'utf-8')
            Lines = inputFile.readlines()
            for line in Lines:
                if subdirs == "neg":
                    outFile.write( "neg " + line + "\n")
                else:
                    outFile.write("pos " + line + "\n")

            inputFile.close()
    outFile.close()

mainFolder = "movie-review-HW2/aclImdb/test"
reviewsIntoFile(mainFolder , "testReviews" )

mainFolder = "movie-review-HW2/aclImdb/train"
reviewsIntoFile(mainFolder , "trainReviews" )



