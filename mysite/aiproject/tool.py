import jieba
import jieba.analyse
import os
import docx
import pathlib

def key_word():#產生關鍵詞list
    path = str(pathlib.Path(__file__).parent.absolute()).replace("\\","/")
    with open(path+"/關鍵詞.txt", "r", encoding="utf-8") as file:
        keys = file.read()
    key_list = list()
    keys = keys.split('\n')
    for i in keys:
        key_list.append(i)
    return key_list
    
def key_find(filename, chi_title):
    path_this = str(pathlib.Path(__file__).parent.absolute()).replace('\\','/')
    path = path_this+'/'+filename
    
    jieba.load_userdict(path_this+'/userdict.txt')
    jieba.analyse.set_stop_words(path_this+'/stop.txt')
    doc = docx.Document(path+"/"+chi_title+".docx")
    content = ""
    for para in doc.paragraphs:
        content+=str(para.text)
    content = str(content)
    tags = jieba.analyse.extract_tags(content, topK=20, withWeight=True)
    key_list = list()
    for tag in tags:
        key_list.append(tag[0])
    return key_list