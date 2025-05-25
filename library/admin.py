from django.contrib import admin
from .models import Student, Enquiry, StudentResponse, Program, Branch, Subject, Bookstore
from django.contrib import admin
from .models import Book, BookIssue
from django.contrib import admin
from .models import Book
from django.contrib import admin
from .models import Book


@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'issue_date', 'return_date')
    list_filter = ('issue_date', 'return_date')
    search_fields = ('book__title', 'user__username')



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_available')
    list_filter = ('is_available',)
    search_fields = ('title', 'author')


admin.site.register(Student)
admin.site.register(Enquiry)
admin.site.register(StudentResponse)
admin.site.register(Program)
admin.site.register(Branch)
admin.site.register(Subject)
admin.site.register(Bookstore)
