from flask import Flask, render_template, request
from weather import getWeather
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
  return render_template("index.html")

@app.route('/weather')
def getWeatherFromUser():
  city = request.args.get('city')

  # Check for empty string. 
  if not bool(city.strip()):
    city = "Irosin"
  weather_data = getWeather(city)

  # if city not found
  if not weather_data['cod'] == 200:
    return render_template("city-not-found.html")


  return render_template(
    "weather.html",
    title = weather_data["name"],
    status = weather_data["weather"][0]["description"].capitalize(),
    feels_like = f"{weather_data['main']['feels_like']:.1f}",
    temp = f"{weather_data['main']['temp']:.1f}"
  )

if __name__ == "__main__":
  serve(app, host="0.0.0.0", port=8001)
  # app.run(host="0.0.0.0", port=8001)