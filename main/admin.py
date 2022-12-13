from django.contrib import admin

# Register your models here.
from .models import Category, Product
from review.models import Comment, Rating

class RatingInLine(admin.TabularInline):
    model = Rating

class CommentInLine(admin.TabularInline):
    model = Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','category','status']
    list_filter = ['category', 'status']
    search_fields = ['title', 'description']
    inlines = [CommentInLine, RatingInLine]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
