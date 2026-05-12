###### Day 3 ############
import os
import requests
from dotenv import load_dotenv

############## KEY Protection ##################


load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")


############ start #####################
if __name__ == "__main__":
    city = "Lyon"
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url, verify=False, timeout = 10)
    data = response.json() #WHY how does .json work without importing json module ?
    print(data)

# temperature = data['list'][0]['main']['temp']-273.15
# description = data['list'][0]['weather'][0]['description']

# print(f"Right now {city}'s weather is {description} and the temperature is {temperature}")

# temperature_in24 = data['list'][8]['main']['temp']-273.15
# description_in24 = data['list'][8]['weather'][0]['description']

# print(f"In 24 hours, {city}'s weather will be {description_in24} and the temperature will be {temperature_in24}")

def get_weather_in_city_hours():
    try:
        city_funct = input("Enter the city name: ")
        hours = int(input("Enter the number of hours: "))
        if hours < 0:
            print("Cannot input a negative number to get weather in the past")
            return

        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_funct}&appid={API_KEY}"
        
        try:
            response = requests.get(url, verify=False, timeout = 10)
            datafunct = response.json()
        except requests.exceptions.Timeout:
            print("Timeout error occurred while fetching weather data.")
            return 
        except requests.exceptions.ConnectionError:
            print("Connection error occurred while fetching weather data.")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}") 
            return

        cod = datafunct.get("cod", None)
        if str(cod)!= "200":
            print(f"{city_funct} not found!")
            return

        temp = datafunct['list'][hours//3]['main']['temp']-273.15
        description = datafunct['list'][hours//3]['weather'][0]['description']
        print(f"In {hours} hours, {city_funct}'s weather will be {description} and the temperature will be {temp}")
    except ValueError:
        print("Invalid input. Please enter a valid number of hours (0 to 24).")
    except KeyError:
        print("Data not available for the specified city or hours.")
    except IndexError:
        print("Hours out of range.120 hours or 5 days are available.")
    # except:
    #     print("An error occurred in getting weather data. Please try again.")


def menu():
    print("1. Get weather for a city in specific hours")
    print("2. Exit")

if __name__ == "__main__":
    while True:
        menu()
        try:
            choice = int(input("What do you want this morning ?"))
            if choice == 1:
                get_weather_in_city_hours()
            elif choice == 2:
                print("Exiting the program.")
                break
        except ValueError:
            print("Invalid input in MENU. Please enter a valid number.")
            continue
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            pass

