import requests
import json
import time

import constants


def main():
    while True:
        url = constants.URL.format(token=constants.TOKEN, method=constants.UPDATE_METHOD)
        content = requests.get(url).text

        data = json.loads(content)
        # print(data)
        result = data['result'][::-1]
        needed_part = None

        for elem in result:
            if elem['message']['chat']['id'] == constants.MY_ID:
                needed_part = elem
                break

        if constants.UPDATE_ID != needed_part['update_id']:
            message = get_message(needed_part)
            msg = get_weather(message)
            answer_user_bot(msg)
            save_update_id(needed_part)

        time.sleep(1)


def answer_user_bot(data):
    data = {
        'chat_id': constants.MY_ID,
        'text': data
    }
    url = constants.URL.format(
        token=constants.TOKEN,
        method=constants.SEND_METHOD
    )
    response = requests.post(url, data=data)


def parse_weather_data(data):
    for elem in data['weather']:
        weather_state = elem['main']
    temp = round(data['main']['temp'], 1)
    city = data['name']
    msg = f'The weather in {city} now:\nTemperature is {temp}°C\nState is {weather_state}'
    return msg


def get_weather(location):
    url = constants.WEATHER_URL.format(city=location, token=constants.WEATHER_TOKEN)
    response = requests.get(url)
    if response.status_code != 200:
        return 'city not found'
    data = json.loads(response.content)
    return parse_weather_data(data)


def get_message(data):
    return data['message']['text']


def save_update_id(update):
    with open(constants.UPDATE_ID_FILE_PATH, 'w') as file:
        file.write(str(update['update_id']))
    constants.UPDATE_ID = update['update_id']
    return True


if __name__ == '__main__':
    main()
