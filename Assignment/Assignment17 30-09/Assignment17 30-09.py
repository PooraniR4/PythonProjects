f = open('count_words.txt', mode='w')
f.write('I have eye cream with me')
f.close()
f1 = open('count_words.txt', mode='r')
write = f1.read()
c = 0
for i in write.split(' '):
    if (i.endswith('e')):
        for j in i:
            c = c + 1
        print(i, ' ', c)

f1.close()