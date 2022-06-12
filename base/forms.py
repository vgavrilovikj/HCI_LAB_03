from django.forms import ModelForm
from .models import Post, UserInfo, User, Comment


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Comment
        exclude = ['user', 'post']


class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = UserInfo
        exclude = ['last_name', 'last_login', 'is_staff', 'date_joined', 'groups', 'user_permissions', 'is_superuser', 'is_active', 'password', 'user']