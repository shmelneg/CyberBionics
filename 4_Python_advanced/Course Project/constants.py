TOKEN = '5535479187:AAFZ65Q_OkXYOTxZWEQK0gkZdRRqNoRCySs'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METHOD = 'getUpdates'
SEND_METHOD = 'sendMessage'

MY_ID = 371757708

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data

WEATHER_TOKEN = '9a8d6034d5b66debcda7ebd616496f4e'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric&lang=ua'
