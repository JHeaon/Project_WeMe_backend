from django.contrib import admin
from .models import Post, Position, TechStack

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    pass
