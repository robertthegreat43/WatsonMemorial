from asyncio import events

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from fsspec.implementations import reference
from nltk.corpus.reader import reviews
from django.http import StreamingHttpResponse
from .Camera import CameraController

from .models import EventSales, Events, DailyBread, Pastor
from .utils import products
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LocalScripture
from .AI_file import detect_topic
from .bible_api import fetch_scripture





def index(request):
    events = Events.objects.all()
    events_list = []
    event_name = request.GET.get('event_name')
    event_date = request.GET.get('event_date')
    event_location = request.GET.get('event_location')
    event_description = request.GET.get('event_description')
    event_image = request.GET.get('event_image')
    for event in events:
        if event_name == event.event_name:
            events_list.append({'event_name: ' + event.event_name + '',
                               'event_date:'  + event_date + '',
                               'event_location:', event_location ,
                               'event_description:' ,event_description,
                               'event_image:', event_image })

    events_now = {'events_list':events}
    return render(request,'CommunityEvents.html', events_now)



def daily_bread(request):
    bread = DailyBread.objects.all()
    breads_list = []
    scripture_name = request.GET.get('scripture_name')
    author = request.GET.get('author')
    date_created = request.GET.get('date_created')
    for breads in bread:
        if scripture_name == breads.scripture_name:
            breads_list.append({'scripture_name:' + breads.scripture_name + '',
                          'author:' + author + '',
                          'date_created:' + date_created + ''})
    daily_now = {'breads_list':bread}
    return render(request, 'Prayers.html', daily_now)


def video(request):

    return render(request, "videorecording.html",)






def home(request):
    return render(request, "home.html")




def items_list(request):
    items = EventSales.objects.all()

    context = {
        "items_list": items
    }

    return render(request, "products.html", context)


def prayers_for_those_in_need(request):
    p = Pastor.objects.all()
    pastors_list = []
    name = request.GET.get('name')
    email = request.GET.get('email')
    pastor = request.GET.get('pastor')
    prayer = request.GET.get('prayer')
    audio_segment = request.GET.get('audio_segment')

    for pastors in p:
        if name == pastors.name:
            pastors_list.append({'name:' + pastors.name + '',
                                 'email:' + email + '',
                                'pastor' + pastor + '',
                                 'prayer:' + prayer + '',
                                 'audio_segment:' + audio_segment
                                 })


    praying_now = {'pastors_list': p }

    return render(request, "prayers_for_those_in_need.html", praying_now)


def media_example(request):
    if request.method == 'POST':
        save_path = (settings.MEDIA_ROOT /
        request.FILES["file_upload"].name)

        with open(save_path, "wb") as output_file:
            for chunk in request.FILES[
                "file_upload"].chunks():
                output_file.write(chunk)

    return render(request, "media_example.html")

def logged_out(request):
    return render(request, "Logged_out.html")





def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    return render(request, "accounts/login.html", {"form": form})


def profile(request):
    return render(request, "profile.html")


camera = CameraController()

def video_feed(request):
    return StreamingHttpResponse(
        camera.stream(),
        content_type='multipart/x-mixed-replace; boundary=frame'
    )




def get_scripture(reference):
    url = f"https://biblechat_api/{reference}"
    r = requests.get(url)
    if r.status_code != 200:
        return None
    data = r.json()
    return data.get("text", None)

# ... existing code ...

def pastoral_reflection(topic):
    reflections = {
        "love": "Love is patient and kind. God calls us to walk in compassion and humility.",
        "faith": "Faith is trusting God even when the path is unclear. He remains faithful.",
        "strength": "God strengthens those who seek Him. You are never alone.",
        "forgiveness": "Forgiveness frees the heart. Christ forgave us so we may forgive others.",
        "fear": "Fear is natural, but God gives courage. His Spirit empowers you.",
        "hope": "Hope reminds us that God is still working, even when we cannot see the full picture.",
        "peace": "God's peace can guard your heart and mind even in difficult seasons.",
        "wisdom": "God invites us to ask for wisdom, and He gives generously.",
        "guidance": "The Lord leads those who seek Him with a sincere heart.",
        "healing": "God is near to the brokenhearted and brings comfort, strength, and restoration.",
        "patience": "Waiting can be hard, but God often shapes our hearts in the waiting.",
        "temptation": "God provides a way through temptation and gives strength to stand.",
        "anxiety": "You can bring every worry to God, because He cares for you.",
        "depression": "Even in dark valleys, God is present and His love has not left you.",
        "grief": "God comforts those who mourn and walks with them through sorrow.",
        "anger": "God can help calm the heart and guide you toward peace and understanding.",
        "loneliness": "You are seen, known, and loved by God. You are not forgotten.",
        "stress": "God invites you to lay your burdens before Him and receive rest.",
        "relationships": "God calls us to love, patience, forgiveness, and humility in our relationships.",
        "purpose": "Your life has meaning, and God can guide your steps toward His purpose."
    }

    return reflections.get(topic, "Let this scripture guide your heart today.")


TOPIC_VERSES = {
    "love": "1 Corinthians 13:4",
    "faith": "Hebrews 11:1",
    "strength": "Isaiah 41:10",
    "forgiveness": "Ephesians 4:32",
    "fear": "2 Timothy 1:7",
    "hope": "Romans 15:13",
    "peace": "John 14:27",
    "wisdom": "James 1:5",
    "guidance": "Proverbs 3:5-6",
    "healing": "Psalm 147:3",
    "patience": "Romans 12:12",
    "temptation": "1 Corinthians 10:13",
    "anxiety": "1 Peter 5:7",
    "depression": "Psalm 34:18",
    "grief": "Matthew 5:4",
    "anger": "James 1:19-20",
    "loneliness": "Deuteronomy 31:6",
    "stress": "Matthew 11:28",
    "relationships": "Colossians 3:13",
    "purpose": "Jeremiah 29:11"
}


@api_view(["POST"])
def biblechat_api(request):
    user_msg = request.data.get("message", "").strip()

    if not user_msg:
        return Response({"reply": "Please type a message first."})

    topic = detect_topic(user_msg)

    reference = TOPIC_VERSES.get(topic, "Proverbs 3:5-6")
    reflection = pastoral_reflection(topic)

    try:
        entry = LocalScripture.objects.get(topic=topic)
        reference = entry.reference

        if entry.reflection:
            reflection = entry.reflection

    except LocalScripture.DoesNotExist:
        pass

    scripture_text = fetch_scripture(reference)

    if not scripture_text:
        scripture_text = "Scripture could not be retrieved from the Bible API."

    ai_response = (
        f"<strong>Topic:</strong> {topic}<br>"
        f"<strong>Scripture:</strong> {reference}<br><br>"
        f"{scripture_text}<br><br>"
        f"<strong>Reflection:</strong> {reflection}"
    )

    return Response({"reply": ai_response})


def biblechat(request):
    return render(request, "biblechat.html")



