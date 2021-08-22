from django import forms


class WeatherForm(forms.Form):
    latitude = forms.CharField(required=True)
    longitude = forms.CharField(required=True)
    # temp_min = forms.IntegerField(required=False)
    # temp_min = forms.IntegerField(required=False)
    # humidity = forms.IntegerField(required=False)
    # wind_speed = forms.IntegerField(required=False)
    # description = forms.CharField(required=False)

    # def __init__(self, *args, **kwargs):
    #     super(WeatherForm, self).__init__(*args, **kwargs)
    #     self.fields['latitude'].initial = 0
    #     self.fields['longitude'].initial = 0
