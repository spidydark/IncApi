from rest_framework import serializers
from Api import models

class Word_Serializer(serializers.ModelSerializer):
    '''
    Serializer of the word model class and performing method create and update
    '''
    class Meta:
        model=models.word_Dict
        
        fields=('word',)

    def create(self,validate_data):
        user=models.word_Dict(word=validate_data['word'])
        user.save()
        return user

    def update(self, instance, validated_data): 
        instance.name = validated_data.get('id', instance.id)
        instance.save()
        return instance