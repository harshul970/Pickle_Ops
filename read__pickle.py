import pickle

# Reading data from Pickle
read_pickle = open('data.pickle', 'rb')
data_read = pickle.load(read_pickle)

for key in data_read:
    print(key, ' : ', data_read[key])
read_pickle.close()
