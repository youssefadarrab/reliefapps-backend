from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from reliefapp.models import Bookmark, History
from reliefapp.serializers import BookmarkSerializer, HistorySerializer


# Create your views here.
@csrf_exempt
def historyApi(request,id=0):
    if request.method == 'GET':
         history = History.objects.all()
         history_serializer = HistorySerializer(history, many=True)
         return JsonResponse(history_serializer.data, safe=False)

    elif request.method == 'POST':
        history_data=JSONParser().parse(request)
        history_serializer = HistorySerializer(data=history_data)
        if history_serializer.is_valid():
            history_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        history_data = JSONParser().parse(request)
        history=History.objects.get(HistoryId=history_data['HistoryId'])
        history_serializer=HistorySerializer(history,data=history_data)
        if history_serializer.is_valid():
            history_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
        
    elif request.method == 'DELETE':
        history=History.objects.get(HistoryId=id)
        history.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

@csrf_exempt
def bookmarkApi(request,id=0):
    if request.method == 'GET':
         bookmark = Bookmark.objects.all()
         bookmark_serializer = BookmarkSerializer(bookmark, many=True)
         return JsonResponse(bookmark_serializer.data, safe=False)

    elif request.method == 'POST':
        bookmark_data=JSONParser().parse(request)
        bookmark_serializer = BookmarkSerializer(data=bookmark_data)
        if bookmark_serializer.is_valid():
            bookmark_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        bookmark_data = JSONParser().parse(request)
        bookmark=Bookmark.objects.get(BookmarkId=bookmark_data['HistoryId'])
        bookmark_serializer=BookmarkSerializer(bookmark,data=bookmark_data)
        if bookmark_serializer.is_valid():
            bookmark_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)
        
    elif request.method == 'DELETE':
        bookmark=Bookmark.objects.get(BookmarkId=id)
        bookmark.delete()
        return JsonResponse("Deleted Successfully!", safe=False)