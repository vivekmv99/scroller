from django.shortcuts import render
from . models import *
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage

def index(request):
    # blog = Blog.objects.all()
    return render(request,'index.html',)

def loader_fn(request):
    start = int(request.GET.get('start'))
    limit = int(request.GET.get('limit'))
    print(start,limit)
    blog = Blog.objects.all().order_by('-id')[start:limit]

    # p = Paginator(blog, 4)
    page_num = request.GET.get('page', 1)
    # try:
    #     page = p.page(page_num)
    # except EmptyPage:
    #     page = p.page(1)

    template = loader.get_template('blog.html')
    context = {
        'blog': blog,
    }
    return HttpResponse(template.render(context, request))

def new(request):
    blog = Blog.objects.all().order_by('-id')
    p = Paginator(blog, 4)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    return render(request,'new.html',{'blog':page})