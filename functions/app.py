import random
from flask import Flask, jsonify, request
import serverless_wsgi

app = Flask(__name__)

ANSWERS = [
    {"en": "The signal is clear: YES.", "mm": "အဖြေကတော့ 'ဟုတ်ကဲ့' ပါ။"},
    {"en": "The signal is blocked. Not now.", "mm": "အခုချိန်မှာ မဖြစ်နိုင်သေးပါဘူး။"},
    {"en": "The Universe requires action.", "mm": "လက်တွေ့လုပ်ဆောင်ဖို့ လိုအပ်ပါတယ်။"},
    {"en": "Proceed with caution.", "mm": "သတိထားပြီး လုပ်ဆောင်ပါ။"}
]

@app.route('/.netlify/functions/app/decode', methods=['POST'])
def decode():
    result = random.choice(ANSWERS)
    return jsonify(result)

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
