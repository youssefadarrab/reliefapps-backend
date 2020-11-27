from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from reliefapp.models import Videos
from reliefapp.serializers import VideoSerializer


# Create your views here.
@csrf_exempt
def videoApi(request,id=0):
    if request.method == 'GET':
         videos = Videos.objects.all()
         videos_serializer = VideoSerializer(videos, many=True)
         return JsonResponse(videos_serializer.data, safe=False)

    elif request.method == 'POST':
        video_data=JSONParser().parse(request)
        video_serializer = VideoSerializer(data=video_data)
        if video_serializer.is_valid():
            video_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        video_data = JSONParser().parse(request)
        video=Videos.objects.get(VideoId=video_data['VideoId'])
        video_serializer=VideoSerializer(video,data=video_data)
        if video_serializer.is_valid():
            video_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
        
    elif request.method == 'DELETE':
        video=Videos.objects.get(VideoId=id)
        video.delete()
        return JsonResponse("Deleted Successfully!", safe=False)