import pickle

dict_data = {
    ('RT3', 'sec_0'): [['sid', 'data1', 'data2', 'data3'], ['abc4', '123', '321', '442']],
    ('RT3', 'sec_1'): [['sid', 'data1', 'data2', 'data3'], ['abc5', '133', '351', '472']],
    ('RT4', 'sec_0'): [['sid', 'data1', 'data2', 'data3'], ['abcq', '113', '360', '466']],
    ('RT4', 'sec_1'): [['sid', 'data1', 'data2', 'data3'], ['abcp', '501', '660', '431']],
}

## Updating data into Pickle
read_pickle = open('data.pickle', 'rb')
dict_data_read = pickle.load(read_pickle)
read_pickle.close()

## Updating Dictionary
dict_data_read.update(dict_data)

## Writing into Pickle
write_pickle_file = open('data.pickle', 'wb')
pickle.dump(dict_data_read, write_pickle_file)
write_pickle_file.close()
