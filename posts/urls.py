from django.urls import path
from .views import HomeView, PostDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"), # if you have some number, we will route it here, pk stands for primary key (<int:id> also works in our case since primary key is id)
]