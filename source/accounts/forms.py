from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta(UserCreationForm.Meta):
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")

    def is_valid(self):
        super().is_valid()
        data = self.cleaned_data
        if not data.get('first_name') and not data.get('last_name'):
            self.add_error('first_name', 'Одно из полей Имени или Фамилии должно быть заполнено')
            return False
        return True
