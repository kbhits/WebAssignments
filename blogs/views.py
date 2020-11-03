from django.shortcuts import render
from .models import Topic, Entry, Introduce, IntroduceTitle
from .forms import TopicForm, EntryForm

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    #主页视图
    return render(request, 'blogs/index.html')

def topics(request):
    #显示所有评论
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'blogs/topics.html', context)

def topic(request, topic_id):
    #显示单个评论的内容
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'blogs/topic.html', context)

def new_topic(request):
    #添加新的回复
    if request.method != 'POST':
        #未提交数据，创建一个新的表单
        form = TopicForm()
    else:
        #POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:topics'))
    context = {'form':form}
    return render(request, 'blogs/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('blogs:topic', args=[topic_id]))
    context = {'topic':topic, 'form':form}
    return render(request, 'blogs/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:topic', args=[topic.id]))
    context = {'entry':entry, 'topic':topic, 'form':form}
    return render(request, 'blogs/edit_entry.html', context)