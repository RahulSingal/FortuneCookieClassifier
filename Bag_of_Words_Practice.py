# Bag of Words Representation Practice


messages = ['this is a test message', 'another message test']
vocabulary = ['a', 'another', 'this', 'is', 'test', 'message', 'more', 'words', 'sort']
vocabulary.sort()
M = len(vocabulary)
print(M)

test_message = [[1,0,1,1,0,0,1,1,0], [0,1,0,1,0,0,1,0,0]]

N = len(messages)

# Initializing message vector to have 2 messages with 9 vocabulary words
message_vector = []
for x in range(0,N):
    temp_list = []
    for y in range(0,M):
        temp_list.append(0)
    message_vector.append(temp_list)


# Sorting messages in alphabetical order
index = 0
for message in messages:
    message = message.split()
    message.sort()
    print(message)
    messages[index] = message
    index = index + 1

# Looping through the words in each fortune and updating message vector 
i = 0
for fortune in messages:
    for word in fortune:
        index = vocabulary.index(word)
        message_vector[i][index] = 1
    i = i + 1

if (message_vector == test_message):
    print("FUCK YES")
else:
    print("Shit")
       