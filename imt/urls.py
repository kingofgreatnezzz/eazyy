from django.urls import path, include
from django.contrib.auth import views as auth_views
from .import views






# post views
urlpatterns = [
  
    path("index/",views.index, name='index'),
    path('', include('django.contrib.auth.urls')),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),

    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),   
    path("signup/", views.register, name='signup'),

    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),  
    path("work/", views.work, name='work'), 
    path("exam/", views.exam, name='exam'),
    path("project/", views.project, name='project'),
    path("PD/", views.PD, name='PD'),
    path("terms_condition/", views.terms_condition, name='terms_condition'), 
    
    ]

