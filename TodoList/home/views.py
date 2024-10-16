from django.shortcuts import render, redirect, HttpResponse
from home.models import Task
from home.models import Contact
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.

#Index page/Add tasks page
def home(request):
    if request.method == "POST":
     #Handle the form
      title = request.POST['title']
      desc = request.POST['desc']
      print(title, desc)

      if len(title)==0 or len(desc)==0:
            messages.error(request, 'Please: Fill the form correctly!')
      else:
            ins = Task(taskTitle=title, taskDesc=desc)
            ins.save()
            messages.success(request, 'Your task has been added to the list.')
    print('You are : ' , request.session.get('loginusername'))
    return render(request, 'index.html')


#Tasks page/View tasks page
def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    context['count'] = context['tasks'].filter(completed=False).count()
    return render(request, 'tasks.html', context)


#For delete a task
def delete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    messages.error(request, 'Task deleted successfully.')
    return redirect('tasks')


#contact us page
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)

        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please: Fill the form correctly!')
        else:
            contact = Contact(nm=name, em1=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has been successfully sent.')

    return render(request, 'contact.html')


#Status for completed tasks
def complete(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = False
    task.save()
    return redirect('tasks')


#Status for pending tasks
def pending(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('tasks')


#For signup users
def handlesignup(request):
    if request.method == 'POST':
        #get the post parameters
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        print(fname, lname, email, username, pass1, pass2)

        #check for errorneous inputs
        if len(username) > 10:
            messages.error(request, 'UserName must be unser 10 characters.')
            return redirect('handlesignup')
        if pass1 != pass2:
            messages.error(request, 'Password do not match.')
            return redirect('handlesignup')
        if not username.isalnum():
            messages.error(request, 'UserName should only contain latters and numbers.')
            return redirect('handlesignup')

        #create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your ToDos account has been successfully created.')
        
    return render(request, 'signup.html')
    

#For Login Users
def handlelogin(request):
     if request.method == 'POST':
        #get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        print(loginusername, loginpassword)

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            request.session['loginusername'] = loginusername
            request.session['loginpassword'] = loginpassword

            messages.success(request, 'Successfully Logged In.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials, Please try again.')
            return redirect('handlelogin')

     return render(request, 'login.html')

 
#For Logout Users
def handlelogout(request):
        logout(request)
        messages.success(request, 'Successfully Logged Out.')
        return redirect('handlelogin')
