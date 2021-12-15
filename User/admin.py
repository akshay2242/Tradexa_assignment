from django.contrib import admin
from .models import User
from .models import Post
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','username','password')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'created_place', 'updated_place')


