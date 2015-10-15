import requests
import requests.exceptions


class YandexTranslator(object):
    url = "https://translate.yandex.net/api/v1.5/tr.json/{endpoint}?"
    # =trnsl.1.1.20151011T175944Z.f6a3de65607a853a.1899ccefa5b8eaf25acc983905132b5212f47a37"
    key = ""
    function = ""
    dict = {"langs": "getLangs", "det": "detect", "trans": "translate"}

    def __init__(self, key=None):
        if key is None:
            raise KeyError
        self.key = key

    def getUrl(self, param):
        return self.url.format(endpoint=self.dict[param])

    def langs(self):
        response = ""
        try:
            response = requests.get(self.getUrl("langs"), params={"key": self.key})
            response = response.json()
            print(response.get("code", 200))
        except Exception as e:
            print(type(e))
        return response

    def detect(self, sentence):
        response = ""
        try:
            response = requests.get(self.getUrl("det"), params={"key": self.key, "text": sentence})
            response = response.json()
            print(response["code"])
        except Exception as e:
            print(type(e))
            print(e.args)
        return response["lang"]

    def trans(self, lang, sentence, options=None):
        # sentence = str(sentence.replace(self, " ", "+"))
        try:
            response = requests.get(self.getUrl("trans"), params={"key": self.key, "lang": lang, "text": sentence, "options": options})
            response = response.json()
            return response["text"]
        except Exception as e:
            print(type(e))

yt = YandexTranslator("trnsl.1.1.20151011T175944Z.f6a3de65607a853a.1899ccefa5b8eaf25acc983905132b5212f47a37")
print(yt.trans("ja", "what do you mean", 1))
