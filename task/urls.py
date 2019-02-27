from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from users import api

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('users.urls')),

    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/users/', api.UserListCreateAPI.as_view(), name='user_list'),
    path('api/v1/users/<pk>/', api.UserRetrieveUpdateDestroyAPI.as_view(), name='user_detail'),
]
