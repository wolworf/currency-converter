import requests

api_key = "2aea0cd7887545a42810499fa7dea176"
url = "http://data.fixer.io/api/latest?access_key=" + api_key




first_currency = input("Birinci Para Birimi:")  # Örnek : USD
second_currency = input("İkinci Para Birimi:")  # Örnek : TRY
amount = int(input("Miktar:"))  # Örnek: 15

response = requests.get(url)

infos = response.json()

firstValue = infos["rates"][first_currency]
secondValue = infos["rates"][second_currency]

print((secondValue / firstValue) * amount)