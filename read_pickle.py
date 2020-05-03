import pickle

# Reading data from Pickle
read_pickle = open('data.pickle', 'rb')         # Opening pickle file in binary read mode
data_read = pickle.load(read_pickle)            # Data is deserialized and stored into Dictionary

for key in data_read:
    print(key, ' : ', data_read[key])
read_pickle.close()
