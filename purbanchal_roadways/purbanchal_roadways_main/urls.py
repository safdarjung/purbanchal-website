"""
URL configuration for purbanchal_roadways project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
admin.site.site_header = "PURBANCHAL ROADWAYS Admin"
admin.site.site_title = "PURBANCHAL ROADWAYS Admin Portal"
admin.site.index_title = "Welcome to PURBANCHAL ROADWAYS Portal"
from django.conf import settings
from django.conf.urls.static import static

from core import views as core_views
from services import views as service_views
from contact import views as contact_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name='home'),
    path('about/', core_views.about, name='about'),
    path('services/', service_views.service_list, name='services'),
    path('services/<int:service_id>/', service_views.service_detail, name='service_detail'),
    path('contact/', contact_views.contact, name='contact'),
    path('pricing/', core_views.pricing, name='pricing'),
    path('faq/', core_views.faq, name='faq'),
    path('privacy-policy/', core_views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', core_views.terms_of_service, name='terms_of_service'),
    path('write-review/', core_views.write_review, name='write_review'),
    path('write-review/<str:category>/', core_views.write_review, name='write_review_category'),
    path('custom-quote/', core_views.custom_quote, name='custom_quote'),
    path('payment/', core_views.payment, name='payment'),
    path('learn-more/', core_views.learn_more, name='learn_more'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
