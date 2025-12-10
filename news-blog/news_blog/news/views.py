from django.views.generic import ListView, DetailView
from .models import Article
from django.shortcuts import render

# def index(request):
#     return render(
#         request, 
#         'index.html',
#         context={'who': 'World'})

class ArticleListView(ListView):
    model = Article 
    template_name = 'news/index.html'
    context_object_name = 'articles'
    
    def get_queryset(self):
        queryset = Article.objects.filter(is_published=True).order_by('-created_at')
        q = self.request.GET.get('q')
        if q:
            queryset = queryset.filter(title__icontains=q)
        return queryset
    
    

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/detail.html'
    context_object_name = 'article'