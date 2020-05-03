import json
import string
import sys, unicodedata, re

print ("Started File Conversion")

trainingFiles = {
    'AddToPlaylist':'data-files/json/train_AddToPlaylist_full.json',
    # 'BookRestaurant':'data-files/json/train_BookRestaurant_full.json',
    # 'GetWeather':'data-files/json/train_GetWeather_full.json',
    # 'PlayMusic':'data-files/json/train_PlayMusic_full.json',
    # 'SearchCreativeWork':'data-files/json/train_SearchCreativeWork_full.json',
    # 'SearchScreeningEvent':'data-files/json/train_SearchScreeningEvent_full.json'
}

# testFiles = {
#     'AddToPlaylist':'data-files/json/validate_AddToPlaylist.json',
#     'BookRestaurant':'data-files/json/validate_BookRestaurant.json',
#     'GetWeather':'data-files/json/validate_GetWeather.json',
#     'PlayMusic':'data-files/json/validate_PlayMusic.json',
#     'SearchCreativeWork':'data-files/json/validate_SearchCreativeWork.json',
#     'SearchScreeningEvent':'data-files/json/validate_SearchScreeningEvent.json'
# }

# Get all unicode characters
all_chars = (unichr(i) for i in xrange(sys.maxunicode))
# Get all non printable characters
control_chars = ''.join(c for c in all_chars if unicodedata.category(c) == 'Cc')
# Create regex of above characters
control_char_re = re.compile('[%s]' % re.escape(control_chars))
# Substitute these characters by empty string in the original string.
def remove_control_chars(s):
    return control_char_re.sub('', s)
print (remove_control_chars('\x00\x01String'))

for source,filePath in trainingFiles.items():
    print("Source: ",source,"\tFile Path: ",filePath)
    with open(filePath) as inputJSONFile:
        jsonObject = json.load(inputJSONFile)
        intentData = jsonObject[source]
        
        for eachData in intentData:
            data = eachData["data"]
            textData = ""
            for sentenceText in range(len(data)):
                textData = textData + data[sentenceText]["text"] + " "
            print(str(textData).strip())
            filteredTextData = filter(lambda x: x in string.printable, str(textData).strip())
            print(filteredTextData)