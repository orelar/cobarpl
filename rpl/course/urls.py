from django.urls import path
from .views import index, create_course, create_bab, search_all_course, search_all_bab

urlpatterns = [
    path('', search_all_course, name="search-all-course"),
    path('<int:courid>/', index, name="courses"),
    path('create-course/', create_course, name="create-course"),
    path('create-bab/<int:course_id>/', create_bab, name="create-bab"),
    path('bab/<int:course_id>/', search_all_bab, name="search-all-bab"),
]
