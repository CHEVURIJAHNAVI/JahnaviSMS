from django import forms
from .models import BlogPost,AddCourse,Marks


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'pub_date']  # Fields to include in the form

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = ['student','course','section']
class MarksForm(forms.ModelForm):
    class Meta:
        model=Marks
        fields='student','course','marks'


