from django import forms


class CityForm(forms.Form):
    CHOICES = (('La Spezia', 'La Spezia'), ('Trieste', 'Trieste'),
               ('Trento', 'Trento'), ('Pescara', 'Pescara'),
               ('Catania', 'Catania'))
    city = forms.ChoiceField(choices=CHOICES,)
