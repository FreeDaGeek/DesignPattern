class Page(object):
    def __init__(self):
        self.__title = "What does the Fox say?"
        self.__css = "css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
    <title>{self.__title}</title>
    <link href="{self.__css}" rel ="stylesheet" type="text/css" />
    </head>
    <body>
    """
        self.body = "<h1>What does the Fox say?</h1><nav><ul><li>Panther</li><li>Dolphin</li><li>Fox</li></ul></nav>"
        self.close = """
    </body>
</html>
        """
        self.whole_page =""

    def update(self):
        self.whole_page = self.head + self.body + self.close
        self.whole_page = self.whole_page.format(**locals())
        ""

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @property
    def css(self):
        return self.__css

    @css.setter
    def css(self, new_css_file):
        self.__css = new_css_file
