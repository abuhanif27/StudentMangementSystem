from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/new/', views.StudentCreateView.as_view(), name='student-create'),
    path('student/<int:pk>/update/', views.StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),
] 