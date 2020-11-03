from django.contrib import admin

from blogs.models import Topic, Entry, IntroduceTitle, Introduce
# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(IntroduceTitle)
admin.site.register(Introduce)