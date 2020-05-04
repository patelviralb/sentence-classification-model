import pandas as pd

from sklearn.model_selection import train_test_split


def create_data_frame_list(data_file_dict):
    data_frame_list = []
    for intent, filepath in data_file_dict.items():
        data_frame = pd.read_csv(filepath, names=['sentence', 'intent'], sep='\t')  # Create data frame with heading
        # dataFrame['actual-intent'] = intent  # Add new column
        data_frame_list.append(data_frame)  # Append the row into the list

    return data_frame_list


def run_model():
    print("Model Started....")

    input_training_files = {
        'AddToPlaylist': '../data-files/train_AddToPlaylist_full.txt',
        # 'BookRestaurant': '../data-files/train_BookRestaurant_full.txt',
        # 'GetWeather': '../data-files/train_GetWeather_full.txt',
        # 'PlayMusic': '../data-files/train_PlayMusic_full.txt',
        # 'SearchCreativeWork': '../data-files/train_SearchCreativeWork_full.txt',
        # 'SearchScreeningEvent': '../data-files/train_SearchScreeningEvent_full.txt'
    }

    input_test_files = {
        'AddToPlaylist': '../data-files/validate_AddToPlaylist.txt',
        # 'BookRestaurant': '../data-files/validate_BookRestaurant.txt',
        # 'GetWeather': '../data-files/validate_GetWeather.txt',
        # 'PlayMusic': '../data-files/validate_PlayMusic.txt',
        # 'SearchCreativeWork': '../data-files/validate_SearchCreativeWork.txt',
        # 'SearchScreeningEvent': '../data-files/validate_SearchScreeningEvent.txt'
    }

    training_data_frame_list = create_data_frame_list(input_training_files)
    test_data_frame_list = create_data_frame_list(input_test_files)

    training_data_set = pd.concat(training_data_frame_list)  # Convert list to Panda data frame
    test_data_set = pd.concat(test_data_frame_list)  # Convert list to Panda data frame

    training_sentences = training_data_set['sentence'].values
    training_intents = training_data_set['intent'].values

    test_sentences = test_data_set['sentence'].values
    test_intents = test_data_set['intent'].values

    sentences_train, sentences_test, y_train, y_test = train_test_split(training_sentences, training_intents,
                                                                        test_size=0.25,
                                                                        random_state=1000)


if __name__ == '__main__':
    run_model()