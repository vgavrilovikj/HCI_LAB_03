from django.forms import ModelForm
from .models import Post, UserInfo, User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = UserInfo
        exclude = ['last_name', 'last_login', 'is_staff', 'date_joined', 'groups', 'user_permissions', 'is_superuser', 'is_active', 'password', 'user']