# This is a sample Python script.

# '7142488802:AAFoZz3eFOAEqqJshQTEO5LqgTQ5TEw87zk'
# 'AIzaSyAvKhOWPhDi6UwCBZaGXh_Hr1edJkkGX3w' genai

import telebot
import google.generativeai as genai
from telebot import types
from PyPDF2 import PdfReader
import re
import os
import PyPDF2
TOKEN = '7142488802:AAFoZz3eFOAEqqJshQTEO5LqgTQ5TEw87zk'
bot = telebot.TeleBot(TOKEN)







"""


import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./nlmatics-1f123f7481dd.json"

import vertexai
vertexai.init(project="nlmatics", location="us-central1")

from vertexai.preview.generative_models import GenerativeModel

def run_prompt(prompt_text, context_text):
  model = GenerativeModel("gemini-pro")
  responses = model.generate_content(f"{prompt_text}\n{context_text}", stream=False)
  return responses.candidates[0].content.parts[0].text

from llmsherpa.readers import LayoutPDFReader
pdf_url = "law_example_2.pdf"
llmsherpa_api_url = "https://readers.llmsherpa.com/api/document/developer/parseDocument?renderFormat=all"
# pdf_url = "https://arxiv.org/pdf/1910.13461.pdf" # also allowed is a file path e.g. /home/downloads/xyz.pdf
pdf_reader = LayoutPDFReader(llmsherpa_api_url)
doc = pdf_reader.read_pdf(pdf_url)


"""











# Configure GenAI
genai.configure(api_key='AIzaSyAvKhOWPhDi6UwCBZaGXh_Hr1edJkkGX3w')
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
# Открываем PDF-файл
# Открываем PDF-файл

with open('law_example.pdf', 'rb') as file:
    # Создаем объект для чтения PDF
    reader = PyPDF2.PdfReader(file)

    # Инициализируем переменную для хранения содержимого PDF
    pdf_text = ''

    # Читаем содержимое каждой страницы и добавляем его в переменную
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        pdf_text += page.extract_text()
print(pdf_text)


response = chat.send_message(f"Referring only to this variable {pdf_text} answer the following question question. If you undestand write 'okay'")
result_text = response._result.candidates[0].content.parts[0].text
print(result_text)

#
# Load the PDF file containing laws
def search_pdf(query):
    pdf_file_path = os.path.join('C:', os.sep, 'Users', 'User', 'Downloads',
                                 'laws_example.pdf')  # Replace with your absolute path
    with open(pdf_file_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()

    # Search for the query in the PDF text
    matches = re.findall(f'\\b{query}\\b', text, re.IGNORECASE)
    if matches:
        return ' '.join(matches)
    else:
        return 'No answer found.'


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Привет! Я бот-консультант по трудовому законодательству Республики Казахстан. Пожалуйста, опишите свою проблемную ситуацию или правонарушение, и я постараюсь найти соответствующие статьи в PDF.")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_query = message.text

    global chat
    response = chat.send_message(user_query)
    answer = response._result.candidates[0].content.parts[0].text

    bot.reply_to(message, answer)


bot.polling()
