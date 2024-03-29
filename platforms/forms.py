from PIL import Image

from django import forms
from django.core.files import File
from django.apps import apps

from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, Div

Platform = apps.get_model('platforms.Platform')

class PlatformCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(HTML("""<div class="form-group"><input type="submit" value="Create Platform" class="btn btn-primary"></div>"""))

    class Meta:
        model = Platform
        fields = ['name', 'slug']

class PlatformUpdateForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    def save(self):
        platform = super().save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(platform.image)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(platform.image.path)

        return platform

    class Meta:
        model = Platform
        fields = ['name', 'slug', 'image', 'x', 'y', 'width', 'height']
