from django.urls import path, include

from . import views

urlpatterns = [
    path('post_list/', views.PostListView.as_view(), name="post_list"),
    path('post_list/<int:pk>/', views.PostDetailView.as_view(), name="post_detail"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name=""),
    path("signup/", views.SignUp.as_view(), name="signup"),
]
