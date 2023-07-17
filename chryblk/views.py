from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

def user_input(request):
    if request.method == "POST":
        user_text = request.POST.get('text_input', '')
        return HttpResponse("You entered: " + user_text)
    else:
        return render(request, 'user_input.html')
