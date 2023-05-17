from django.contrib import admin
from contact.models import contactform

class contactdisplay(admin.ModelAdmin):
    list_display=('name','email','subject','message')

admin.site.register(contactform,contactdisplay)

# Register your models here.
