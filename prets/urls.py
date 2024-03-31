from django.urls import path
from .views import PretsView

urlpatterns = [
        path("prets", PretsView.as_view(template_name="list_prets.html"), name="list-prets",),
    ]
