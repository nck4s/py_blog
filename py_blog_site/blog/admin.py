from django.contrib import admin
from .models import Post

admin.site.register(Post) #чтобы модель для создания новых постов отображалась в панели администрирования
