
from django.shortcuts import render
from contact.models import contactform
from recipes.models import recipe

def home(request):
    recipe_data=recipe.objects.all()
    data={
        'recipe_data':recipe_data
    }
    # data={
    #     'title':'Home',
    # }
    return render(request,"index.html",data)
def about_us(request):
    return render(request,"about-us.html")
def recipes(request):
    recipe_data=recipe.objects.all()
    data={
        'recipe_data':recipe_data
    }

    return render(request,"recipes.html",data)

def recipedetail(request,recipeid):
    recipedetail=recipe.objects.get(id=recipeid)
    data={
        'recipedetail':recipedetail
    }
    return render(request,"recipepost.html",data)

def make_recipe(request):
     return render(request,"makerecipe.html")

def contact(request):

    return render(request,"contact.html")

def contact_form(request):
    if request.method=="POST":
        user_name=request.POST.get('name')
        user_email=request.POST.get('email')
        user_subject=request.POST.get('subject')
        user_message=request.POST.get('message')

        user_data=contactform(name=user_name,email=user_email,subject=user_subject,message=user_message)
        # print(user_name,user_email,user_subject,user_message)
        # data=contactform(name=user_name,email=user_email,subject=user_subject,message=user_message)

        user_data.save()
        message='Thank you for Conact us.....'
    return render(request,"contact.html",{'message':message})