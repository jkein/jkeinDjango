# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import Article, Category
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

def allitems(request):
    cats = Category.objects.all().order_by("name")
    articlesall = Article.objects.all().order_by("-published")
    
    paginator = Paginator(articlesall, 3)
    
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try: articlesall = paginator.page(page)
    except (InvalidPage, EmptyPage): articlesall = paginator.page(paginator.num_pages)
    
    return render_to_response ('all.html', { 'articlesall': articlesall, 
                                            'cats': cats },
                               context_instance=RequestContext(request))

def categoryview(request, name_slug):
    category = get_object_or_404(Category, name_slug=name_slug)
    category_news_items = Article.objects.filter(cat=name_slug)
    return render_to_response('category.html', { 'category': category, 
                                                'category_news_items': category_news_items},
                              context_instance=RequestContext(request))
    
def articledetail(request, slug):
    article_details = get_object_or_404(Article, slug=slug)
    categories_all = Category.objects.order_by("name")
    return render_to_response('blog_details.html', {'article_details': article_details,
                                                    'categories_all': categories_all},
                              context_instance=RequestContext(request))