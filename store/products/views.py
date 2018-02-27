 # импортируем модель для CBV            
from django.views import generic 

  # импортируем нашу модель
from .models import Product
from .models import Category
from django.views.generic import TemplateView

class IndexView(generic.ListView): 
    template_name = 'products_list.html' # подключаем наш Темплейт
    context_object_name = 'products' # под каким именем передадутся данные в Темплейт
    model = Product # название Модели

class ProductDetail(generic.DetailView): 
    template_name = 'product_detail.html' 
    model = Product

class CategoryDetail(generic.DetailView): 
    template_name = 'сategory_detail.html' 
    model = Category

"""
class HomePageView(TemplateView):
    template_name = 'home.html'
 
class WomenPageView(TemplateView):
    template_name = 'women.html'

class MenPageView(TemplateView):
    template_name = 'men.html'

class ChildrenPageView(TemplateView):
    template_name = 'children.html'
"""