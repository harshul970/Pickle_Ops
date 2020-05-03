import pickle

dict_data = {
    ('RT1', 'sec_0'): [['sid', 'data1', 'data2', 'data3'], ['abc1', '123', '321', '442']],
    ('RT1', 'sec_1'): [['sid', 'data1', 'data2', 'data3'], ['abc2', '133', '351', '472']],
    ('RT2', 'sec_0'): [['sid', 'data1', 'data2', 'data3'], ['abcs', '113', '360', '466']],
    ('RT2', 'sec_1'): [['sid', 'data1', 'data2', 'data3'], ['abc2', '501', '660', '431']],
}

print(dict_data)

# Storing Data into Pickle
pickle_file = open('data.pickle', 'wb')
pickle.dump(dict_data, pickle_file)
pickle_file.close()
