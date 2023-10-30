
from django.contrib import admin
from django.urls import path,include # new
from myapp.views import TestView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # new
    path('', TestView.as_view(),name='test'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
