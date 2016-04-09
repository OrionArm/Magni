from django.contrib import admin
from .models import Person, Location, Comment
# Register your models here., Location, Comment


class LocationInline(admin.TabularInline):
	model = Location


class PersonAdmin(admin.ModelAdmin):
	
	inlines = [
	LocationInline
	]

	class Meta:
		model = Person

admin.site.register(Person, PersonAdmin)
admin.site.register(Comment)
admin.site.register(Location)