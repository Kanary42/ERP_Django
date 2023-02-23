from django.urls import path

from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView,
                    PlanView,
                    DayTaskSheetCreateView,
                    DayTaskSheetDetailView,
                    DayTaskSheetListView,
                    DayTaskCreateView,
                    daytask,
                    HomeView)

urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('plan/', PlanView.as_view(), name='plan'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('daytasksheet/new/', DayTaskSheetCreateView.as_view(), name='daytasksheet-create'),
    path('daytasksheet/<int:pk>/', DayTaskSheetDetailView.as_view(), name='daytasksheet-detail'),
    path('daytasksheet/<int:sheet_id>/daytask/new', daytask, name='daytask-create'),
    path('daytasksheet_list/', DayTaskSheetListView.as_view(), name='daytasksheet-list'),
    path('about/', views.about, name='blog-about'),
]
