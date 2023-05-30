
from django.contrib import admin
from django.urls import path
from urunler.views import *
from user.views import *


urlpatterns = [
    path('', index, name='index'),
    path('urun/<int:urunId>', urun, name='urun'),
    path('admin/', admin.site.urls),
    path('register/', userRegister, name='register'),
    path('olustur/', olustur, name='olustur'),
    path('sepet/', sepet, name='sepet'),
    path('odeme/', payment, name='payment'),
    path('result/', result, name='result'),
    path('success/', success, name='success'),
    path('fail/', fail, name='failure')

]
