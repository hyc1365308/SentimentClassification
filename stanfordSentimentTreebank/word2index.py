def getDictionary(filename,flag):
    f = open(filename)
    dic = {}  
    k = 0
    num = 1
    dic['.'] = 0
    for line in f:
        k = k + 1
        if k > 10 and flag:
            break;
        #print line,
        split_sen = line.split('|')
        tmp = split_sen[len(split_sen)-1]
        split_sen[len(split_sen)-1] = tmp.replace('\n','')
        #print split_sen
        for word in split_sen:
            if not dic.has_key(word):
                dic[word] = num
                num = num +1
    f.close()  
    if flag:
        print dic
    return dic

#getDictionary("SOStr.txt",True)