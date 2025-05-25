from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, BookIssue
from django.contrib import messages
# Create your views here.
from django.shortcuts import render
from .models import Program, Branch, Subject, Bookstore
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail
from django.utils.timezone import now
from django.shortcuts import render
from .models import Book
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book

# Home Page
def home(request):
    return render(request, 'home.html')
def Contact(request):
    return render(request, 'Contact.html')
# Registration View
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered!")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registration successful! Please log in.")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match!")
    return render(request, 'register.html')


# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password!")
    return render(request, 'login.html')


# Dashboard View
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard.html', {'user': request.user})


# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')



def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        form = PasswordResetForm({'email': email})
        if form.is_valid():
            form.save(request=request)  # This sends the password reset email
            messages.success(request, f"Password reset link sent to {email}")
        else:
            messages.error(request, "No user found with this email address!")
    else:
        form = PasswordResetForm()
    
    return render(request, 'forgot_password.html', {'form': form})

def dashboard(request):
    programs = Program.objects.all()
    branches = Branch.objects.all()
    subjects = Subject.objects.all()
    books = Bookstore.objects.all()
    return render(request, 'library/dashboard.html', {
        'programs': programs,
        'branches': branches,
        'subjects': subjects,
        'books': books,
    })
# views.py


def issue_book(request, book_id):
    # Get the book object
    book = get_object_or_404(Book, id=book_id)

    # Check if the book is available
    if book.is_available:
        book.is_available = False  # Mark as not available
        book.save()
        messages.success(request, f"You have successfully issued the book: {book.title}")
    else:
        messages.error(request, "This book is not available.")

    # Redirect to the available books page
    return redirect('available_books')

def available_books(request):
    # Retrieve all books
    books = Book.objects.all()
    return render(request, 'available_books.html', {'books': books})


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})


@login_required
def issue_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.is_available:
        # Mark the book as issued
        BookIssue.objects.create(user=request.user, book=book)
        book.is_available = False
        book.save()
        messages.success(request, f"You have successfully issued {book.title}.")
    else:
        messages.error(request, f"Sorry, {book.title} is already issued.")
    return redirect('book_list')


@login_required
def issued_books(request):
    issued_books = BookIssue.objects.filter(user=request.user)
    return render(request, 'library/issued_books.html', {'issued_books': issued_books})

@login_required
def return_book(request, issue_id):
    try:
        book_issue = BookIssue.objects.get(id=issue_id, user=request.user)
        book = book_issue.book
        book.is_available = True  # Mark the book as available
        book.save()
        book_issue.return_date = now()  # Set the return date to current date
        book_issue.save()
        messages.success(request, f"You have successfully returned {book.title}.")
    except BookIssue.DoesNotExist:
        messages.error(request, "Invalid request. You can't return this book.")
    return redirect('issued_books')
def book_list(request):
    books = Book.objects.filter(is_available=True)
    return render(request, 'books/book_list.html', {'books': books})
# Serve PDFs only for logged-in admins
from django.http import HttpResponseForbidden

def view_pdf(request, book_id):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to access this file.")
    # Logic to stream the file can be added here
