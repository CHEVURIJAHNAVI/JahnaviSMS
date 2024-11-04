import pytz
from django import forms
from django.shortcuts import redirect, render

from .models import StudentList, FeedbackForm
import pytz
from django import forms
from .models import Task
#It will resuce the lines of code in HTML file and views.py.When the no.of parametres in more we can use forms.py This file is not mandatory
# is_valid() - Checks the form whether all the fields are filled or not in the form
# form.save() - saves the information in the database
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentList
        fields = ['Register_Number', 'Name']

class UploadFileForm(forms.Form):
    file = forms.FileField()
    from django import forms
    from .models import FeedbackForm

class FeedbackForm(forms.ModelForm) :
    class Meta :
        model = FeedbackForm
        fields = ['name', 'email', 'mobile', 'comments']
        widgets = {
            'name' : forms.TextInput(attrs={'placeholder' : 'Your name', 'class' : 'form-control'}),
            'email' : forms.EmailInput(attrs={'placeholder' : 'Your email', 'class' : 'form-control'}),
            'mobile' : forms.TextInput(attrs={'placeholder' : 'Your mobile number', 'class' : 'form-control'}),
            'comments' : forms.Textarea(
                attrs={'placeholder' : 'Your comments', 'class' : 'form-control', 'rows' : 5}),
        }
        labels = {
            'name' : 'Name',
            'email' : 'Email',
            'mobile' : 'Mobile Number',
            'comments' : 'Comments (max 150 characters)',
        }

    def clean_mobile(self) :
        mobile = self.cleaned_data.get('mobile')
        if len(mobile) != 10 or not mobile.isdigit() :
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        return mobile-0


from django import forms
from .models import StudentList


class EmailInvitationForm(forms.Form) :
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Subject',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Write your message here...',
        'rows' : 4,
    }))

    students = forms.ModelMultipleChoiceField(
        queryset=StudentList.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select Students"
    )
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address']
