from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework import generics
from . models import webdata1,slugdata
from  .serializers import webdata1Serializer,slugdataSerializer
from rest_framework.parsers import MultiPartParser, FormParser


from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework import status

# @api_view(['POST'])
# def upload_images(request):
#     serializer = slugdataSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyModelListCreate(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = webdata1.objects.all()
    serializer_class = webdata1Serializer

class MyModelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = webdata1.objects.all()
    serializer_class = webdata1Serializer


class MyModel2ListCreate(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = slugdata.objects.all()
    serializer_class = slugdataSerializer

    def post(self, request, format=None):
            serializer = slugdataSerializer(data=request.data)
            if serializer.is_valid():
                slugdata_instance = serializer.save()

                # Iterate over each image key and save it to the database
                for i in range(1, 9):
                    image_key = f'body_img{i}'
                    image_file = request.FILES.get(image_key)
                    print(image_file)
                    if image_file:
                        setattr(slugdata_instance, image_key, image_file)
                
                slugdata_instance.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyModel2RetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser, FormParser]
    queryset = slugdata.objects.all()
    serializer_class = slugdataSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Update image data if provided
        for i in range(1, 9):
            image_key = f'body_img{i}'
            image_file = request.FILES.get(image_key)
            print(image_file)
            print(image_key)
            if image_file:
                setattr(instance, image_key, image_file)
        
        instance.save()

        return Response(serializer.data)


# Views

# def datainsert(request):
#     if request.method == 'POST':
#         DATA = request.POST.get('data')
#         print(DATA)
#         # return JsonResponse(json.dumps({'data': "okay"}), safe=False)
#     return JsonResponse(json.dumps({'data': "successfull"}), safe=False)
    

def continent_list(request,continent_name):
    continent_data = webdata1.objects.filter(continent_n=continent_name.capitalize()).first()
    print(continent_name.capitalize())
    # print(continent_data.bg_image.url)
    
    context = {"continent_data": continent_data}
    return render(request, 'asia.html', context)

    # if request.method == 'GET':
    #     continent_data = webdata1.objects.filter(continent_n=continent_name.capitalize()).first()
    #     # context = {"continent_data": continent_data}

    #     if continent_data:
    #         print("Body Image 1 URL:", continent_data.body_img1.url)
    #         print("Body Image 2 URL:", continent_data.body_img2.url)
    #         context = {"continent_data": continent_data}
    #         return render(request, 'asia.html', context)
    #     else:
    #         return render(request, 'error.html', {"errors": "Instance not found"})
    #     return render(request, 'asia.html', context)
    # elif request.method == 'PUT':
    #     # Print incoming data for debugging
    #     print(request.data)
        
    #     # Retrieve the instance to update
    #     continent_data = webdata1.objects.filter(continent_n=continent_name.capitalize()).first()
    #     if continent_data:
    #         # Serialize the instance with the incoming data
    #         serializer = webdata1Serializer(continent_data, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return render(request, 'success.html')  # Render a success page
    #         else:
    #             return render(request, 'error.html', {"errors": serializer.errors})  # Render an error page with validation errors
    #     else:
    #         return render(request, 'error.html', {"errors": "Instance not found"})  # Render an error page if instance is not found

def index (request):
    return render(request,'index.html')

def blogs(request):
    
    return render(request,"blogs.html")

def getdata(request,slugvalue):
    # a=slugdata.objects.all()
    # # print(a)
    # b=slugdata.objects.filter(slug=slugvalue)
    # print(b.slug)
    
    slug_data_insert = slugdata.objects.filter(slug=slugvalue).first()
    # print(slug_data_insert.bg_img.url)
    context={'slug_data_insert':slug_data_insert}

    return render(request,'slug.html',context)



def contact(request):
    return render(request,'contact.html')
def destination(request):
    return render(request,'destination.html')
def trips(request):
    return render(request,'trip.html')
def article(request):
    return render(request,'blog.html')

