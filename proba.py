import requests

url = "https://vedicrishi-horoscope-matching-v1.p.rapidapi.com/numero_table/"

payload = """{
  \"day\": \"25\",
  \"month\": \"12\",
  \"year\": \"1988\",
  \"hour\": \"2\",
  \"min\": \"30\",
  \"name\": \"demo\",
  \"lat\": \"25.123\",
  \"lon\": \"82.34\",
  \"tzone\": \"5.5\"
}"""
headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "vedicrishi-horoscope-matching-v1.p.rapidapi.com",
    'x-rapidapi-key': "ca48e96ac5msh7c3bf2c3aa86086p1fbc8ajsn2150edc4dc60"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
print(2)