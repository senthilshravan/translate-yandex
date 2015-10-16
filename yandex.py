import requests
import requests.exceptions


class YandexTranslator(object):
    url = "https://translate.yandex.net/api/v1.5/tr.json/{endpoint}?"
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

    def convert(self, file):
        k = 10
        j = 0
        f = open(file, "r+")
        newfile = open("convertedfile.srt", "w+")
        # print(sentence)
        page = f.read()
        i = 0
        for sentence in page.splitlines():
            # Adding the timeline
            if j > k:
                break
            if i is 1:
                newfile.write(sentence)
                i = 0
                newfile.write("\n")
            else:
                flag = 0
                try:
                    digit = int(sentence)
                except ValueError:
                    flag = 1
                # Adding numbers
                if flag is 0:
                    i = 1
                    j = j + 1
                    newfile.write(sentence)
                    newfile.write("\n")
                    print(sentence)
                # Adding sentence
                if flag is 1:
                    newfile.write(self.trans("de", sentence, options=None)[0])
                    newfile.write("\n")
        f.close()
        newfile.close()

yt = YandexTranslator("trnsl.1.1.20151011T175944Z.f6a3de65607a853a.1899ccefa5b8eaf25acc983905132b5212f47a37")
yt.convert("YOUR SRT FILE")
