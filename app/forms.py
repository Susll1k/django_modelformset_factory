from django import forms
from .models import Recipe, Ingredients, Todo
from captcha.fields import CaptchaField

class CaptchaForm(forms.Form):
    captcha = CaptchaField()

ingredient_formset= forms.modelformset_factory(Ingredients, fields=['title'], extra=1)

todo_formset= forms.modelformset_factory(Todo, fields=['title','description','status','deadline'],extra=1)
