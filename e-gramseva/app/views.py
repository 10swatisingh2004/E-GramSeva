from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import CustomUser, Service, Application

# Helper to check user roles
def is_officer(user):
    return user.role == 'officer'

def is_staff(user):
    return user.role == 'staff'

def is_user(user):
    return user.role == 'user'

# 1. Home View
def home(request):
    return render(request, 'index.html')
def home1(request):
    return render(request , 'home.html')
# 2. Register View (without form)
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')
        if username and password and role:
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                user = CustomUser.objects.create_user(username=username, password=password, role=role)
                user.save()
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')
        else:
            messages.error(request, 'All fields are required.')
    return render(request, 'register.html')

# 3. Login View (without form)
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home1')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# 4. Logout View
@login_required
def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

# 5. Services List View

def services(request):
    all_services = Service.objects.all()
    return render(request, 'services.html', {'services': all_services})

# 6. Apply for a Service (User)
@login_required
@user_passes_test(is_user, login_url='home')
def apply_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    Application.objects.create(user=request.user, service=service, status='pending')
    messages.success(request, 'Application submitted successfully.')
    return redirect('my_applications')

# 7. My Applications View (User)
@login_required
@user_passes_test(is_user, login_url='home')
def my_applications(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'my_applications.html', {'applications': applications})

# 8. Create Service View (Officer, without form)
@login_required
@user_passes_test(is_officer, login_url='home')
def create_service(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')  # Get the uploaded image
        if name and description:
            Service.objects.create(name=name, description=description, created_by=request.user, image=image)
            messages.success(request, 'Service created successfully.')
            return redirect('home')
        else:
            messages.error(request, 'All fields are required.')
    return render(request, 'create_service.html')


# 9. Staff Applications Management View
def is_staff_or_officer(user):
    return user.is_authenticated and user.role in ['staff', 'officer']

@login_required
@user_passes_test(is_staff_or_officer, login_url='home')  # Allow staff and officers
def staff_applications(request):
    applications = Application.objects.all().select_related('service', 'user')
    
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        status = request.POST.get('status')
        if application_id and status:
            application = get_object_or_404(Application, id=application_id)
            application.status = status
            application.save()
            messages.success(request, 'Application status updated successfully.')
        else:
            messages.error(request, 'Application ID and status are required.')
    
    return render(request, 'staff_applications.html', {'applications': applications})

@login_required
@user_passes_test(is_officer, login_url='home')  # Restrict to officers
def update_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')  # Optional: check if a new image is uploaded

        if name and description:
            service.name = name
            service.description = description
            if image:  # Update image only if a new one is provided
                service.image = image
            service.save()
            messages.success(request, 'Service updated successfully.')
            return redirect('services')
        else:
            messages.error(request, 'All fields are required.')

    return render(request, 'update_service.html', {'service': service})
@login_required
@user_passes_test(is_officer, login_url='home')  # Restrict to officers
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        service.delete()
        messages.success(request, 'Service deleted successfully.')
        return redirect('services')

    return render(request, 'confirm_delete_service.html', {'service': service})
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Application

def is_staff_or_officer(user):
    return user.is_authenticated and user.role in ['staff', 'officer']

@login_required
@user_passes_test(is_staff_or_officer, login_url='home')  # Restrict to staff and officers
def update_application_status(request, application_id):
    if request.method == 'POST':
        application = get_object_or_404(Application, id=application_id)
        status = request.POST.get('status')
        if status in ['pending', 'approved', 'rejected']:
            application.status = status
            application.save()
            messages.success(request, 'Application status updated successfully.')
        else:
            messages.error(request, 'Invalid status value.')
    return redirect('staff_applications')
