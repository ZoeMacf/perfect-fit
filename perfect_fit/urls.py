from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('faq/', include('faq.urls')),
    path('about_us/', include('about_us.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),

]
