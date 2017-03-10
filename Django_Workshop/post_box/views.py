from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class NewPerson(View):
    
    def get(self,request):
        response = HttpResponse()
        response.write("""<form method="POST">
        Imię:<br>
        <input type="text" name="name">
        <br>
        Nazwisko:<br>
        <input type="text" name="surname"><br>
        Opis:<br>
        <textarea name="description"></textarea>
        <br><br>
        <input type="submit" value="Wyślij">
        </form>
        """)
        
        return response
    
    def post(self,request):
        pass