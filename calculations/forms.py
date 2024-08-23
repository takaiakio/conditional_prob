from django import forms

class ConditionalProbabilityForm(forms.Form):
    probability_a_and_b = forms.FloatField(label='P(A ∩ B)', min_value=0, max_value=1)
    probability_a = forms.FloatField(label='P(A)', min_value=0, max_value=1)
    probability_b = forms.FloatField(label='P(B)', min_value=0, max_value=1)
