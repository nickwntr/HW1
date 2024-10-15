from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def as_view(request):
    return render(request,"second_task/func_template.html")

class as_class(TemplateView):
    template_name = "second_task/class_template.html"