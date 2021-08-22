from django.shortcuts import render, get_object_or_404
import requests
from .forms import WeatherForm

AUTH_TOKEN = "JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF"

#
# res = requests.get('https://ipinfo.io/')
# data = res.json()
# city = data['city']
# location = data['loc'].split[',']
# latitude = location[0]
# longitude = location[1]
#
# print("Latitude: ", latitude)
# print("Longitude: ", longitude)
# print("City: ", city)

# latitude = 54.4609
# longitude = views.py
# latitude = 0
# longitude = 0

# #url = 'https://api.openweathermap.org/data/2.5/weather?q=Berlin&APPID=f085ab04c05267ccd1670d5c7bc802f7'
# url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=f085ab04c05267ccd1670d5c7bc802f7'.format(latitude,longitude)
# res = requests.get(url)
# data = res.json()
# temp_min = data['main']['temp_min']
# temp_max = data['main']['temp_max']
# humidity = data['main']['humidity']
# wind_speed = data['wind']['speed']
# latitude = data['coord']['lat']
# longitude = data['coord']['lon']
# description = data['weather'][0]['description']
# city = data['name']
#
# print('Temperature Min : {} degree celcius'.format(temp_min))
# print('Temperature Max : {} degree celcius'.format(temp_max))
# print('Humidity : {}'.format(humidity))
# print('Wind Speed : {} m/s'.format(wind_speed))
# print('Latitude : {}'.format(latitude))
# print('Longitude : {}'.format(longitude))
# print('Description: {}'.format(description))
# print('City: {}'.format(city))

# Create your views here.
def weather(request):

    # url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=f085ab04c05267ccd1670d5c7bc802f7'.format(
    #     latitude, longitude)
    # res = requests.get(url)
    # data = res.json()
    # temp_min = data['main']['temp_min']
    # temp_max = data['main']['temp_max']
    # humidity = data['main']['humidity']
    # wind_speed = data['wind']['speed']
    # latitude = data['coord']['lat']
    # longitude = data['coord']['lon']
    # description = data['weather'][0]['description']
    latitude = 0
    longitude = 0
    if request.POST:
        form = WeatherForm(request.POST)
        if form.is_valid():
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
    url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID=f085ab04c05267ccd1670d5c7bc802f7'.format(
        latitude, longitude)
    res = requests.get(url)
    data = res.json()
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']
    city = data['name']
        # else:
        #     latitude = 0
        #     longitude = 0
        #     temp_min = 0
        #     temp_max = 0
        #     humidity = 0
        #     wind_speed = 0
        #     description = ''
        #     city = ''

    form = WeatherForm()
    return render(request, 'form.html', {'form': form, 'latitude': latitude, 'longitude': longitude, 'temp_min': temp_min, 'temp_max': temp_max, 'humidity': humidity, 'wind_speed': wind_speed, 'description': description, 'city': city})


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'weatherapp/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'weatherapp/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'weatherapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('weatherapp:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'weatherapp/results.html', {'question': question})

def authenticate(token):
    if token == AUTH_TOKEN:
        return True
    else:
        return False