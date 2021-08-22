from django.shortcuts import render, get_object_or_404
import requests
from .forms import WeatherForm

AUTH_TOKEN = "JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF"

# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def future(request):
    return render(request,'thefuture.html')

def feedback(request):
    return render(request,'feedback.html')

def weather(request):
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