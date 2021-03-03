#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/2/19 10:20
# @Author  : lihongzheng
# @FileName: emotion_analysis_campare.py
# @Software: PyCharm
# @function:将数据集转换为pkl的形式，作用即为生成数据集供后续使用
#####
#####Python中的pickle模块的作用是将对象进行序列化和反序列化。其中dump为序列化的函数，load为反序列化的函数。
#####Python中的.pkl文件的作用是将需要保存到本地的一些对象，数据等暂存到本地的pkl文件中，需要取出来的时候就利用load的方式取出，存储的时候就利用dump存储。
#####利用pkl存储的对象可以是字符串，bool值，字典值等，提取的时候直接提取即可。

import pickle
import jieba
import os
import re
import string
import codecs
import os


# ##文件先转码，即将gbk编码文件转化为utf8编码文件
# BLOCKSIZE = 104857600000
# FindPath = '../raw_data/'
# FileNames = os.listdir(FindPath)
# print(FileNames)
# for file_name in FileNames:
#     full_file_name = os.path.join(FindPath, file_name)
#     if 'utf8' in full_file_name:
#         break
#     with codecs.open(full_file_name, 'r', 'GBK') as f:
#         with codecs.open(full_file_name+ "_utf8", "w", "utf-8") as target_file:
#             try:
#                 while True:
#                     contents = f.readlines(BLOCKSIZE)
#                     if not contents:
#                         break
#                     target_file.write(contents)
#             except UnicodeDecodeError:
#                 print(full_file_name)


pos_words = []
neg_words = []
test_words=[]

# ######读取文件中的每一行，并添加到列表当中去
posfile=open('../raw_data/pos.txt',encoding='utf-8')#注意要加上utf8编码，不然打开时会自动转化为gbk编码，导致报错。###########3
for pos_text in posfile.readlines():
    pos_text = ''.join(pos_text.split())
    # pos_text = re.sub(string.punctuation, "", pos_text)
    pos_text = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）～-]+", "", pos_text)
    pos_list = jieba.cut(pos_text, cut_all=False)
    pos_words.append(list(pos_list))

negfile=open('../raw_data/neg.txt',encoding='utf-8')
for neg_text in negfile.readlines():
    neg_text = ''.join(neg_text.split())
    # pos_text = re.sub(string.punctuation, "", pos_text)
    neg_text = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）～-]+", "", neg_text)
    neg_list = jieba.cut(neg_text, cut_all=False)
    neg_words.append(list(neg_list))

testfile=open('../raw_data/test(50pos 20neg).txt',encoding='utf-8')
for test_text in testfile.readlines():
    test_text = ''.join(test_text.split())
    # pos_text = re.sub(string.punctuation, "", pos_text)
    test_text = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）～-]+", "", test_text)
    test_list = jieba.cut(test_text, cut_all=False)
    test_words.append(list(test_list))


##下文急用dump将序列化的对象存储到本地pkl文件中
output = open('../pkl_data/pos_review.pkl', 'wb')
pickle.dump(pos_words, output)
output.close()

output = open('../pkl_data/neg_review.pkl', 'wb')
pickle.dump(neg_words, output)
output.close()

output = open('../pkl_data/test_review.pkl', 'wb')
pickle.dump(test_words, output)
output.close()
