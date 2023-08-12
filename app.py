from flask import Flask, request, abort 

from events.basic import *
from line_bot_api import *



app = Flask(__name__)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):

    message_text=str(event.message.text).lower()

    if message_text =="@關於我們":
        about_us_event(event)

    elif message_text=="@營業據點":
        location_event(event)

@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = """Hello 您好,歡迎成為 寶石服飾 的好友!
    
我是 寶石服飾 的小幫手

-想預約來店取件可以直接跟我互動喔
-直接點選下方的選單功能

-期待你的光臨
"""
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg)
    )


    
@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)


if __name__ =="__main__":
    app.run()