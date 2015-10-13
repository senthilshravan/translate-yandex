import requests
import requests.exceptions


class YandexTranslator(object):
    url = "https://translate.yandex.net/api/v1.5/tr.json/{endpoint}"
    key = ""
    function = ""
    dict = {"langs": "getLangs", "det": "detect", "trans": "translate"}

    def __init__(self, key=None, func="detect"):
        self.function = func
        if key is None:
            raise KeyError
        self.key = key

    def getUrl(self, param):
        return self.url.format(endpoint=self.dict[param])

    def langs(self):
        try:
            response = requests.get(self.getUrl("langs"), params={"key": self.key})
        except Exception as e:
            print(type(e))
        return response

yt = YandexTranslator("trnsl.1.1.20151011T175944Z.f6a3de65607a853a.1899ccefa5b8eaf25acc983905132b5212f47a37")
print(yt.langs())
