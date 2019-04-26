from authentication.serializers.user import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json

@api_view(['GET'])
def get_me_action(request):
    current_user = request.user
    serializer = UserSerializer(current_user)
    return Response(serializer.data)

@csrf_exempt
def sign_in_action(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return JsonResponse({'ok': True}, status=status.HTTP_200_OK)
    else:
        return JsonResponse({'message': 'Failed to authenticate.'}, status=status.HTTP_401_UNAUTHORIZED)

# TODO: Add validation for data here.
@api_view(['POST'])
def sign_up_action(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'GET'])
def sign_out_action(request):
    try:
        logout(request)
        return JsonResponse({'message': 'Authenticated successfully.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)