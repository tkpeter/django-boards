"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path

from boards import views
from accounts import views as account_views

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),
    path('boards/<int:pk>/new', views.new_topic, name='new_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>', views.topic_posts, name='topic_posts'),
    path('boards/<int:pk>/topics/<int:topic_pk>/reply', views.reply_topic, name='reply_topic'),
    path('boards/<int:pk>/topics/<int:topic_pk>/post/<int:post_pk>', views.PostUpdateView.as_view(), name='edit_post'),
    path('signup', account_views.signup, name='signup'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('login', auth_views.LoginView.as_view(template_name='login.html') , name='login'),
    path('reset', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('admin/', admin.site.urls),
    #path('homepage/', views.home, name='home')
]
