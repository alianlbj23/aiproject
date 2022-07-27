from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from aiproject.models import Member
from .models import *
import os
import sys
sys.path.append('aiproject')
import tool


def home(request):
    members = Member.objects.all()
    articles = Article.objects.all()
    return render(request, 'index.html', locals())

def article_list(request,mod):
    if mod == 0:
        articles = Article.objects.all()
    elif mod == 1:
        articles = AI_Article.objects.all()
    return render(request, 'article_list.html', locals())

def article_list_tag(request, tag):
    tag_list = list()
    tag_list.append(tag)
    tag_list = set(tag_list)
    slide_pk = slide_article_pk(tag_list)
    articles = Article.objects.filter(pk__in=slide_pk[0])
    ai_articles = AI_Article.objects.filter(pk__in=slide_pk[1])
    return render(request, 'article_list_tag.html', locals())
    
from pydocx import PyDocX
import pathlib
def dataOutput(information,range1, range2):
    left = information.find(range1)
    information = information[left+len(range1):]
    right = information.find(range2)
    target = information[:right]
    target = target.strip()
    Updateinformation = information[right:]
    return target,Updateinformation

def slide_article_pk(target_set):
    target_set = set(target_set)
    articles = Article.objects.all()
    ai_articles = AI_Article.objects.all()
    pk_list = list()
    ai_pk_list = list()
    for j in articles:
        tmp = Article.objects.filter(pk=j.pk)
        article_title = str(list(tmp.values('Chi_title'))[0]['Chi_title'])
        article_tag = set(tool.key_find("word_read",article_title))
        if len(list(article_tag & target_set)) != 0:
            pk_list.append(j.pk)

    for j in ai_articles:
        tmp = AI_Article.objects.filter(pk=j.pk)
        article_title = str(list(tmp.values('Chi_title'))[0]['Chi_title'])
        article_tag = set(tool.key_find("ai_word_read",article_title))
        if len(list(article_tag & target_set)) != 0:
            ai_pk_list.append(j.pk)
    
    return [pk_list,ai_pk_list]
from django.utils.safestring import mark_safe
def article_read(request,mod,pk):
    if mod == 0:
        article_tmp = Article.objects.filter(pk=pk)
        file_name = "word_read"
        # articles = Article.objects.all()
    elif mod == 1:
        article_tmp = AI_Article.objects.filter(pk=pk)
        file_name = "ai_word_read"
        # ai_articles = AI_Article.objects.all()
    article_title = str(list(article_tmp.values('Chi_title'))[0]['Chi_title'])
    article_title_eng = str(list(article_tmp.values('Eng_title'))[0]['Eng_title'])
    article_editor = str(list(article_tmp.values('Editor'))[0]['Editor'])
    article_url = str(list(article_tmp.values('Data_url'))[0]['Data_url'])
    path = str(pathlib.Path(__file__).parent.absolute()).replace('\\','/')
    
    path = path+"/"+file_name+"/"+str(article_title)+".docx"
    print("@@@@@@@@@@@@@@@@", path)
    html = PyDocX.to_html(path)
    with open("test.html", 'w', encoding="utf-8") as f:
        f.write(html)
    with open("test.html", 'r', encoding="utf-8") as f:
        html_data = f.read()
    body_html, html_data = dataOutput(html_data,"<body>", "</body>")
    print("!!!!!!!!!!!",article_url)
    body_html = mark_safe(body_html)
    all_keys = set(tool.key_word())
    article_tag = set(tool.key_find(file_name,article_title))
    tags = list(all_keys & article_tag)
    slide_pk = slide_article_pk(tags)
    articles = Article.objects.filter(pk__in=slide_pk[0])
    ai_articles = AI_Article.objects.filter(pk__in=slide_pk[1])
    return render(request, 'tool.html', locals())
