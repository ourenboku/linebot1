from line_bot_api import *
from urllib.parse import parse_qsl


services = {
    1:{
        'catrgory':'上衣',
        'img_url':'https://12376876.imgur.com/all',
        'title':'上衣,洋裝,小可愛',
        'description':'日韓系上衣',
        'price':1500,
        'post_url':'https://www.facebook.com/jewel5562956/?locale=zh_TW'

    },
    2:{
        'catrgory':'裙子',
        'img_url':'https://12376876.imgur.com/all',
        'title':'上衣,洋裝,小可愛',
        'description':'日韓系上衣',
        'price':1500,
        'post_url':'https://www.facebook.com/jewel5562956/?locale=zh_TW'

    },
}

def service_category_event(event):
    image_carousel_template_message = TemplateSendMessage(
        alt_text='請選擇想服務類別',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://12376876.imgur.com/all',
                    action=PostbackAction(
                        label='上衣',
                        display_text='想了解上衣',
                        data='action=service&category=上衣'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://12376876.imgur.com/all',
                    action=PostbackAction(
                        label='裙子',
                        display_text='裙子',
                        data='action=service&category=裙子'
                    )
                )
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        [image_carousel_template_message])

def servicce_event(event):

    data= dict(parse_qsl(event.postback.data))

    bubbles=[]


    for service_id in services:
        if services[service_id]['category'] == data['category']:
            service = services[service_id]
            bubble = {
              "type": "bubble",
              "hero": {
                "type": "image",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "url": service['img_url']
              },
              "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "text",
                    "text": service['title'],
                    "wrap": True,
                    "weight": "bold",
                    "size": "xl"
                  },
                  {
                    "type": "text",
                    "text": service['duration'],
                    "size": "md",
                    "weight": "bold"
                  },
                  {
                    "type": "text",
                    "text": service['description'],
                    "margin": "lg",
                    "wrap": True
                  },
                  {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                      {
                        "type": "text",
                        "text": f"NT$ {service['price']}",
                        "wrap": True,
                        "weight": "bold",
                        "size": "xl",
                        "flex": 0
                      }
                    ],
                    "margin": "xl"
                  }
                ]
              },
              "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "button",
                    "style": "primary",
                    "action": {
                      "type": "postback",
                      "label": "預約",
                      "data": f"action=select_date&service_id={service_id}",
                      "displayText": f"我想預約【{service['title']} {service['duration']}】"
                    },
                    "color": "#b28530"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "uri",
                      "label": "了解詳情",
                      "uri": service['post_url']
                    }
                  }
                ]
              }
            }

            bubbles.append(bubble)
    flex_message = FlexSendMessage(
        alt_text='請選擇查看項目',
        contents={
            "type":"carousel",
            "contents":bubbles
        }
    )

    line_bot_api.reply_message(
        event.reply_token,
        [flex_message]
    )