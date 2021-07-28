from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ArticleForm, CommentForm

def blog(request):
    if request.method == 'GET':
        title = 'Блог'
        articles = Article.objects.all()
        comments = Comment.objects.all()
        form = CommentForm()
        context = {
            'title':title,
            'articles':articles,
            'comments':comments,
            'form':form,
        }
        return render(request, 'blog.html', context)
    else:
        form = CommentForm(request.POST)
        if int(request.POST['parent-com-id']) != 0 and form.is_valid():
            form.cleaned_data['article_id'] = request.POST['article-id']
            form.cleaned_data['parent_com'] = request.POST.get('parent-com-id')
            Comment.objects.create(**form.cleaned_data)
            print(form.cleaned_data)
            return redirect('blog')
        else:
            if form.is_valid():
                form.cleaned_data['article_id'] = request.POST['article-id']
                Comment.objects.create(**form.cleaned_data)
                print(form.cleaned_data)
                return redirect('blog')

def create_article(request):
    if request.method == 'GET':
        title = 'Создание статьи'
        form = ArticleForm()
        context = {
            'title': title,
            'form':form
        }
        return render(request, 'create_article.html', context)
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            Article.objects.create(**form.cleaned_data)
            return redirect('blog')


