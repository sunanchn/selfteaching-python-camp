 
text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}


def stats_text_en(text):
    import re
    '''只保留英文'''
    text = re.sub("[^A-Za-z]"," ",text.strip())
    list1 = re.split(r"\w",text)
    while '' in list1:
        list1.remove('')
    for i in list1:
        """将出现次数，分别赋值给dict1的键和值"""
        dict1.setdefault(i,list1.count(i))
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)
    for tup1 in tup1:
        dict2[tup1[0]] = dict1[tup1[0]]
    return dict2


print("英文词频统计结果为：")
print(stats_text_en(text))
str = ''



'''创建一个名为stats_text_cn的函数，用来统计中文词频'''
def histogram(s, old_d):
    d = old_d
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

def stats_text_cn(text):
    import re
    """去掉text中的英文和数字"""
    text = re.sub("[A-Za-z0-9]", "", text)
    '''将字符串text转换为列表list1,只保留单词为list1中的元素'''
    list1 = re.split(r"\W+",text)   

    '''删除list1中为空的列表元素'''
    while '' in list1:   
        list1.remove('')
    
    ''' 把dict3的行拆成单字，拆成字典格式的'''
    dict3 = dict()
    '''给dict3赋值'''
    for i in range(len(list1)):
        dict3 = histogram(list1[i], dict3)

    """将dict3按照value值从大到小排列，并将结果赋给元组tup1"""
    tup1 = sorted(dict3.items(),key = lambda items:items[1],reverse = True)  

    """遍历元组tup1"""
    for tup1 in tup1:   
            dict4[tup1[0]] = dict3[tup1[0]]  
    return dict4

print("统计中文词频的结果为:")
print(stats_text_cn(text))