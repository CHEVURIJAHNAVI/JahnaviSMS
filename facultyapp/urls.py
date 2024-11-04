from django.urls import path,include
from . import views
app_name = 'facultyapp'
urlpatterns = [
    path('projecthomepage/',views.projecthomepage,name='projecthomepage'),
    path('FacultyHomePage/',views.FacultyHomePage,name='FacultyHomePage'),
    path('createpost/', views.create_post_page_call, name='createpost'),
    path('createpostlogic/', views.createpost, name='createpostlogic'),
    path('posts_list/', views.post_list, name='post_list'),  # URL for listing all posts
    path('post_detail/<slug:slug>/', views.post_detail, name='post_detail'),
    path('add_course', views.add_course, name='add_course'),
path('addcoursepagecall', views.add_course_page_call, name='addcoursepagecall'),
    path('viewstudents', views.view_student_list, name='viewstudents'),
path('postmarks', views.post_marks, name='postmarks'),
]