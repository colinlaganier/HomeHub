import requests, json

def api_call():
	api_key = "87e3c3092c2a452c91c165654222307"
	api_url = 'http://api.weatherapi.com/v1/forecast.json'
	response = requests.get(api_url, params = {"key" : api_key, "q" : "London", "days" : 1, "aqi" : "yes", "alerts" : "no"})

	if response.status_code != 200:
		error_message = response.json()
		print(error_message.code + ": " + error_message.message)
		write_json(error_message, True)

	else:
		weather_data = response.json()
		write_json(weather_data, False)

def write_json(weather_data, error):
	with open(json_file, "r") as data_file:
	    data = json.load(data_file)

	if error:
		data["status"]["timestamp"] = round(time.time())
		data["status"]["error"] = 1
		data["status"]["error_code"] = weather_data.code
		data["status"]["error_message"] = weather_data.message
		data["weather_data"]["temperature"] = -1
		data["weather_data"]["weather"] = ""
		data["weather_data"]["precipitation"] = -1
		data["weather_data"]["air_quality"] = -1

	else:
		if data["status"]["error"] == 1:
			data["status"]["error"] = 0
			data["status"]["error_code"] = -1
			data["status"]["error_message"] = ""

		data["status"]["timestamp"] = weather_data["location"]["localtime_epoch"]
		data["weather_data"]["temperature"] = weather_data["current"]["temp_c"]
		data["weather_data"]["weather"] = weather_data["current"]["condition"]["text"];
		data["weather_data"]["precipitation"] = weather_data["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"]
		data["weather_data"]["air_quality"] = weather_data["current"]["air_quality"]["gb-defra-index"]

	with open(json_file, "w") as data_file:
	    json.dump(data, data_file)


if __name__ == "__main__":
	json_file = "weather_data.json"
	api_call()