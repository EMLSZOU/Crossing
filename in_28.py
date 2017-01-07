# 28.string slice
sentence = 'I am an English sentence.'
list_sentence = sentence.split()
print(list_sentence)
for i in sentence:
    print(i, end=' ')
print()
sentence1 = ' '.join(list_sentence)
print(sentence1)
print(sentence[:])
print('.'.join(sentence))

# file
openpy = open('Untitled-2', 'r+', encoding='UTF-8')  # 打开文件。有时候默认gbk打开，会报错
print('文件名是', openpy)
print(openpy.tell())
text = openpy.read(20)  # 读取指定的字母数或者中文字数。如果未给定或为负，则读取所有
print(text)
print(openpy.readline(2))
openpy.write('将此字符串写入文件，没有返回值。')
print(openpy.read())  # 注意缓存机制。并不会从头读起，而是读取上次read了20之后的内容。并且刚write的内容不可读。
openpy.close()  # 关闭文件。关闭后不能再读写
del text

openpy = open('Untitled-2', 'r+', encoding='UTF-8')  # 上次write的内容，需要关闭重新打开才能看到。.flush()也可以
text = openpy.read()
# 创建一个新文件，并且将旧文件的数据存入其中。
open_another = open('filex', 'w+', encoding='UTF-8')
open_another.write(text)
open_another.flush()
open_another = open('filex', 'r+', encoding='UTF-8')
print('open_another:', open_another.read())
open_another.close()

open_another = open('filex', 'r+', encoding='UTF-8')
print('输入一些内容，存入文件中')
inword = input()
open_another.write(inword+"\n")  # 注意input()没有换行符，需要加上换行符，否则会报错。
open_another.close()
open_another = open('filex', 'r+', encoding='UTF-8')
print('open_another:', open_another.read())
# TODO
# 一个乱码问题 https://segmentfault.com/q/1010000000397712
open_another.close()
