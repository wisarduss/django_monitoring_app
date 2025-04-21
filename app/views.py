from django.http import JsonResponse
from .monitoring import process_request

def health_check(request):
    process_request()
    return JsonResponse({"status": "ok"})

def example_view(request):
    process_request()
    return JsonResponse({"message": "Hello, World!"})