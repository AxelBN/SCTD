"""SCTD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Tracking import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index.html/', views.index),
    path('', views.index),
    path('tracking_list.html/', views.document_list.as_view(template_name="tracking_list.html"), name='documents'),
    path('tracking_list.html/tracking.html/', views.tracking),
    path('tracking_list.html/update_documents.html/<int:pk>', views.update_document.as_view(template_name="update_documents.html"), name='Update'),
    path('tracking_list.html/delete_document.html/<int:pk>', views.delete_document.as_view(template_name="delete_document.html", success_url="/tracking_list.html"), name='delete'),
]

urlpatterns += staticfiles_urlpatterns()