from rest_framework import generics, authentication, permissions

from .serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """새로운 유저 생성"""
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """인증된 유저 정보 관리"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permisson_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """유저 조회와 유저 반환"""
        return self.request.user
