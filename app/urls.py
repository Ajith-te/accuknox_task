from django.urls import path
from .views import (
    SignupView, LoginView, UserSearchView,
    FriendRequestCreateView, FriendRequestUpdateView, FriendListView, PendingFriendRequestsView
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('search/', UserSearchView.as_view(), name='user-search'),
    path('friend-request/send/', FriendRequestCreateView.as_view(), name='friend-request-create'),
    path('friend-request/<int:id>/respond/', FriendRequestUpdateView.as_view(), name='friend-request-respond'),
    path('friends/', FriendListView.as_view(), name='friend-list'),
    path('friend-request/pending/', PendingFriendRequestsView.as_view(), name='pending-friend-requests'),
]
