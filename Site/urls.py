from django.urls import path
from Site import views
urlpatterns = [
    path('Site', views.Site, name='site')
]