 # импортируем модель для CBV            
from django.views import generic 

  # импортируем нашу модель
from .models import Product,Category,Order
from django.urls import reverse

class IndexView(generic.ListView): 
    template_name = 'products_list.html' 
    context_object_name = 'products' 
    model = Product 

class ProductDetail(generic.DetailView): 
    template_name = 'product_detail.html' 
    model = Product

class CategoryDetail(generic.DetailView): 
    template_name = 'сategory_detail.html' 
    model = Category

"""
class ProductList(generic.ListView): 
    template_name = 'product_list.html' 
    # добавляем объекты модели в контекст под этим именем
    context_object_name = 'products' 
    model = Product
    # метод для добавления дополнительной информации в контекст
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        # передаем в словарь контекста список всех категорий 
        context['categories'] = Category.objects.all()
        return context
"""

# форма создания продукта           
class ProductCreate(generic.CreateView): 
    model = Product 
     # название нашего шаблона с формой
    template_name = 'product_new.html' 
    # какие поля будут в форме 
    fields = '__all__'

# форма заказа
class OrderFormView(generic.CreateView): 
    model = Order 
    template_name = 'order_form.html' 
    success_url = 'success_url.html' 
    # выведем только поля, которые нужно заполнить самому человеку
    fields = ['customer_name', 'customer_phone']
    def form_valid(self, form):
        # получаем ID из ссылки и передаем в ORM для фильтрации
        product = Product.objects.get(id=self.kwargs['pk']) 
        # передаем в поле товара нашей формы отфильтрованный товар
        form.instance.product = product 
        # super — перезагружает форму, нужен для работы
        return super().form_valid(form)