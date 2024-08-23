from django.shortcuts import render
from .forms import ConditionalProbabilityForm

def calculate_probability(request):
    result = None
    if request.method == 'POST':
        form = ConditionalProbabilityForm(request.POST)
        if form.is_valid():
            probability_a_and_b = form.cleaned_data['probability_a_and_b']
            probability_a = form.cleaned_data['probability_a']
            probability_b = form.cleaned_data['probability_b']
            
            # P(A|B) = P(A ∩ B) / P(B)
            probability_a_given_b = probability_a_and_b / probability_b if probability_b > 0 else None
            # P(B|A) = P(A ∩ B) / P(A)
            probability_b_given_a = probability_a_and_b / probability_a if probability_a > 0 else None

            result = {
                'probability_a_given_b': probability_a_given_b,
                'probability_b_given_a': probability_b_given_a
            }
    else:
        form = ConditionalProbabilityForm()

    return render(request, 'calculations/calculate.html', {'form': form, 'result': result})
