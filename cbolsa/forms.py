from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile  # Asegúrate de importar tu modelo UserProfile

class CustomUserCreationForm(UserCreationForm):
    # Campos adicionales de UserProfile
    saldo = forms.DecimalField(max_digits=12, required=True, label="Saldo Inicial")
    tipo_usuario = forms.ChoiceField(choices=UserProfile.USER_TYPE_CHOICES, required=True, label="Tipo de Usuario")
    
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')  # Incluye los campos de User

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

        # Crear UserProfile solo si no existe
        UserProfile.objects.update_or_create(
            user=user,
            defaults={
                'saldo': self.cleaned_data['saldo'],
                'tipo_usuario': self.cleaned_data['tipo_usuario']
            }
        )

        return user
