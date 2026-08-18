from django.conf import settings
from openai.types.video_extend_params import Video
from rest_framework import generics
from .models import Events
from .serializers import EventsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .Camera import CameraController
from django.http import FileResponse, Http404
import os
from .views import camera


class EventsList(generics.ListAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer











# camera_app/api_views.py


@api_view(['POST'])
def start_recording(request):
    from Events.views import camera
    filename = camera.start_recording()
    return Response({"status": "recording started", "file": filename})


@api_view(['POST'])
def stop_recording(request):
    camera.stop_recording()
    return Response({"status": "recording stopped"})


@api_view(['GET'])
def list_recordings(request):
    files = [f for f in os.listdir('.') if f.endswith('.mp4')]
    return Response({"videos": files})


@api_view(['GET'])
def download_video(request, filename):
    file_path = os.path.join(settings.BASE_DIR, filename)

    if not os.path.exists(file_path):
        raise Http404("Video file not found")

    return FileResponse(open(file_path, 'rb'), as_attachment=True)



