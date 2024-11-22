from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


router = DefaultRouter()
router.register(r"snippets", views.SnippetViewSet, basename="snippet")
router.register(r"users", views.UserViewSet, basename="user")


urlpatterns = [
    path('languages/', views.language_list),
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)