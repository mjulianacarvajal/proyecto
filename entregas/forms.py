from django.forms import ModelForm, widgets
from entregas.models import EntregaCliente, EntregaExterna
from entregas.views import EntregaCliente,EntregaExterna


class EntregaClienteForm(ModelForm):
    class Meta:
        model = EntregaCliente
        fields = "__all__"


class EntregaClienteUpdateForm(ModelForm):
    class Meta:
        model = EntregaCliente
        fields = "__all__"
        widgets = {
            'nombre': widgets.DateInput(attrs={'placeholder': 'EntregaExterna'})  # para EntregaExternas internos
        }


class EntregaExternaForm(ModelForm):
    class Meta:
        model = EntregaExterna
        fields = "__all__"
        widgets = {
            'nombre': widgets.DateInput(attrs={'placeholder': 'EntregaExterna'})  # para EntregaExternas internos
        }


class EntregaExternaUpdateForm(ModelForm):
    class Meta:
        model = EntregaExterna
        fields = "__all__"
        widgets = {
            'nombre': widgets.DateInput(attrs={'placeholder': 'EntregaExterna'})  # para EntregaExternas internos
        }
