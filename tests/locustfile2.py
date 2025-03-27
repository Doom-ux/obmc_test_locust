from locust import HttpUser, task, between
import json
from json import JSONDecodeError


class JsonPlaceholderUser(HttpUser):
	#host = "https://jsonplaceholder.typicode.com"
	wait_time = between(3, 5)

	@task 
	def get_resource_list(self):
		with self.client.get("/posts", verify=False, catch_response=True) as response:

			if response.status_code != 200:
				response.failure("Returned unsucccessful status")

			try:
				testdata_json = response.json()
				if type(testdata_json) is list:
					print("First post:")
					print(testdata_json[0])
					print("Number of posts:", len(testdata_json))
				else:
					print(testdata_json)

			except JSONDecodeError:
				response.failure("Response could not be decoded as JSON")


class WttrInUser(HttpUser):
	#host = "https://wttr.in"
	wait_time = between(3, 5)

	@task
	def get_weather(self):
		with self.client.get("/Novosibirsk", params={"format":"j1"}, verify=False, catch_response=True) as response:
			if response.status_code != 200:
				response.failure("Returned unsuccessful status")

			try:
				testdata_json = response.json()
				if type(testdata_json) is dict:
					print("Location:", testdata_json["nearest_area"][0]["areaName"][0]["value"])
					print("Date:", testdata_json["weather"][0]["date"])
					print("AVG temp(C):", testdata_json["weather"][0]["avgtempC"])
				else:
					print(testdata_json)

			except JSONDecodeError:
				response.failure("Response could not be decoded as JSON")

