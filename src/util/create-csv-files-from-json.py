import json
import string
import re
# import os


def createDataFiles(inputTrainingJSONFiles, inputTestJSONFiles):
    trainingJSONFiles = inputTrainingJSONFiles
    testJSONFiles = inputTestJSONFiles

    print ("Started File Conversion....")
    # print ("Working Directory: ",os.getcwd())
    
    trainingFiles = readFile(trainingJSONFiles)
    testingFiles = readFile(testJSONFiles)

    return trainingFiles, testingFiles


def readFile(fileDictionary):
    printable = set(string.printable)
    textFileDictionary = {}


    for source,filePath in fileDictionary.items():
        # print("Source: ",source,"\tFile Path: ",filePath)
        fileName = filePath.split("/")[2].split(".")[0]
        csvFilename = "data-files/" + fileName + ".txt"
        # print("CSV File: ",csvFilename)
        f = open(csvFilename,'w+')

        currentIndex = list(fileDictionary.keys()).index(source)
        # print("currentIndex: ",currentIndex)

        textFileDictionary[source] = csvFilename
        # print(trainingFiles)

        with open(filePath) as inputJSONFile:
            jsonObject = json.load(inputJSONFile)
            intentData = jsonObject[source]
            
            for eachData in intentData:
                data = eachData["data"]
                textData = ""
                for sentenceText in range(len(data)):
                    textData = textData + data[sentenceText]["text"] + " "
                # print(str(textData).strip())
                printableTextData = ''.join(filter(lambda x: x in printable, str(textData).strip()))
                filteredTextData = re.sub(' +', ' ', re.sub('[^\w\s]', '', printableTextData))
                dataToAdd = filteredTextData + "\t" + str(currentIndex) + "\n"
                f.write(dataToAdd)
        
    return textFileDictionary

inputTrainingJSONFiles = {
    'AddToPlaylist':'data-files/json/train_AddToPlaylist_full.json',
    'BookRestaurant':'data-files/json/train_BookRestaurant_full.json',
    'GetWeather':'data-files/json/train_GetWeather_full.json',
    'PlayMusic':'data-files/json/train_PlayMusic_full.json',
    'SearchCreativeWork':'data-files/json/train_SearchCreativeWork_full.json',
    'SearchScreeningEvent':'data-files/json/train_SearchScreeningEvent_full.json'
}

inputTestJSONFiles = {
    'AddToPlaylist':'data-files/json/validate_AddToPlaylist.json',
    'BookRestaurant':'data-files/json/validate_BookRestaurant.json',
    'GetWeather':'data-files/json/validate_GetWeather.json',
    'PlayMusic':'data-files/json/validate_PlayMusic.json',
    'SearchCreativeWork':'data-files/json/validate_SearchCreativeWork.json',
    'SearchScreeningEvent':'data-files/json/validate_SearchScreeningEvent.json'
}

trainingFiles, testingFiles = createDataFiles(inputTrainingJSONFiles, inputTestJSONFiles)
print("Finished....")
print(trainingFiles)
print(testingFiles)