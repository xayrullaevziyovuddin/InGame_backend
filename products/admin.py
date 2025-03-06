from django.contrib import admin
from .models import Product, ProductImage, ProductAttribute, Category, ProductType, Brand


@admin.register(Category)  # Add this!
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
   list_display = ('name', 'category')


@admin.register(Brand)  # Add this!
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "category", "price", "stock", "is_active")
    list_filter = ("brand", "category", "product_type", "is_active")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline, ProductAttributeInline]
    list_editable = ("is_active", "price", "stock")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Основная информация", {
            "fields": ("name", "slug", "description", "main_image")
        }),
        ("Классификация", {
            "fields": ("category", "product_type", "brand")
        }),
        ("Цены и наличие", {
            "fields": ("price", "discount_price", "stock", "is_active")
        }),
        ("Даты", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",)
        }),
    )