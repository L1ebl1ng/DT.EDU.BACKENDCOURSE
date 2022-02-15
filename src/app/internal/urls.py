from django.urls import path
from app.internal.transport.rest.handlers import me_endpoint

urlpatterns = [
    path('me/<str:username>', me_endpoint)
]
