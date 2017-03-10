from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from post_box.models import Person

# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class NewPerson(View):
    
    def get(self,request):
        
        return render(request,"post_box/form.html")
    
    def post(self,request):
        response = HttpResponse()
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        description = request.POST.get("description")
        new_person = Person.objects.create(name = name, surname = surname, description = description)
        response.write("Do bazy dodano osobę: {} {}, z opisem {}".format(name,surname,description))
        return response
    

@method_decorator(csrf_exempt, name="dispatch")
class ModPerson(View):
    
    def get(self,request,id):
        context = {
            "person" : Person.objects.get(pk=id)
            }
        return render(request,"post_box/modify_form.html",context)