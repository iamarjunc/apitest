from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication  # Import JWTAuthentication
from .models import Author, Book, Review
from .serializers import AuthorSerializer, BookSerializer, ReviewSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requires authentication for all actions
    authentication_classes = [JWTAuthentication]  # JWT Authentication

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
