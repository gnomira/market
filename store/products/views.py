 # импортируем модель для CBV            
from django.views import generic
from django.views.generic import TemplateView

  # импортируем нашу модель
from .models import Product,Category,Order
#для создания пользователя
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse,reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import generics, serializers 
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .serializers import ProductSerializer
from rest_framework import permissions

class IndexView(generic.ListView): 
    template_name = 'products_list.html' 
    context_object_name = 'products' 
    model = Product 

    # метод для добавления дополнительной информации в контекст
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        # передаем в словарь контекста список всех категорий 
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        products = Product.objects.all()
        # Отбираем первые 10 статей
        paginator = Paginator(products, 10)
        page = self.request.GET.get('page')
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            products = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            products = paginator.page(paginator.num_pages)
        return products

class ProductDetail(generic.DetailView): 
    template_name = 'product_detail.html' 
    model = Product

class CategoryDetail(generic.DetailView): 
    template_name = 'сategory_detail.html' 
    model = Category

# форма заказа
class OrderFormView(generic.CreateView): 
    model = Order 
    template_name = 'order_form.html' 
    success_url = '/thanks/' 
    # выведем только поля, которые нужно заполнить самому человеку
    fields = ['customer_name', 'customer_phone','customer_email']
   
    def form_valid(self, form):
        # получаем ID из ссылки и передаем в ORM для фильтрации
        product = Product.objects.get(id=self.kwargs['pk']) 
        # передаем в поле товара нашей формы отфильтрованный товар
        user = self.request.user 
        if  self.request.user.is_authenticated:
            form.instance.user=user
        form.instance.product = product 
        # super — перезагружает форму, нужен для работы
        return super().form_valid(form)

#для создания пользователя
class SignUpView(generic.CreateView): 
    form_class = UserCreationForm 
    success_url = reverse_lazy('login') 
    template_name = 'signup.html'


class OrderThanks(TemplateView): 
    template_name = 'order_thanks.html' 
    # метод для добавления дополнительной информации в контекст
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        # передаем в словарь контекста список всех категорий 
        context['categories'] = Category.objects.all()
        return context
  
class ProductListAPI(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer)
    permission_classes = (permissions.IsAdminUser)
    #serializer_class = ProductSerializer

"""
 # наш секретный Вью
class SecretAdminView(UserPassesTestMixin, generic.TemplateView):
    # секретное содержимое
    template_name = 'memes.html'

    # проверяем условие, если пользователь — админ, то вернет True и пустит пользователя
    def test_func(self): 
        return self.request.user.is_superuser

# форма создания продукта           
class ProductCreate(generic.CreateView): 
    model = Product 
     # название нашего шаблона с формой
    template_name = 'product_new.html' 
    # какие поля будут в форме 
    fields = '__all__'

"""