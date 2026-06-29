from .models import AvtorModel,BookModel
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, CreateAPIView, DestroyAPIView,
                                     ListCreateAPIView, RetrieveUpdateAPIView,
                                     RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView)
from .serializers import AvtorModelSerializer,BookModelSerializer

class AvtorAllView(ListAPIView):
    queryset = AvtorModel.objects.all()
    serializer_class = AvtorModelSerializer

class BookBariView(ListAPIView):
    queryset = BookModel.objects.all()  
    serializer_class = BookModelSerializer 

class AvtorDetailView(RetrieveAPIView):
    queryset = AvtorModel.objects.all()
    serializer_class = AvtorModelSerializer


class BookRetrieView(RetrieveAPIView):
    queryset = BookModel.objects.all()  
    serializer_class = BookModelSerializer         

class AvtorCreateView(CreateAPIView):
    queryset = AvtorModel.objects.all()
    serializer_class = AvtorModelSerializer
 
class BookqosiwView(CreateAPIView):
    queryset = BookModel.objects.all()  
    serializer_class = BookModelSerializer         

class AvtorUpdateView(UpdateAPIView):
    queryset = AvtorModel.objects.all()
    serializer_class = AvtorModelSerializer

class BookOzgertiwView(UpdateAPIView):
    queryset = BookModel.objects.all()  
    serializer_class = BookModelSerializer 

class AvtorDestroyView(DestroyAPIView):
    queryset = AvtorModel.objects.all()
    serializer_class = AvtorModelSerializer

class BookDeleteView(DestroyAPIView):
    queryset = BookModel.objects.all()  
    serializer_class = BookModelSerializer 

class AvtorAllCreateView(ListCreateAPIView):
    queryset = AvtorModel.objects.all()
    serializer_class = AvtorModelSerializer

class BookBariQosiw(ListCreateAPIView):
    queryset = BookModel.objects.all()  
    serializer_class = BookModelSerializer 

class AvtorRetrieDestroyView(RetrieveDestroyAPIView):
    queryset = AvtorModel.objects.all()
    serializer_class = AvtorModelSerializer

class BookDetailDeleteView(RetrieveDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer    

class AvtorRetrieUpdateView(RetrieveUpdateAPIView):
    queryset = AvtorModel.objects.all()
    serializer_class = AvtorModelSerializer

class BookDetailOzgertiwView(RetrieveUpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer        

class AvtorRetrieUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = AvtorModel.objects.all()
    serializer_class = AvtorModelSerializer

class BookDetailOzgertiwDelete(RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookModelSerializer    
