from django.urls import path
from website import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='home'),
]
