from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Quản trị viên'),
        ('User', 'Người dùng thường'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='User', verbose_name="Vai trò")
    full_name = models.CharField(max_length=100, blank=True, verbose_name="Họ và tên")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == 'Admin' or self.is_superuser

    class Meta:
        verbose_name = "Người dùng"
        verbose_name_plural = "Người dùng"
