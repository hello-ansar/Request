from selenium import webdriver
from bs4 import BeautifulSoup

import requests


# путь к драйверу chrome
chromedriver = '/usr/local/bin/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument('headless')  # для открытия headless-браузера
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

url = 'https://yandex.ru'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Ищет все новости и записывает в переменную
news = soup.find_all('a', class_='home-link list__item-content list__item-content_with-icon '
                                 'home-link_black_yes')


# Выводит текст каждой новости (всего их 10)
for link in news:
    print(link.text)


# from twilio.rest import Client
#
#
# def msg_mom_and_dad(event=None, context=None):
#     # тут нужно использовать SID и токен аутентификации, которые вы получили на Twilio
#     twilio_sid = 'AC7bf65262bb4bd58d3ed9156fe54c15d9'
#     auth_token = '81b908eca00341b911c14c012b77b059'
#
#     whatsapp_client = Client(twilio_sid, auth_token)
#
#     # в этот словарь можно добавлять контактные сведения тех,
#     # кому вы хотите отправлять сообщения
#     contact_directory = {'Дэн': '+77787008084'}
#
#     for key, value in contact_directory.items():
#         msg_loved_ones = whatsapp_client.messages.create(
#             body='ТЫ храсавчег есь же{} !'.format(
#                 key),
#             from_='whatsapp:+14155238886',
#             to='whatsapp:' + value,
#
#         )
#
#         print(msg_loved_ones.sid)
#
#
# if __name__ == '__main__':
#     msg_mom_and_dad()

# import os
# from twilio.rest import Client
#
#
# # Your Account Sid and Auth Token from twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# # account_sid = os.environ['AC7bf65262bb4bd58d3ed9156fe54c15d9']
# # auth_token = os.environ['81b908eca00341b911c14c012b77b059']
# client = Client('AC7bf65262bb4bd58d3ed9156fe54c15d9', '81b908eca00341b911c14c012b77b059')
#
#
# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+17197668665',
#                      to='+77028574975'
#                  )
#
# print(message.sid)
