import paralleldots as pd

class API:

    pd.set_api_key('u1XpKY8SLGpEKTOMJhOwAd9BAQVONXbZO34hRjryuGc')

    def ner_analysis(self,text):
        res = pd.ner(text)
        return res

    def sentiments_analysis(self,text):
        res = pd.sentiment(text)
        return res

    def emotions_analysis(self,text):
        res = pd.emotion(text)
        return res

# ap =API()
# print(ap.ner_analysis("Apple was founded by Steve Jobs."))

