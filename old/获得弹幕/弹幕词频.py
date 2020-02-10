def cipin(path):
    txt = open(path,'r',encoding='utf-8').read().split('\n')
    words = txt
    count={}
    for word in words:
        if len(word) ==1:
            continue
        else:
            count[word]=count.get(word,0)+1
    result = sorted(count.items(),key=lambda x:x[1],reverse=True)
    for i in range(20):
        word,count=result[i]
        print(str(i+1)+'->'+word,':',count)
path = '弹幕.txt'
cipin(path)