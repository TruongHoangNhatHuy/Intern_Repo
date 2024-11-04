from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from oauth2_provider.views.generic import ProtectedResourceView


class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hi mom")


@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)