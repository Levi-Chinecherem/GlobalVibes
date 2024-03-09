# community/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Community, Chat
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

@login_required
def community_list(request):
    communities = Community.objects.all()
    return render(request, 'community/community_list.html', {'communities': communities})

@login_required
def community_chat(request, community_id):
    community = get_object_or_404(Community, id=community_id)
    chats = community.chat_set.all()

    unique_users = set()
    unique_chats = []

    for chat in chats:
        if chat.user not in unique_users:
            unique_users.add(chat.user)
            unique_chats.append(chat)

    return render(request, 'community/community_chat.html', {'community': community, 'unique_chats': unique_chats, 'chats': chats})

@csrf_exempt
@login_required
def send_chat(request, community_id):
    if request.method == 'POST':
        community = get_object_or_404(Community, id=community_id)
        message = request.POST.get('message', '')
        media_file = request.FILES.get('media_file', None)

        if message or media_file:
            # Handle the message and/or media_file data as needed
            chat = Chat.objects.create(
                community=community,
                user=request.user,
                message=message,
                media_file=media_file
            )

            response_data = {
                'status': 'success',
                'message': chat.message,
                'sender': chat.user.username,
                'media_file_url': chat.media_file.url if chat.media_file else None,
            }
        else:
            response_data = {'status': 'error', 'message': 'Invalid request, no message or media file provided'}

        return JsonResponse(response_data)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
