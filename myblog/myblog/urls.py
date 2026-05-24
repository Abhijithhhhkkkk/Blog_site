from django.urls import path,include
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += [
    path('', include('blog.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]

