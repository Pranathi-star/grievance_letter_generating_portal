"""smc_grievances URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from smc import views as smc_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('smc_register/', smc_views.register_smc, name='smc_register'),
    path('login/', auth_views.LoginView.as_view(template_name='smc/smc_login.html'), name='smc_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='smc/smc_logout.html'), name='smc_logout'),
    path('', smc_views.project_home, name='project_home'),
    path('about/', smc_views.project_about, name='project_about'),
    path('grievance_form/', smc_views.grievance_form, name = 'grievance_form'),
    path('new_grievance/', smc_views.new_grievance, name = 'new_grievance'),
    path('view_letter/', smc_views.ViewPDF.as_view(), name = 'view_letter'),
    path('raise_grievance/', smc_views.raise_grievance, name = 'raise_grievance'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
