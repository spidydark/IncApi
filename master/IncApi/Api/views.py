from pyexpat import model
from rest_framework import viewsets
from rest_framework.response import Response
from Api import models
from Api import serializer

# Create your views here.

class ApiView1(viewsets.ModelViewSet):
    ''''
    Class for performing update and delete
    '''

    serializer_class=serializer.Word_Serializer
    queryset=models.word_Dict.objects.all()

    def update(self,request,pk=None):
        val=models.word_Dict.objects.get(id=pk)
        val.word=request.POST['word']
        val.save()
        return Response({'word':val.word})



