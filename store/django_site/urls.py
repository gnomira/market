# стандартный вью для админки
from django.contrib import admin
# модуль Джанго для определения урлов
from django.urls import path 
# импортируем наш файл views из products
from products import views 
  
# говорим Джанго о том, что хотим отображать наш вью на главной странице
urlpatterns = [ 
  path('', views.IndexView.as_view(),name='index'), 
  path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
  path('products/new/', views.ProductCreate.as_view(), name='product_create'),
  path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category'),
  path('products/<int:pk>/order', views.OrderFormView.as_view(), name='product_order'),
  path('admin/', admin.site.urls), 
    #path('', views.HomePageView.as_view(), name='home'),
    #path('women/', views.WomenPageView.as_view(), name='women'),
    #path('men/', views.MenPageView.as_view(), name='men'),
    #path('children/', views.ChildrenPageView.as_view(), name='children'),


  ]