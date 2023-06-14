from django.url import path
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]