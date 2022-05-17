from googletrans import Translator
import random
import re
import requests

resp = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "text/plain"}).text
joke = resp
print(joke)

translator = Translator()

runs = int(input("How many times do you want to run this: "))

all_lang_codes = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'zh-CN', 'zh-TW', 'co', 'hr', 'cd', 'da', 'nl', 'en', 'eo', 'et', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'or', 'no', 'ny', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'te', 'th', 'tr', 'uk', 'ur', 'uz', 'cy', 'xh', 'zu']
hard_lang_codes = ['bn', 'my', 'el', 'hi', 'lo', 'ne', 'si', 'vi', 'ar', 'ja', 'zh-TW', 'ko', 'tr', 'or', 'en']

lang_types = [all_lang_codes, hard_lang_codes]
lang_codes = random.choice(lang_types)

for run_count in range(runs):
	dest_code = random.choice(lang_codes)
	joke = str(translator.translate(joke, dest=dest_code))
	joke = joke.split('ext=')[1].split(', pro')[0]
	#print(joke)

joke = str(translator.translate(joke, dest='en'))
joke = joke.split('ext=')[1].split(', pro')[0]
print(joke)

split_resp = resp.split(' ')
replacement_words = []

for randreplace in range(random.randint(2, int(len(split_resp) / 2))):
	rand_word = random.choice(split_resp)
	output_word = re.sub('[^0-9a-zA-Z ]+', '', rand_word)
	replacement_words.append(output_word.lower())
	split_resp[split_resp.index(rand_word)] = '_' * len(rand_word)

join_resp = ' '.join(split_resp)
answer = input('\nYour base:\n' + join_resp + '\nFill in the blanks - if there is more than one answer, separat id with a space (x y): ')

answer = re.sub('[^0-9a-zA-Z ]+', '', answer)
answers = answer.lower().split(' ')

if sorted(answers) == sorted(replacement_words):
	print('Correct! The answer was:\n' + resp)
else:
	print('Incorrect! The correct answer was:\n' + ', '.join(replacement_words))