from django.contrib import admin
from .models import Like, PostComment, Profilis, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('uploaded_by', 'description')

admin.site.register(Post, PostAdmin)
admin.site.register(Profilis)
admin.site.register(PostComment)
admin.site.register(Like)



# Register your models here.
