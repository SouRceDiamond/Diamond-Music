import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "14679741"))
    API_HASH = os.environ.get("API_HASH", "fd2513e47faa7e45f40cb0370f05151b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5418940211:AAGtltrwmr6ePhBYx6Ay3wVNIzL-07dpzoQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BACAq6qSgw7KnYAwjlyus9XR7b3EKLUxmHgem7zxxtpFO28OHc0XWG8XEA-o6yiN1N5b0awAOyqiVz0P77hKoLUXZDcd1WyCeu2WYJkUyVH34HCifoKGbZKYU90Ebde8YxR_fzrbM2aNh4eu3HgwO7LvwXbP0TttLDWmsyTQRvimGgDPg5X3qy3lMqRRVoa-xLIeT_PCTQyKx8WW_6eg-5EJGVdw6bsWu2Jb1WWK_asMlMf5clDuu4cH37IqEKaqV3XTOgOu6hrw2TLcMdjJ4velTr5WUP84EWUk4NSXlwfeQHweedfQ2DlBfTbWtr3ug7Q2AW0Gv5ClU8-ScR0ZDzReAAAAAT65H3QA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "bdggdbbot")
    SUPPORT = os.environ.get("SUPPORT", "bajwkk")
    CHANNEL = os.environ.get("CHANNEL", "CR_T2")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/c41c41a1b48e64fea51c9.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/c41c41a1b48e64fea51c9.jpg")