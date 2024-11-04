from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.projecthomepage,name='projecthomepage'),
    path('printpagecall/',views.printpagecall, name='printpagecall'),
    path('printpagelogic/',views.printpagelogic, name='printpagelogic'),
    path('randompagecall/',views.randompagecall, name='randompagecall'),
    path('randomlogic/',views.randomlogic, name='randomlogic'),
    path('calculatorpagecall/', views.calculatorpagecall, name='calculatorpagecall'),path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('timepagecall/',views.timepagecall,name='timepagecall'),
    path('timepagelogic/',views.timepagelogic,name='timepagelogic'),
    path('addtaskpagecall/',views.addtaskpagecall,name='addtaskpagecall'),
    path('add_task/',views.add_task,name='add_task'),
    path('<int:pk>/delete/',views.delete_task,name='delete_task'),
    path('UserRegisterPageCall/',views.UserRegisterPageCall,name='UserRegisterPageCall'),
    path('UserRegisterLogic/',views.UserRegisterLogic,name='UserRegisterLogic'),
    path('exceptionpagecall/',views.printpagecall, name='exceptionpagecall'),
    path('exceptionlogic/',views.printpagelogic, name='exceptionpagelogic'),
    path('UserLoginLogic',views.UserLoginLogic,name='UserLoginLogic'),
    path('UserLoginPagecall',views.UserLoginPageCall,name='UserLoginPageCall'),
    path('student_list',views.student_list,name='student_list'),
    path('add_student',views.add_student,name='add_student'),
    path('add_student_page_call',views.add_student_page_call,name='add_student_page_call'),
    path('student_list_page_call',views.student_list_page_call,name='student_list_page_call'),
path('logout',views.logout,name='logout'),
path('uploadfile',views.upload_file,name='uploadfile'),
path('feedback',views.feedback_view,name='feedback'),
path('sendinvitation',views.send_invitation_email,name='sendinvitation'),
path('addcontactpagecall/',views.add_contact_page_call,name='addcontactpagecall'),
path('add_contact/', views.add_contact, name='add_contact'),
    path('<int:pk>/delete/', views.delete_contact, name='delete_contact'),
]