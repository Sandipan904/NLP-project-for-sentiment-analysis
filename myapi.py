

import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key('shZGR1vEDR7kamwpHvoCjpzDZpPNLC1xdRXya67GMvE')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response




