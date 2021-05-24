from django.http import JsonResponse

# Create your views here.


def sulthan(request):
    return JsonResponse({'info': 'Django React Course', 'name': "Sulthan", 'lastname': "Mohiddin"})