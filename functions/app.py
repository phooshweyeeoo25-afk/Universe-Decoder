import random
from flask import Flask, jsonify
import serverless_wsgi

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

ANSWERS = [
    {"en": "The signal is clear: YES. Success and positive energy surround your question.", "mm": "အဖြေကတော့ 'ဟုတ်ကဲ့/အောင်မြင်ပါလိမ့်မယ်'။ အဆင်ပြေချောမွေ့မှုတွေ ရရှိလာတော့မှာပါ။"},
    {"en": "The signal is blocked. Now is not the right time. Re-evaluate your direction.", "mm": "အဖြေကတော့ 'မဖြစ်နိုင်သေးပါ'။ အခုချိန်ဟာ အဆင်သင့်မဖြစ်သေးလို့ ပြန်လည်စဉ်းစားပေးပါ။"},
    {"en": "The Universe requires action. The answer depends on your next choice.", "mm": "လုပ်ဆောင်ချက်အပေါ်မှာပဲ မူတည်ပါတယ်။ သင့်ရဲ့ ဆုံးဖြတ်ချက်က အဖြေကို ပြောင်းလဲပေးပါလိမ့်မယ်။"},
    {"en": "Proceed with caution. There are hidden details you haven't seen yet.", "mm": "သတိထားပြီး လုပ်ဆောင်ပါ။ သင်မမြင်ရသေးတဲ့ လျှို့ဝှက်ချက်တွေ ရှိနေနိုင်ပါတယ်။"},
    {"en": "A flow of energy is coming. Expect a breakthrough in your path soon.", "mm": "တိုးတက်မှုတွေ ရရှိလာတော့မှာပါ။ မကြာခင်မှာ အခွင့်အရေးကောင်းတွေ ရရှိပါလိမ့်မယ်။"}
]

@app.route('/decode', methods=['POST'])
def decode():
    result = random.choice(ANSWERS)
    return jsonify(result)

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)
