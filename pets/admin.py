from django.contrib import admin
from pets.models import Animal, Breed

@admin.register(Animal)
class BookAdmin(admin.ModelAdmin):
    pass
    # list_filter = ('title', 'author')

    # @staticmethod
    # def author_full_name(obj):
    #     return obj.author.full_name

    # list_display = ('title', 'author_full_name',)
    # fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'publish', 'copy_count', 'price', 'friend', 'pic')


@admin.register(Breed)
class AuthorAdmin(admin.ModelAdmin):
    pass