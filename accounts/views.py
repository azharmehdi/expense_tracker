from rest_framework.decorators  import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegister

@api_view(['POST'])
def register_user(request):
    serializer = UserRegister(data = request.data)
    if serializer.is_valid():
        serializer.save()
        Response ({
            "message": "User registered successfully",
            "user": serializer.data
        }), status =status.HTTP_201_created

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

