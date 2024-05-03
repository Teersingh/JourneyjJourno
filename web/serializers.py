from rest_framework import serializers
from . models  import webdata1,slugdata



class  webdata1Serializer(serializers.ModelSerializer):


    bg_image = serializers.ImageField()
    body_img1 = serializers.ImageField()
    body_img2 = serializers.ImageField()
    
    class Meta:
        model= webdata1
        fields= ['continent_n','desciption_1','desciption_2','desciption_3','desciption_4','description_5','description_6','title','countries',"bg_image","body_img1","body_img2"]

class slugdataSerializer(serializers.ModelSerializer):
    

    # body_img5 = serializers.ImageField()
    # body_img6 = serializers.ImageField()
    # body_img7 = serializers.ImageField()

    class Meta:
        model=slugdata
        fields= "__all__"