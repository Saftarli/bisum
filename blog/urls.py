
from django.urls import path
from blog.views import blog ,detail

urlpatterns = [
    path('',blog, name='x'),
    path('detail', detail, name='detail')
]
