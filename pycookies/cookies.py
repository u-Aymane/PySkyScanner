class COOKIES:
    def __init__(self, text):
        self.text = text
        self.formated_cookies = {}

    def cookies_function(self):
        parts = self.text.split('; ')
        for i in parts:
            self.formated_cookies[i.split('=', 1)[0]] = i.split('=', 1)[1]

        return self.formated_cookies
