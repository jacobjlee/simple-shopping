from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('users:create')
ME_URL = reverse('users:me')


def create_user(**params):
    """유저 생성하는 헬퍼함수"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """인증 없는 유저 테스트"""

    def setUp(self):
        self.client = APIClient

    def test_create_valid_user_success(self):
        """필요한 정보로 유저 생성 테스트"""
        payload = {
            'email': 'test@test.com',
            'password': 'testpass',
            'name': 'Test Name',
            'phone_number': '010-0000-0000'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_created)
        
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.checnk_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_already_exists(self):
        """이미 존재하는 유저 테스트"""
        payload = {
            'email': 'test@test.com',
            'password': 'testpass',
            'name': 'Test Name',
            'phone_number': '010-0000-0000'
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """비밀번호 여섯자 이상 테스트"""
        paylaod = {
            'email': 'test@test.com',
            'password': 'short',
            'name': 'Test Name',
            'phone_number': '010-0000-0000'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_retrieve_user_unauthorized(self):
        """승인되지 않은 유저 테스트"""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):
    """인증이 필요한 유저 테스트"""
    
    def setUp(self):
        self.user = create_url(
            email = 'test@test.com',
            password = 'testpass',
            name = 'Test Name',
            phone_number = '010-0000-0000'
        )
        self.client = APIClient
        self.client.force_authentication(user=self.user)

    def test_retrieve_profile_success(self):
        """로그인한 유저 조회 테스트"""
        res = self.client.get(ME_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            'name': self.user.name,
            'email': self.user.email,
            'phone_number': self.user.phone_number
        })

    def test_post_not_allowed(self):
        """POST 사용 불가 테스트"""
        res = self.client.post(ME_URL, {})

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """인증된 유저 프로필 업데이트 테스트"""
        payload = {
            'name': 'New Name', 
            'phone_number': '010-1111-1111', 
            'password': 'newpassword'
        }

        res = self.client.patch(ME_URL, payload)

        self.user.refresh_from_db()
        self.assertEqual(self.user.name, payload['name'])
        self.assertEqual(self.user.phone_number, payload['phone_number'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
