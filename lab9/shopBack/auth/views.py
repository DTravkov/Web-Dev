from rest_framework import status, serializers
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import LoginSerializer, LogoutSerializer, SignUpSerializer, CustomRefreshSerializer, CheckSerializer



class AuthViewSet(GenericViewSet):

    def get_serializer_class(self, *args, **kwargs):
        serializer_map = {
            'signup' : SignUpSerializer,
            'login' : LoginSerializer,
            'logout' : LogoutSerializer,
            'refresh' : CustomRefreshSerializer
        }
        option = serializer_map.get(self.action, None)
        if option is not None:
            return option
        
        return super().get_serializer_class()
    
    def get_permissions(self):
        if self.action in ['refresh', 'logout']:
            return [IsAuthenticated()]
        
        return [AllowAny()]
    
    @action(detail=False, methods=['POST'])
    def logout(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({"detail" : "Successful logout"}, status=status.HTTP_200_OK)
    

    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data.get('refresh')
        access_token = serializer.validated_data.get('access')
        return Response( { "refresh" : str(refresh_token),
                           "access" : str(access_token) }, status=status.HTTP_200_OK)
    

    @action(detail=False, methods=['POST'])
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        return Response({'detail' : "Signed up successfully."}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['POST'])
    def refresh(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh = serializer.validated_data.get('refresh')
        access = serializer.validated_data.get('access')
        
        return Response({"refresh" : str(refresh), "access" : str(access) }, status=status.HTTP_200_OK)