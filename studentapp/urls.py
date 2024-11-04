from django.urls import path,include
from . import views
app_name = 'studentapp'
urlpatterns = [
    path('name/',views.name,name='name'),
    path('StudentHomePage/',views.StudentHomePage,name='StudentHomePage'),
    path('viewmarks/', views.view_marks, name='viewmarks'),
]
