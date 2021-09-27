import cv2
import time
import os


def getListOfFiles(dirName):
    listOfFiles = os.listdir(dirName)
    #os.listdir(path='.') => returns a list containing the names of the entries in the directory given by path. The list is in arbitrary order, and does not include the special entries '.' and '..' even if they are present in the directory.
    allFiles = list()
    
    for entry in listOfFiles:
        fullPath = os.path.join(dirName, entry)
        #os.path.join(path, *paths) => join one or more path components intelligently. The return value is the concatenation of path and any members of *paths with exactly one directory separator following each non-empty part except the last, meaning that the result will only end in a separator if the last part is empty.
        if os.path.isdir(fullPath):
        #os.path.isdir(path) => returns True if path is an existing directory
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
            
    return allFiles



def main():
    dirname = 'pictures'
    listOfFiles = getListOfFiles(dirname)
    
    for i in range(20):
        imagePath = listOfFiles[i]
        print(imagePath)
        cascPath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale(gray,
                                            scaleFactor=1.1,
                                            minNeighbors=5,
                                            minSize=(30,30))
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
        cv2.imshow("Faces found", image)
        cv2.waitKey(4)
        time.sleep(5)
        cv2.destroyAllWindows()
        


if __name__ == '__main__':
    main()
