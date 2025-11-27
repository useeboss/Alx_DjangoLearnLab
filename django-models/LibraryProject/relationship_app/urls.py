from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book


urlpatterns = [
    # Function-based views
    urlpatterns = [
    path('admin-role/', admin_view, name='admin_view'),
    path('librarian-role/', librarian_view, name='librarian_view'),
    path('member-role/', member_view, name='member_view'),
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),

]


    # Authentication views
    path('register/', views.register_view, name='register'),  # checker looks for "views.register"
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]



from django.urls import path
from .views import admin_view

urlpatterns = [
    path('admin-role/', admin_view, name='admin_view'),
]


from django.urls import path
from .views import librarian_view

urlpatterns = [
    path('librarian-role/', librarian_view, name='librarian_view'),
]
