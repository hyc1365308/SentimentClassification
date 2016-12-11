import pickle
from word2index import *

def get_sentiment(sentence): #get the sentiment number
	return int(sentence.split(' ')[0].split('(')[1])

def scan_sentiment(filename, dic):
	file_object = open(filename)
	for line in file_object:
		print line

def load_local():
	#init dict
    input_dict = getDictionary("SOStr.txt",False)

    datasetSplit = open("datasetSplit.txt")
    test = open("test.txt")
    dev = open("dev.txt")
    train = open("train.txt")
    sostr = open("SOStr.txt")

    test_shape = open("test_stape.txt",'w')
    dev_shape = open("dev_shape.txt",'w')
    train_shape = open("train_shape.txt",'w')

    test_set = [1]*2
    test_set[0] = []
    test_set[1] = []

    dev_set = [1]*2
    dev_set[0] = []
    dev_set[1] = []

    train_set = [1]*2
    train_set[0] = []
    train_set[1] = []

    for line in datasetSplit:
    	number = line.split(',')[1] #The sentence is in which set

    	#get the sentence with sentiment number
    	newline = ""
    	if (number == "1\n"):
    		newline = train.readline()
    	elif (number == "2\n"):
    		newline = test.readline()
    	elif (number == "3\n"):
    		newline = dev.readline()
    	else:
    		print "first line"
    		continue

    	#get the sentiment number
    	sentiment = get_sentiment(newline)
    	
    	#get the words in the sentence
    	newline = sostr.readline()
    	wordlist = newline.split('|')
    	tmp = wordlist[len(wordlist) - 1]
    	wordlist[len(wordlist) - 1] = tmp.replace('\n','');

    	#construct new wordlist
    	new_wordlist = []
    	for i in range(len(wordlist)):
    		new_wordlist.append( input_dict[wordlist[i]] )
        del wordlist

    	#upload the set
    	if (number == "1\n"):
    		train_set[0].append(new_wordlist)
    		train_set[1].append(sentiment)
    	elif (number == "2\n"):
    		test_set[0].append(new_wordlist)
    		test_set[1].append(sentiment)
    	elif (number == "3\n"):
    		dev_set[0].append(new_wordlist)
    		dev_set[1].append(sentiment)
    	else:
    		print "first line"
    		continue

    #save the new set
    pickle.dump(train_set, train_shape)
    pickle.dump(test_set, test_shape)
    pickle.dump(dev_set, dev_shape)
    #print len(train_set[0])

    #close the file
    datasetSplit.close()
    test.close()
    dev.close()
    train.close()
    sostr.close()

    test_shape.close()
    dev_shape.close()
    train_shape.close()
    return train_set, test_set, dev_set

if __name__ == '__main__':
	train, test, dev = load_local()