from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='book_images/')
    is_available = models.BooleanField(default=True)  # Tracks availability

    def __str__(self):
        return self.title

class BookIssue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} issued to {self.user.username}"

class Program(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Enquiry(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry from {self.student.name}"

class StudentResponse(models.Model):
    enquiry = models.OneToOneField(Enquiry, on_delete=models.CASCADE)
    response = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Response to {self.enquiry.student.name}"

class Program(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Branch(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bookstore(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def get_subject_name(self):
        return self.subject.name if self.subject else "General"
class Subject(models.Model):
    name = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Bookstore(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title
