from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import User, FriendRequest

from .serializers import (
    UserSerializer, SignupSerializer, LoginSerializer,
    FriendRequestSerializer, FriendRequestCreateSerializer
)

from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = []


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        keyword = self.request.query_params.get('q', '').lower()
        return User.objects.filter(Q(email__iexact=keyword) | Q(username__icontains=keyword))


class FriendRequestCreateView(generics.CreateAPIView):
    serializer_class = FriendRequestCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        now = timezone.now()
        one_minute_ago = now - timedelta(minutes=1)
        recent_requests = FriendRequest.objects.filter(from_user=self.request.user, created_at__gte=one_minute_ago).count()

        if recent_requests >= 3:
            raise serializers.ValidationError({"error": "You can only send 3 friend requests per minute."})
        
        # Ensure `from_user` is set from the request user
        serializer.save(from_user=self.request.user)

class FriendRequestUpdateView(generics.UpdateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        friend_request = self.get_object()
        if friend_request.to_user != request.user:
            return Response({"error": "You cannot modify this request."}, status=status.HTTP_403_FORBIDDEN)
        
        status = request.data.get('status')
        if status not in ['accepted', 'rejected']:
            return Response({"error": "Invalid status."}, status=status.HTTP_400_BAD_REQUEST)

        friend_request.status = status
        friend_request.save()

        return Response(FriendRequestSerializer(friend_request).data)


class FriendListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(
            Q(sent_requests__to_user=self.request.user, sent_requests__status='accepted') |
            Q(received_requests__from_user=self.request.user, received_requests__status='accepted')
        ).distinct()


class PendingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, status='pending')
