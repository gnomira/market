from django.contrib import admin
# модуль Джанго для определения урлов
from django.urls import path, include
# импортируем наш файл views из products
from products import views 

from django.conf import settings
from django.conf.urls.static import static

  
# говорим Джанго о том, что хотим отображать наш вью на главной странице
urlpatterns = [ 
  path('', views.IndexView.as_view(),name='index'), 
  path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
  #path('products/new/', views.ProductCreate.as_view(), name='product_create'),
  path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
  path('products/<int:pk>/order', views.OrderFormView.as_view(), name='product_order'),
  path('signup/', views.SignUpView.as_view(), name='signup'),
  path('thanks/', views.OrderThanks.as_view(), name='order_thanks'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('admin/', admin.site.urls), 

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


