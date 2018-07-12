# Assignment: Cpts 315 HW 3 - Fortune Cookie Classifier
# Programmer: Rahul Singal (11471764)
# Date Created: 3/20/18
# Date Last Edited: 3/23/18
# Description: 
# Collaborators: Prof. Doppa in class pseduocode & slides

from sklearn.linear_model import perceptron
from numpy import dot,sign


# *********************** Reading In Files *************************
filename = open('traindata.txt', 'r')
Train_Data = filename.read().splitlines()
filename.close()

filename = open('trainlabels.txt', 'r')
Train_Labels = filename.read().splitlines()
filename.close()

filename = open('stoplist.txt', 'r')
Stop_Words = filename.read().splitlines()
filename.close()

filename = open('testdata.txt', 'r')
Test_Data = filename.read().splitlines()
filename.close()

filename = open('testlabels.txt', 'r')
Test_Labels = filename.read().splitlines()
filename.close()

# *********************** Pre-Processing *************************
"""
Convert fortune cookie messages into features to be used by your classifier.
You will be using a Bag of Words Representation. Following Steps:
    
    1. Vocabulary (All Unique words in Training Data with all Stop Words Removed)
        1a). Go through all the training data and find all unique words and put into
        a vocabulary variable
        1b). Remove all the stop words in the vocabulary
        1c). Sort the vocabulary so it is in alphabetical order
        1d). Remove all stop words in each message
    
    2. Convert Training Data into a set of features. Each message will be of size 
    M (Size of vocabulary), each slot will be 0 or 1 (0 means not present, 1 means it is)
        2a). Create a list of list for the training features
        2b). Go through the message words and find the index that it represents, make slot 1
        2c). Continue for all messages 
"""

# Finding all unique words in the training data & sorting them alphabetically. 
# There are 884 unique words in the vocabulary
Vocabulary = []
for x in Train_Data:
    #x will be the string message
    x = x.split()
    for word in x:
        #word will be the unique word in the message?
        if word not in Vocabulary:
            Vocabulary.append(word)
Vocabulary.sort()

# Removing all stop words from the vocabulary
for word in Stop_Words:
    if word in Vocabulary:
        Vocabulary.remove(word)
        
# Remove all stop words in each message and sort alphabetically
# I loop 10 times in case a stop word exists more than once
for x in range(0,5):
    index = 0
    for message in Train_Data:
        message = message.split()
        #print(message)
        for word in Stop_Words:
            #print(word)
            for w in message:
                if (w == word):
                    message.remove(w)
        message.sort()
        #print(message)
        message = ' '.join(message)
        Train_Data[index] = message
        index = index + 1

# Convert Training Data into a feature vector of size M (693 words in Vocabulary)
Vocab_Size = len(Vocabulary)
Number_of_Messages = len(Train_Data)

# Initializing a feature vector with each message having a vocab size
Feature_Vector = []
for x in range(0,Number_of_Messages):
    temp_list = []
    for y in range(0,Vocab_Size):
        temp_list.append(0)
    Feature_Vector.append(temp_list)

i = 0
for fortune in Train_Data:
    #print(fortune)
    fortune = fortune.split()
    for word in fortune:
        index = Vocabulary.index(word)
        Feature_Vector[i][index] = 1
    i = i + 1

Test_Number_of_Messages = len(Test_Data)
Test_Feature_Vector = []

for x in range(0,5):
    index = 0
    for message in Test_Data:
        message = message.split()
        #print(message)
        for word in Stop_Words:
            #print(word)
            for w in message:
                if (w == word):
                    message.remove(w)
        message.sort()
        #print(message)
        message = ' '.join(message)
        Test_Data[index] = message
        index = index + 1

# Initializing a feature vector with each message having a vocab size
Test_Feature_Vector = []
for x in range(0,Test_Number_of_Messages):
    temp_list = []
    for y in range(0,Vocab_Size):
        temp_list.append(0)
    Test_Feature_Vector.append(temp_list)

i = 0
for fortune in Test_Data:
    #print(fortune)
    fortune = fortune.split()
    for word in fortune:
        try:
            index = Vocabulary.index(word)
            Test_Feature_Vector[i][index] = 1
        except ValueError:
            pass
    i = i + 1


#Convert Train and Test Labels 0 to -1 so it works with perceptron algorithm
for x in range(0, len(Train_Labels)):
    if (Train_Labels[x] == '0'):
        Train_Labels[x] = '-1'

for x in range(0, len(Test_Labels)):
    if (Test_Labels[x] == '0'):
        Test_Labels[x] = '-1'
        

"""
Implement a binary classifier and multi class online learning algorithm using
the two given algorithms below

    1. Binary Classifier with Perceptron Weight Update using Algorithm 1
Input: D = Training Examples, T = Maximum number of Training Iterations (20)
Output: w, the final weight vector
T = 20
1a). Initialize the weights to w = (0,0,....0) -> Vocab_Size
    for x in range(0, Vocab_Size):
        w.append(0)
        
1b). For index in range(0, T):
        num_mistakes = 0
        accuracy = 0
        For y in range(0, len(Train_Data)):
            Xt = Feature_Vector[y]
            Yt = Train_Label[y]
            Yt = int(Yt)
            Yht = sign(dot(w, Xt))
            if (Yht != Yt):
                w0 = [x * Yt for x in Xt]
                w = [x + y for x,y in zip(w, w0)]
                num_mistakes = num_msitakes + 1
            else:
                pass
        print("iteration " + str(index) + " had " + str(num_mistakes) + " mistakes")
        accuracy = (len(Train_Data) - num_mistakes) / len(Train_Data)    
        print("Iteration " + str(index) + "has an accuracy of " + str(accuracy) + "%")
    
    2. Multi-Class Online Learning Algorithm using Algorithm 2
        2a).
    
"""
print("**************TRAINING DATA********************")

T = 20
w = []
for x in range(0, Vocab_Size):
    w.append(0)

for index in range(0,T):
    num_mistakes = 0
    accuracy = 0
    for y in range(0,len(Train_Data)):
        Xt = Feature_Vector[y]
        Yt = Train_Labels[y]
        Yt = int(Yt)
        Yht = sign(dot(w, Xt))
        if (Yht != Yt):
            w0 = [x * Yt for x in Xt]
            w = [x + y for x,y in zip(w, w0)]
            num_mistakes = num_mistakes + 1
        else:
            pass
    print("Iteration-" + str(index) + " No-of-Mistakes: " + str(num_mistakes))
    accuracy = (len(Train_Data) - num_mistakes) / len(Train_Data)
    print("Iteration-" + str(index) + " Training-Accuracy: " + str(accuracy))


print("**************TESTING DATA********************")
num_mistakes = 0
accuracy = 0
for x in range(0, len(Test_Data)):
    Xt = Test_Feature_Vector[x]
    Yt = Test_Labels[x]
    Yt = int(Yt)
    Yht = sign(dot(w, Xt)) 
    if (Yht != Yt):
        num_mistakes = num_mistakes + 1
    else:
        pass
    
accuracy = (len(Test_Data) - num_mistakes) / len(Test_Data)
print("Testing Mistakes: " + str(num_mistakes))
print("Testing Accuracy: " + str(accuracy))


print("**************REAL RESULTS********************")
practice = perceptron.Perceptron(max_iter=20)
practice.fit(Feature_Vector, Train_Labels)
print("Real Iteration-20 Accuracy:")
print (practice.score(Feature_Vector, Train_Labels)*100)

