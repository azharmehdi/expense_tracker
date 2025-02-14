from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import UserRegister
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def register_user(request):
    serializer = UserRegister(data = request.data)
    if serializer.is_valid():
        serializer.save()
        Response ({
            "message": "User registered successfully",
            "user": serializer.data
        }, status =status.HTTP_201_created)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username,password=password)
    if user is None:
        return Response ({
            "error":"invalid credentials"
        }, status.HTTP_401_Unauthorized)
    refresh = RefreshToken.for_user(user)

    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }, status=status.HTTP_201_OK)