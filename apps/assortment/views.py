from rest_framework import viewsets, generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class NewArrivalsList(generics.ListAPIView):
    queryset = Product.objects.all().order_by('-created_at')[:10]  
    serializer_class = ProductSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

        return Response({
            "user": {
                "username": user.username,
            },
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })