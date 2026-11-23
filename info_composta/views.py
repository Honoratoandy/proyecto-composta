from django.shortcuts import render

def inicio(request):
    return render(request, 'info_composta/index.html')
