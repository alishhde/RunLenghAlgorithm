# Seyyedali Shohadaalhosseini
import matplotlib.image as mpimg
from numpy import array
from PIL import Image as im


def mainFunc():
    pixels_flattened = Read_input()
    Write_toFile(pixels_flattened)
    RLC_coding()
    RLC_encoding()


def Read_input(imagePath='D:\Teachers\DR  M. Rostaee\Multimedia\Exercises\HW1\img0-gray.jpg'):
    img_pixels_matrix = mpimg.imread(imagePath)
    print(img_pixels_matrix.shape)
    print(type(img_pixels_matrix))
    print(img_pixels_matrix[1].shape)
    return img_pixels_matrix


def Write_toFile(data):
    """ This Function will write the data to a file with respect to the shape of the main data"""
    dataFile = open("dataFile.txt", "w")
    for eachLineOfData in data:
        for char in eachLineOfData:
            dataFile.write(f"{char}:")
        dataFile.write("\n")
    dataFile.close()
    return True


def RLC_coding(dataPath='D:\Teachers\DR  M. Rostaee\Multimedia\Exercises\HW1\Code\dataFile.txt'):
    coded_list = list()
    coded_line = list()
    with open(dataPath, 'r') as dataFileToRead:
        c = 0
        for line in dataFileToRead:
            c += 1
            listOfEachValues = line.split(":")
            for value_index in range(len(listOfEachValues)):
                valCNT = 0
                if len(coded_line) > 0 and listOfEachValues[value_index] == coded_line[-1][0]:
                    continue
                for value_counter in range(value_index, len(listOfEachValues)):
                    if listOfEachValues[value_index] == listOfEachValues[value_counter]:
                        valCNT += 1
                    else:
                        coded_line.append((listOfEachValues[value_index], valCNT))
                        break
            coded_list.append(coded_line)
            coded_line = []

        # print("\n\n", coded_list)
        codeFile = open("pixelCoded.txt", "w")
        for eachline in coded_list:
            for eachPixelTuple in eachline:
                codeFile.write(f"{eachPixelTuple[0]}:{eachPixelTuple[1]}@")
            codeFile.write("\n")
        codeFile.close()
    dataFileToRead.close()


def RLC_encoding(CodedData='D:\Teachers\DR  M. Rostaee\Multimedia\Exercises\HW1\Code\pixelCoded.txt'):
    with open(CodedData, "r") as codedFile:
        mainDataList = list()
        eachLineList = list()

        for Eachline in codedFile:
            listOfLinePixelsWithFreq = Eachline.split("@")[:-1]
            for eachPixel in listOfLinePixelsWithFreq:
                pixelFreq = eachPixel.split(":")
                pixel, frequency = int(pixelFreq[0]), int(pixelFreq[1])

                for fre in range(frequency):
                    eachLineList.append(pixel)
            mainDataList.append(eachLineList)
            eachLineList = []

        arrayOfPixel = array(mainDataList)
        print(arrayOfPixel.shape)

        mpimg.imsave("a.png", arrayOfPixel)
        data = im.fromarray(arrayOfPixel, 'RGB')
        data.save('tst.png')

mainFunc()
