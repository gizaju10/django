from django.test import TestCase
from django.urls import reverse_lazy

from .models import User, UserManager


class LoggedInTestCase(TestCase):
    def setUp(self):
        """テストメソッド実行前の事前設定"""

        # テストユーザーのパスワード
        self.password = 'pass1122'

        # テスト用ユーザーを生成しインスタンス変数に格納しておく
        self.test_user = get_user_model().objects.create_user(username='Guest_user', password=self.password)

        # テスト用ユーザーでログインする
        self.client.login(email=self.test_user.email, password=self.password)