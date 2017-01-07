f = open('scores.txt', 'r+', encoding='gbk')  # 打开文件，注意Win Txt是GBK编码
lines = f.readlines()  # 按行读取,每行成为一个元素，存入list变量lines
f.close()
print('按行切成列表：', lines)
results = []  # 预备一个空的列表results
for l in lines:  # 遍历列表lines，也就是每行数据
    data = l.split()  # 一个元素/一个人的信息（原始数据的一行）按照空格分割，存入变量data
    print('每个人的分数', data)
    sum = 0
    for score in data[1:]:  # 遍历一个人的分数。data这个list的第二个及以后的元素
        sum += int(score)  # 累加分数，求和
    result = '%s\t:%d\n' % (data[0], sum)  # 名字和求和，存入变量result
    print(result)
    results.append(result)  # 将变量result加入list变量results中
print(results)
output = open('scoresSumUp.txt', 'w+', encoding='gbk')  # 打开文件，追加编辑
#output.close()  # open和close，创建了文件
#output = open('scoresSumUp.txt', 'r+', encoding='gbk')  # 再次open，追加编辑内容
output.writelines(results)
output.close()
################## while 循环在条件不满足时结束。for 循环 遍历完序列后结束。break和continue则控制
i = 0
while i <5:
    if i ==2:
        break
    print('while ,break', i)
    i += 1
del i
for i in range(0, 5):
    if i == 2:
        break
    print('for,break', i)
#TODO while 循环的continue没有用
i = 0
while i < 5:
#    if i == 2:
#        continue
    print('while,continue', i)
    i += 1

del i
for i in range(0, 5):
    if i == 2:
        continue
    print('for,continue', i)
    i += 1