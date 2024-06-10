from .views import handler404
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
    path('puzzle_exchange/', include('puzzle_exchange.urls')),
    path('profile/', include('users.urls')),

]

handler404 = 'perfect_fit.views.handler404'