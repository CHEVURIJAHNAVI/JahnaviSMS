from calendar import calendar
from datetime import timedelta
from typing import Any

from django.contrib.auth import authenticate

#from .forms import TaskForm
#from .models import StudentList
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from .models import StudentList, Task


def projecthomepage(request):
    return render(request, "adminapp/ProjectHomePage.html")
def printpagecall(request):
    return render(request, 'adminapp/printer.html')
def printpagelogic(request):
    if request.method=="POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    a1={'user_input': user_input}
    return render(request,'adminapp/Printer.html',a1)
def exceptionpagecall(request):
    return render(request, 'adminapp/print_to_console.html')
from django.shortcuts import render

from django.http import HttpResponse

def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input', '')
        try:
            result = process_user_input(user_input)
            return render(request, 'adminapp/print_to_console.html', {'result': result})
        except Exception as e:
            return render(request, 'adminapp/print_to_console.html', {'error': str(e)})
    return render(request, 'adminapp/print_to_console.html')
def process_user_input(user_input):
    try:
        num = int(user_input)
        result = 10 / num
        return result
    except ZeroDivisionError:
        raise Exception('Cannot divide by zero.')
    except ValueError:
        raise Exception('Invalid input. Please enter a valid number.')
import random
import string
def randompagecall(request):
    return render(request, 'adminapp/randompage.html')
def randomlogic(request):
    if request.method=="POST":
        number1=int(request.POST['number1'])
        ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=number1))
    a1={'ran':ran}
    return render(request, 'adminapp/randompage.html',a1)
def calculatorpagecall(request):
    return render(request, 'adminapp/Calculator.html')

def calculatorlogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/Calculator.html', {'result': result})




from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/RegisterPage.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/RegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/RegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/RegisterPage.html')
    else:
        return render(request, 'adminapp/Register.html')
import datetime
def timepagecall(request):
    return render(request,'adminapp/Datetimewebpage.html')


from datetime import datetime, timedelta
import calendar
from django.shortcuts import render


def timepagelogic(request):
    if request.method == "POST":
        try:
            # Get the input from the form and convert it to an integer
            number1 = int(request.POST['date1'])

            # Get the current date and time
            x = datetime.now()

            # Add the number of days (input by the user) to the current date
            ran = x + timedelta(days=number1)

            # Get the year from the new date
            ran1 = ran.year

            # Check if the year is a leap year
            if calendar.isleap(ran1):
                ran3 = "Leap Year"
            else:
                ran3 = "Not Leap Year"

            # Pass the variables to the template
            context = {'ran': ran, 'ran3': ran3, 'ran1': ran1, 'number1': number1}
            return render(request, 'adminapp/Datetimewebpage.html', context)

        except (ValueError, KeyError):
            # Handle cases where the input is invalid
            return render(request, 'adminapp/Datetimewebpage.html', {'error': 'Invalid input'})

    # Default GET request (for example, render the page with the form)
    return render(request, 'adminapp/Datetimewebpage.html')



def UserLoginPageCall(request):
    return render(request, 'adminapp/LoginPage.html')


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def UserLoginLogic(request) :
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None :
            login(request, user)
            if len(username) == 10 :
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Corrected URL
            elif len(username) == 4 :
                messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Corrected URL
            else :
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/LoginPage.html')
        else :
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/LoginPage.html')
    else :
        return render(request, 'adminapp/LoginPage.html')


from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

def logout(request):
    auth_logout(request)  # Logs out the user
    return redirect('projecthomepage')  # Ensure 'ProjectHomePage' is defined in your urls.py

def student_list(request):
    students = StudentList.objects.all()
    return render(request, 'adminapp/viewstudents.html', {'students': students})
from .forms import StudentForm, TaskForm
from .models import StudentList
from .models import Task
from .forms import TaskForm
def addtaskpagecall(request):
    return render(request,'adminapp/Task.html')





def add_task(request) :
    if request.method == 'POST' :
        form = TaskForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('add_task')
    else :
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/Task.html', {'form' : form, 'tasks' : tasks})

def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('add_task')
def add_student_page_call(request):
    return render(request, 'adminapp/AddStudent.html')
"""def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else: 
        form = StudentForm()
    return render(request, 'adminapp/AddStudent.html', {'form': form})
    """
