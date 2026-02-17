# TODO: retirar pprint
from pprint import pprint

from django import forms
from django.contrib.auth.models import User

from . import models


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields = '__all__'
        exclude = ('usuario',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'password',
            'password2',
            'email',
        )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(),
    )

    password2 = forms.CharField(
        label='Confirma senha',
        widget=forms.PasswordInput(),
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.usuario = usuario

        if not usuario:
            # TODO: remover print
            print('INIIITTTT NAOOOOO LOGADO')
            self.fields['password'].required = True
            self.fields['password2'].required = True
            self.fields['email'].required = True
        else:
            # TODO: remover print
            print('INIIITTTT LOGADOOOOOOOOOOO')
            self.fields['password'].required = False
            self.fields['password'].label = 'Alterar senha'
            self.fields['password2'].required = False
            self.fields['password2'].label = 'Confirmar senha alterada'
            self.fields['email'].required = False

    def clean(self, *args, **kwargs):
        data = self.data
        cleaned_data = self.cleaned_data
        validation_error_msg = {}
        usuario_data = cleaned_data.get('username')
        email_data = cleaned_data.get('email')
        password_data = cleaned_data.get('password')
        password2_data = cleaned_data.get('password2')

        usuario_db = User.objects.filter(username=usuario_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = 'Usuário já existe.'
        error_msg_email_exists = 'E-mail já existe.'
        error_msg_password_match = 'As senhas não conferem.'
        error_msg_password_short = 'Sua senha precisa de pelo menos 6 caracters.'

        if self.usuario:
            # TODO: remover print
            print('LOGADOOOOOOOOOOO')

            if str(self.usuario) != usuario_data:
                if usuario_db and usuario_data == usuario_db.username:
                    validation_error_msg['username'] = error_msg_user_exists

            if self.usuario.email != email_data:
                if email_db and email_data == email_db.email:
                    validation_error_msg['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msg['password'] = error_msg_password_match
                    validation_error_msg['password2'] = error_msg_password_match

                if len(password_data) < 6:
                    validation_error_msg['password'] = error_msg_password_short


        else:
            # TODO: remover print
            print('NAOOO LOGADO!!!!')

            if usuario_db:
                validation_error_msg['username'] = error_msg_user_exists

            if email_db:
                validation_error_msg['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msg['password'] = error_msg_password_match
                    validation_error_msg['password2'] = error_msg_password_match

                if len(password_data) < 6:
                    validation_error_msg['password'] = error_msg_password_short

        if validation_error_msg:
            raise (forms.ValidationError(validation_error_msg))
