import time
import jieba
jieba.initialize()

#用这个来分词！！！

content = open("neg.txt","rb").read()
t1 = time.time()
words = " ".join(jieba.cut(content))

t2 = time.time()
tm_cost = t2-t1

log_f = open("neg2.txt","wb")
log_f.write(words.encode('utf-8'))
log_f.close()

print('cost ' + str(tm_cost))
print('speed %s bytes/second' % (len(content)/tm_cost))