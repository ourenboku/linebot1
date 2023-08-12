from line_bot_api import *


def about_us_event(event):
    emoji = [
        {
            "index": 0,
            "productId": "5ac21184040ab15980c9b43a",
            "emojiId": "225"
        },
        {
            "index": 13,
            "productId": "5ac21184040ab15980c9b43a",
            "emojiId": "225"
        }
    ]

    text_message = TextSendMessage(text='''$ 寶石服飾 $

-嚴格把關：所有用品皆有嚴格把關

-可以試穿:來店皆可試穿衣物
                                   
。''', emojis=emoji)

    sticker_message = StickerSendMessage(
        package_id='8522',
        sticker_id='16581271'
    )

    about_us_img = 'https://i.imgur.com/33pk0Iw.jpeg'

    image_message = ImageSendMessage(
        original_content_url=about_us_img,
        preview_image_url=about_us_img
    )

    line_bot_api.reply_message(
        event.reply_token,
        [text_message, sticker_message, image_message])
    
def location_event(event):
    location_message = LocationSendMessage(
        title='寶石服飾',
        address='高雄市新興區文化路81號',
        latitude=25.034563695,
        longitude=121.5738839
    )

    line_bot_api.reply_message(
        event.reply_token,
        location_message)