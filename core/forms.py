from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, Div

from allauth.account.forms import LoginForm, SignupForm

class CrispyLoginForm(LoginForm):
    """Convert Allauth loginform into a bootstrap4 crispy form"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

class CrispySignupForm(SignupForm):
    """Convert Allauth signupform into a bootstrap4 crispy form"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
