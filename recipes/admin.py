from django.contrib import admin
from recipes.models import recipe
# from recipes.models import service

# class serviceadmin(admin.ModelAdmin):
#     list_display=('service_icon','service_title','service_des')

# admin.site.register(service,serviceadmin)
# Register your models here.
class recipedisplay(admin.ModelAdmin):
    list_display=('recipe_title','recipe_image','recipe_date','recipe_des','recipe_preparetime','recipe_cooktime','recipe_servings','recipe_readyin','recipe_youtubelink','recipe_ingredients','recipe_rating','recipe_comment')

admin.site.register(recipe,recipedisplay)