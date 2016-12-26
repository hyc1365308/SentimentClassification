def getDictionary(filename,flag):
    f = open(filename)
    dic = {}  
    k = 0
    num = 1
    dic['.'] = 0
    for line in f:
        k = k + 1
        if k > 2 and flag:
            break;
        #print line,
        split_sen = line.split('|')
        tmp = split_sen[len(split_sen)-1]
        split_sen[len(split_sen)-1] = tmp.replace('\n','')
        #print split_sen
        for word in split_sen:
            lower_word = word.lower()
            if not dic.has_key(lower_word):
                dic[lower_word] = num
                num = num +1
    f.close()  
    if flag:
        print dic
    return dic

def get_word2vec(filename):
    f = open("news.txt")
    dic = {}
    k = 0
    dim = 25
    f.readline() # ignore the first line
    for line in f:
        # print(line)
        split_sen = line.split(' ')
        word = split_sen[0]
        for i in range(1,dim+1):
            split_sen[i] = float(split_sen[i])
        vec = split_sen[1:dim+1]
        dic[word] = vec
        k = k + 1
        if k % 10000 == 0:
            print k
    print("dictionary finished!")   
    return dic

dic = get_word2vec("SOStr.txt")
# print dic
# dic = getDictionary("SOStr.txt",True)
# print dic