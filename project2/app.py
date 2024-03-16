from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO
import Adafruit_DHT
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
GPIO.setup(11, GPIO.OUT)

DHT_PIN = 4
DHT_SENSOR = Adafruit_DHT.DHT11
app = Flask(__name__)


def get_sensor_reading():  
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    humidity_val=30
    temperature_val=30
    if humidity is not None and temperature is not None:
        humidity_val=humidity
        temperature_val=temperature
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        humidity_val=humidity_val
        temperature_val=temperature_val
        print("Sensor failure. Check wiring.")
    return (temperature_val, humidity_val)
        
@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/sensorReadings")
def get_sensor_readings():
    temperature, humidity = get_sensor_reading()
    return jsonify(
        {
            "status": "OK",
            "temperature": temperature,
            "humidity": humidity,
        }
    )

if __name__ == '__main__':
    app.run(debug=True, host='172.20.10.6')
