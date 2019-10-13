from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from blog_index import models
from django.utils.safestring import mark_safe
from utils.page_list import Page
from django import forms
from django.forms import fields
from  django.forms import widgets
from django.db.models import Q
import uuid
import os
from lblog import settings
# Create your views here.
import json
class Fm(forms.Form):
    user = fields.CharField(max_length=20, min_length=3,label="用户名：", error_messages={'required': u'标题不能为空','min_length': u'标题最少为5个字符','max_length': u'标题最多为20个字符'})
    pwd = fields.CharField(max_length=16, min_length=6, error_messages={
        'required': '密码不能为空',
        'min_length': '最低长度不能少于6位',
        'max_length': '最大长度不能大于16位',
    },
        widget = widgets.PasswordInput,
        label="密码："
    )
def index(request):
    p = int(request.GET.get('p', 1))
    for_page_count = 8
    articless = models.Article.objects.filter(category=5).order_by('-is_recommend','-date_publish')
    article = articless[(p-1)*for_page_count:p*for_page_count]
    data_count = len(articless)
    count = 3
    page = Page(data_count,for_page_count,count,p)
    pagestr = page.page_list()
    tags = models.Tag.objects.all()
    links = models.Indexlink.objects.all()

    return render(request, 'index.html', {'article':article, 'tags':tags, 'links':links,'pagestr':pagestr})

def archive(request):
    article = models.Article.objects.filter(category=5).order_by('-is_recommend', '-date_publish')
    tags = models.Tag.objects.all()
    links = models.Indexlink.objects.all()
    return render(request, 'archive.html', {'article': article, 'tags': tags, 'links': links})

def comments(request):
    comment_all = models.Comment.objects.all()
    comment_list = []
    for comment in comment_all:
        for row in comment_list:
            if not hasattr(row, 'child_comment'):
                setattr(row, 'child_comment', [])
            if comment.pid == row:
                print(row.id)
                row.child_comment.append(comment)
                break
        if comment.pid == None:
            comment_list.append(comment)

    tags = models.Tag.objects.all()
    links = models.Indexlink.objects.all()
    return render(request, 'comment.html', {'comment':comment_list, 'tags':tags, 'links':links})

def diary(request):
    if request.session.get('is_login',None):
        article = models.Article.objects.filter(category=4).order_by('-is_recommend', '-date_publish')
        tags = models.Tag.objects.all()
        links = models.Indexlink.objects.all()
        return render(request, 'diary.html', {'article': article, 'tags': tags, 'links': links})
    else:
        return redirect('/login/')

def about(request):
    tags = models.Tag.objects.all()
    links = models.Indexlink.objects.all()
    return render(request, 'about.html', {'tags':tags, 'links':links})

def article(request, a_id):
    article = models.Article.objects.filter(Q(id=a_id)&Q(category=5)).first()
    tags = models.Tag.objects.all()
    links = models.Indexlink.objects.all()
    return render(request, 'article.html', {"article_content":mark_safe(article.content),'article':article, 'tags':tags, 'links':links})

def tags(request, tagid):
    article = models.Article.objects.filter(tag__id=tagid).order_by('-is_recommend', '-date_publish')
    tagss = models.Tag.objects.all()
    links = models.Indexlink.objects.all()
    print(article)
    return render(request, 'tags.html', {'article': article, 'tags': tagss, 'links': links})

def login(request):
    fm = Fm()
    if request.method == 'GET':
        return render(request, 'login.html', {'fm':fm})
    elif request.method == 'POST':
        form = Fm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            pwd = form.cleaned_data['pwd']
            try:
                u = models.User.objects.get(username=user)
                if u.password == pwd:
                    request.session['user'] = user
                    request.session['is_login'] = True
                    request.session.set_expiry(100)
                    return redirect('/diary/')
                else:
                    return redirect('/login/')
            except:
                return redirect('/login/')
        else:
            print(form.errors)
            return render(request, 'login.html', {'error_msg': form.errors, 'fm': fm})

def diary_article(request, did):
    if request.session.get('is_login', None):
        article = models.Article.objects.filter(id=did,category=4).first()
        print(article)
        tags = models.Tag.objects.all()
        links = models.Indexlink.objects.all()
        return render(request, 'diary_article.html', {"article_content":mark_safe(article.content),'article':article,'tags':tags, 'links':links})
    else:
        return redirect('/login/')

def ajax_comment(request):
    ret = {'success':True, 'data': "评论成功！", 'error':None}
    try:
        comment = request.POST.get("comment")
        content = comment.strip()
        if len(content) > 0:
            models.Comment.objects.create(content=content)
        else:
            ret['data'] = "评论失败！"
    except:
        return HttpResponse(json.dumps(ret))
    return HttpResponse(json.dumps(ret))

def find(request):
    find_content = request.POST.get('find_content')
    tags = models.Tag.objects.all()
    links = models.Indexlink.objects.all()
    if len(find_content.strip()) == 0:
        return render(request, 'find.html',{'title': "结果为空", 'tags': tags, 'links': links})

    article = models.Article.objects.filter(Q(title__icontains=find_content) | Q(desc__icontains=find_content) | Q(content__icontains=find_content) ).order_by('-is_recommend', '-date_publish')
    if len(article) == 0:
        return render(request, 'find.html', {'title': "结果为空", 'tags': tags, 'links': links})
    return render(request, 'find.html', {'title': "相关文章如下",'article': article, 'tags': tags, 'links': links})

def upload_img(request):
    dic = {'error':0,'url':'','message':''}
    allow_suffix = ['jpg', 'png', 'jpeg', 'gif', 'bmp']

    files = request.FILES.get('imgFile')
    file_suffix = files.name.split(".")[-1]
    if file_suffix not in allow_suffix:
        dic["error"] = 1
        dic["message"] = "上传格式错误"
        return HttpResponse(json.dumps(dic))
    file_name = str(uuid.uuid1()) + "." + file_suffix
    file_path = os.path.join(settings.MEDIA_ROOT, 'images',file_name)
    file_url = os.path.join(settings.MEDIA_URL, 'images', file_name)

    print(file_url)
    with open(file_path, 'wb') as f:
        print(dic['url'])
        for i in files.chunks():
            f.write(i)
    dic["message"] = "上传成功"
    dic["url"] = file_url
    return HttpResponse(json.dumps(dic))
    # except:
    #     dic["error"] = 1
    #     dic["message"] = "上传失败"
    # return HttpResponse(json.dumps(dic))