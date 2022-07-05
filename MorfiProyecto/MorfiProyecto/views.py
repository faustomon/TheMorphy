from django.shortcuts import render

def error_404(request, exception):
    return render(request,"AppFunciones/templates/not_found.html", status=404)