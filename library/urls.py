from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('Contact/', views.Contact, name='Contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('books/', views.book_list, name='book_list'),
    path('issue-book/<int:book_id>/', views.issue_book, name='issue_book'),
    path('issued-books/', views.issued_books, name='issued_books'),
    path('return-book/<int:issue_id>/', views.return_book, name='return_book'),
    path('', views.home, name='home'),  # Home page
    path('books/', views.available_books, name='available_books'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
