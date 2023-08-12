from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import(
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent, StickerSendMessage, ImageSendMessage, LocationSendMessage
)

# Channel access token
line_bot_api = LineBotApi('Bt3t396iZROmq9J4tZRJelmiVuPen2S7qEPH53OWY8t6LtnWXjKYDnstsf2UgLRBcQgKQLXMt1GZUEkOSCaR6zA+g9g23xek/KL0TWituhFCyBqMIoWidcfOTTwaxMzrXbvEh5v66xCOyL50u5L/CQdB04t89/1O/w1cDnyilFU=')
# Channel secret 
handler = WebhookHandler('ce3610cc7e18921f9ba3219fea16f6ef')
