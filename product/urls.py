from django.urls import path
from .views import (AvtorAllView,BookBariView,BookRetrieView,AvtorDetailView,
                    AvtorCreateView,BookqosiwView,BookOzgertiwView,
                    AvtorDestroyView,AvtorUpdateView,BookDeleteView,
                    AvtorAllCreateView,BookBariQosiw,AvtorRetrieDestroyView,
                    BookDetailDeleteView,AvtorRetrieUpdateView,BookDetailOzgertiwView,
                    AvtorRetrieUpdateDestroy,BookDetailOzgertiwDelete)


urlpatterns = [
    path('all/', AvtorAllView.as_view()),
    path('bari/', BookBariView.as_view()),
    path('id/<int:pk>',AvtorDetailView.as_view()),
    path('get/<int:pk>',AvtorDetailView.as_view()),
    path('crate/',AvtorCreateView.as_view()),
    path('qosiw/',BookqosiwView.as_view()),
    path('Ozgertiw/<int:pk>',BookOzgertiwView.as_view()),
    path('update/<int:pk>', AvtorUpdateView.as_view()),
    path('destroy/<int:pk>', AvtorDestroyView.as_view()),
    path('delete/<int:pk>', BookDeleteView.as_view()),
    path('allcreate/', AvtorAllCreateView.as_view()),
    path('bariqosiw/', BookBariQosiw.as_view()),
    path('iddelete/<int:pk>', AvtorRetrieDestroyView.as_view()),
    path('idoshiriw/<int:pk>', BookDetailDeleteView.as_view()),
    path('idupdate/<int:pk>', AvtorRetrieUpdateView.as_view()),
    path('idozgertiw/<int:pk>', BookDetailOzgertiwView.as_view()),
    path('full/<int:pk>', AvtorRetrieUpdateDestroy.as_view()),
    path('full2/<int:pk>', BookDetailOzgertiwDelete.as_view()),



]