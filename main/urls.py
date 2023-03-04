from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('service/', service, name='service'),
    path('features/', features, name='features'),
    path('user/', user, name='user'),
    path('pricing/', pricing, name='pricing'),
    path('faq/', faq, name='faq'),
    path('blog/', blog, name='blog'),
]