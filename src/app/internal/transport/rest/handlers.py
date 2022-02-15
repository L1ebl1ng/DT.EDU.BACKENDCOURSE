from app.internal.services.user_service import get_data
from django.http import JsonResponse


def me_endpoint(request, username):
    answer = get_data(username)
    return JsonResponse(answer)
