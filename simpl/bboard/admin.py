from django.contrib import admin
from.models import Bb, Rubric


class BbAdmin (admin.ModelAdmin):
	list_display = ("title", "content", "prise", "published", "rubric")
	list_display_links = ("title", "content")
	search_fields = ()

admin.site.register(Bb)
admin.site.register(Rubric)


