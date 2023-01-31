from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery
import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1



@admin.register(Product)
@admin_thumbnails.thumbnail('images')
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'stock', 'category', 'modified_date', 'is_available']
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['product', 'variation_category', 'variation_value', 'is_active', 'created_date']
    list_editable = ['is_active']
    list_filter = ['product', 'variation_category', 'variation_value', 'created_date']


@admin.register(ReviewRating)
class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'subject', 'rating', 'status']


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    pass
