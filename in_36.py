# 异常处理。如果try里面的代码能够执行，那就执行。
#如果不能执行，就跳过，执行except里面的代码
try:
    f = open('Test.txt', 'r+', encoding='utf-8')
    print('Test.txt opened!')
    f.close()
except:
    print('File not exists!')
print('Done!')

# dictionary
# d = {key1:value1, key2:value2, key3:value3}
# 没有顺序，而是对应。1.键key必须是唯一的；2.键只能是简单对象，比如字符串、整数、浮点数、bool值。
# list能不能作为key，但可以作为value
score = {'萧峰':95, '段誉':85, '虚竹':90, '阿朱':58}
print(score['段誉'])  # 通过键访问。字符串key需要加引号。数字key不要引号
for name in score:  # name与 for i in range(1, 10)中的i相同
    print(score[name])  # 遍历，仅仅是遍历key，而不是value。得到的却是value
score['虚竹'] = 91.5  # 给一个key赋新的值。score[key] = value
score['慕容复'] = 81  # 增加一个值，加到最前面（虽然字典无序）。score[key] = value
print(score)
del score['慕容复']  # 删除一个key:value
NoneDictionary = {} 　# 创建一个空字典


