import queue

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
USER_QUEUE = {}

def chat(request):
    uid = request.GET.get('uid')
    USER_QUEUE[uid] = queue.Queue()
    return render(request, 'chat.html',{'uid':uid})

def send_msg(request):
    text = request.GET.get('text')
    for uid,q in USER_QUEUE.items():
        q.put(text)
    return HttpResponse("OK")


def get_msg(request):
    uid = request.GET.get('uid')
    q = USER_QUEUE[uid]
    result = {"status": True, "data": None}
    try:
        text = q.get(timeout=10)
        result["data"] = text
    except queue.Empty as e:
        result["status"] = False
    return JsonResponse(result)