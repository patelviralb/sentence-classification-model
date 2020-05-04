import json
import string
import re


# import os


def create_data_files(input_training_json_files, input_test_json_files):
    training_json_files = input_training_json_files
    test_json_files = input_test_json_files

    print("Started File Conversion....")
    # print ("Working Directory: ",os.getcwd())

    training_files = read_file(training_json_files)
    testing_files = read_file(test_json_files)

    return training_files, testing_files


def read_file(file_dictionary):
    printable = set(string.printable)
    text_file_dictionary = {}

    for source, filePath in file_dictionary.items():
        # print("Source: ",source,"\tFile Path: ",filePath)
        filename = filePath.split("/")[2].split(".")[0]
        text_filename = "data-files/" + filename + ".txt"
        # print("CSV File: ",text_filename)
        f = open(text_filename, 'w+')

        current_index = list(file_dictionary.keys()).index(source)
        # print("current_index: ",current_index)

        text_file_dictionary[source] = text_filename
        # print(training_files)

        with open(filePath) as input_json_file:
            json_object = json.load(input_json_file)
            intent_data = json_object[source]

            for eachData in intent_data:
                data = eachData["data"]
                text_data = ""
                for sentenceText in range(len(data)):
                    text_data = text_data + data[sentenceText]["text"] + " "
                # print(str(text_data).strip())
                printable_text_data = ''.join(filter(lambda x: x in printable, str(text_data).strip()))
                filtered_text_data = re.sub(' +', ' ', re.sub('[^\w\s]', '', printable_text_data))
                data_to_add = filtered_text_data + "\t" + str(current_index) + "\n"
                f.write(data_to_add)

    return text_file_dictionary

# input_training_json_files = {
#     'AddToPlaylist':'data-files/json/train_AddToPlaylist_full.json',
#     'BookRestaurant':'data-files/json/train_BookRestaurant_full.json',
#     'GetWeather':'data-files/json/train_GetWeather_full.json',
#     'PlayMusic':'data-files/json/train_PlayMusic_full.json',
#     'SearchCreativeWork':'data-files/json/train_SearchCreativeWork_full.json',
#     'SearchScreeningEvent':'data-files/json/train_SearchScreeningEvent_full.json'
# }
#
# input_test_json_files = {
#     'AddToPlaylist':'data-files/json/validate_AddToPlaylist.json',
#     'BookRestaurant':'data-files/json/validate_BookRestaurant.json',
#     'GetWeather':'data-files/json/validate_GetWeather.json',
#     'PlayMusic':'data-files/json/validate_PlayMusic.json',
#     'SearchCreativeWork':'data-files/json/validate_SearchCreativeWork.json',
#     'SearchScreeningEvent':'data-files/json/validate_SearchScreeningEvent.json'
# }

# training_files, testing_files = create_data_files(input_training_json_files, input_test_json_files)
# print("Finished....")
# print(training_files)
# print(testing_files)
