from django.db import models
from django.contrib.auth.models import AbstractUser

# AbstractUser를 사용하면 기존의 auth_user테이블에 있던 열들을 전부 유지한 채 새로운 열을 추가할 수 있다. 
# 이로써 앞으로는 auth_user의 역할을 MyUser가 대신할 것.
class ExtendUser(AbstractUser):
    
    email = models.EmailField(blank=False, max_length=255, verbose_name="email")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
 