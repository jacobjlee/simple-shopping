from django.urls import path

from .views import CreateUserView, ManageUserView

app_name = 'users'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('me/', views.ManageUserView.as_view(), name='me')
]
