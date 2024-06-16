from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

from .views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('faq/', include('faq.urls')),
    path('about_us/', include('about_us.urls')),
    path('contact_us/', include('contact_us.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('puzzle_exchange/', include('puzzle_exchange.urls')),
    path('users/', include('users.urls')),
    path('user_msgs/',include('user_msgs.urls'))

]

handler404 = 'perfect_fit.views.handler404'