from django.contrib.auth.models import User
from .models import StudentList
from .forms import StudentForm
from django.shortcuts import redirect, render
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            register_number = form.cleaned_data['Register_Number']
            try:
                user = User.objects.get(username=register_number)
                student.user = user  # Assign the matching User to the student
            except User.DoesNotExist:
                form.add_error('Register_Number', 'No user found with this Register Number')
                return render(request, 'adminapp/add_student.html', {'form': form})
            student.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'adminapp/AddStudent.html', {'form': form})
def student_list_page_call(request):
    return render(request, 'adminapp/viewstudents.html')

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file=request.FILES['file']
        df = pd.read_csv(file, parse_dates=['Date'],dayfirst=True)
        total_sales = df['Sales'].sum()
        average_sales=df['Sales'].mean()
        df['Month']=df['Date'].dt.month
        monthly_sales=df.groupby('Month')['Sales'].sum()
        month_names=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        monthly_sales.index = monthly_sales.index.map(lambda x : month_names[x-1])
        plt.pie(monthly_sales,labels=monthly_sales.index, autopct = '%1.1f%%')
        plt.title('Sales Distribution Per Month')
        buffer = BytesIO()
        plt.savefig(buffer,format='png')
        buffer.seek(0)
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        buffer.close()
        return render(request,'adminapp/chart.html' , {
            'total_sales' : total_sales,
            'average_sales': average_sales,
            'chart': image_data
        })
    return render(request,'adminapp/chart.html',{'form':UploadFileForm()})

from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save feedback to the database
            return redirect('projecthomepage')  # Redirect to a success page (replace with your URL name)
    else:
        form = FeedbackForm()

    return render(request, 'adminapp/Feedbackform.html', {'form': form})
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import StudentList, EmailInvitation
from django.utils import timezone

def send_invitation_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        student_ids = request.POST.getlist('students')  # Assume you're sending student IDs from the form

        # Fetch the students based on selected IDs
        students = StudentList.objects.filter(id__in=student_ids)

        for student in students:
            # Send email to each student's user email
            if student.user and student.user.email:
                send_mail(
                    subject,
                    message,
                    'your_email@example.com',  # Sender's email
                    [student.user.email],      # Recipient's email
                    fail_silently=False,
                )
                # Save email details in the EmailInvitation model (if needed)
                EmailInvitation.objects.create(
                    subject=subject,
                    body=message,
                    sent_at=timezone.now(),
                    student=student,
                )

        messages.success(request, "Invitation emails sent successfully!")
        return redirect('send_invitation_email')  # Redirect after sending emails

    # If GET request, render the form
    students = StudentList.objects.all()  # Fetch all students for form display
    return render(request, 'adminapp/send_invitation.html', {'students': students})
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_instance = form.save(commit=False)
            contact_instance.save()

            # Get the logged-in user
            user_email = request.user.email
            user_first_name = request.user.first_name

            # Prepare email details
            subject = 'New Contact Added'
            message = (
                f'Hello, {user_first_name},\n\n'
                f'A new contact has been added with the following details:\n'
                f'Name: {contact_instance.name}\n'
                f'Email: {contact_instance.email}\n'
                f'Phone Number: {contact_instance.phone_number}\n'
                f'Address: {contact_instance.address}\n\n'  # Updated to address
                f'Thank you!'
            )
            from_email = 'jahnavichevuri@gmail.com'
            recipient_list = [user_email]

            # Send the email
            send_mail(subject, message, from_email, recipient_list)

            return redirect('add_contact')  # Redirect after saving

    else:
        form = ContactForm()

    contacts = Contact.objects.all()
    return render(request, 'adminapp/contact.html', {'form': form, 'contacts': contacts})

from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from .models import Contact

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    # Ensure the user is logged in
    if request.user.is_authenticated:
        # Get the logged-in user's email and first name
        user_email = request.user.email
        user_first_name = request.user.first_name

        # Prepare email details
        subject = 'Contact Deleted'
        message = (
            f'Hello, {user_first_name},\n\n'
            f'The following contact has been deleted:\n'
            f'Name: {contact.name}\n'
            f'Email: {contact.email}\n'
            f'Phone Number: {contact.phone_number}\n'
            f'Address: {contact.address}\n\n'
            f'Thank you!'
        )
        from_email = 'jahnavichevuri@gmail.com'
        recipient_list = [user_email]

        # Send the email before deleting the contact
        send_mail(subject, message, from_email, recipient_list)

    # Delete the contact
    contact.delete()

    return redirect('add_contact')  # Redirect after deletion

# Adjust this to your desired URL after deletion
def add_contact_page_call(request):
    return render(request, 'adminapp/contact.html')