from math import floor
import requests
import json
import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv
import datetime

PORT = 587
EMAIL_SERVER = "smtp-mail.outlook.com"  # Adjust server address, if you are not using @outlook

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()  # give the current dir
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("PASSWORD")
API_KEY = os.getenv("API_KEY")
receiver_email = os.getenv('RECEIVER_EMAIL')


def send_email(subject: str, receiver_email: str, message: str) -> None:
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Weather", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(message)

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


def fahrenheit_to_celsius(temp_fahrenheit: float) -> float:
    """Converts Fahrenheit to Celsius
    Doctest:
    >>> fahrenheit_to_celsius(32)
    0.0
    >>> fahrenheit_to_celsius(212)
    100.0
    """
    temp_celsius = (temp_fahrenheit - 32) * 5 / 9
    return temp_celsius


def create_message():
    # Specify the city and number of days for which you want to get the weather forecast
    city = "Tel Aviv"

    # Use the OpenWeatherMap API to get the weather forecast for the specified city
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=imperial")

    # Parse the response
    data = json.loads(response.text)

    # The weather of today
    weather = data['list']  # all the details.

    # 3 -> 09:00 AM , 4 -> 12:00 PM , 5 -> 15:00 PM

    all_day_details = [weather[3], weather[4],
                       weather[5]]  # each item contains all the details of the weather in the current day


    # Get the current date
    today = str(datetime.date.today())

    date = datetime.datetime.strptime(today, '%Y-%m-%d').strftime(
        '%d/%m/%Y')  # date of the weather in the format of dd/mm/yyyy.

    # Initialize a string to hold the weather forecast
    forecast = f"Hey Baby, Good evening\nToday is the {date}\nThe weather tomorrow in {city}\n"

    # Get the date, temperature, and weather description for the current day
    for hour in all_day_details:
        print(hour)
        temp = floor(fahrenheit_to_celsius(hour['main']['temp']))  # temperature in celsius.
        description = hour['weather'][0]['description']
        time = hour['dt_txt'][11:]  # time of the weather
        forecast += f"• In {time[:-3]} temp -> {temp}°C and will be {description}\n"

    forecast += "Love You :)"

    """
    Example of the final message:
    Hey Baby, Good evening
    Today is the 20/09/2021
    The weather tomorrow in Tel Aviv
    • In 09:00 temp -> 24°C and will be broken clouds
    • In 12:00 temp -> 26°C and will be broken clouds
    • In 15:00 temp -> 22°C and will be broken clouds
    """

    return forecast  # final message


if __name__ == '__main__':
    create_message()
