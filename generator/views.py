from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage

from generator.models import *
from generator.picture_recognize import *
from generator.poem import *

import random

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):  # 設定 LINE Bot 的回應
#              
                
                if event.message.type=='image':

                    image_content = line_bot_api.get_message_content(event.message.id)
                    path='./static/'+'tmp.jpg'
                    with open(path, 'wb') as fd:
                        for chunk in image_content.iter_content():
                            fd.write(chunk)
                    name = picture_recognize(path)  # 先得到辨識結果
                    poem_generate_result = poem_generate(name)  # 再產生詩句
                    message=[]
                    message.append(TextSendMessage(text='動物辨識結果：%s'%(name)))
                    message.append(TextSendMessage(text='用%s作詩：%s'%(name,poem_generate_result)))
                    line_bot_api.reply_message(event.reply_token,message)  # 紀錄結果

        return HttpResponse()  # 回傳訊息
    else:
        return HttpResponseBadRequest()