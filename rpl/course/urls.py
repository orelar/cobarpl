from django.urls import path
from .views import index, create_course


urlpatterns = [
	path('courses/<int:courid>/', index, name="courses"),
	path('create-course/<int:courid>/', create_course, name="create-course"),
    # path('search-course/<str:namacourse>/', create_course, name="search-course"),
    path('search-course/', create_course, name="search-course"),
]
