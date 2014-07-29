class Page(object):
    def __init__(self):
        self.title = "What does the Fox say?"
        self.header = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>What does the FOX say?</title>
        <link rel="stylesheet" href="css/style.css" type="text/css" />
    </head>
    <body>
        <div id = "container">
        <h1>What does the fox say?</h1> '''

        self.links = '''
        <nav>
            <ul>
                <a href=?animals=0" + array[0] + "><button class='first'>Panther</button></br>
                <a href=?animals=1" + array[1] + "><button class='second'>Dolphin</button></br>
                <a href=?animals=2" + array[2] + "><button class='third'>Fox</button>
            </ul>
        </nav>
        '''
        self.footer = '''
    </body>

    <footer>
    <p>Copyright &copy; 2014 What does the FOX say?</p>
    </footer>
    </div><!-- closes "container" div -->
</html>
        '''

    def header(self):
        return self.header

    def links(self):
        return self.links

    def footer(self):
        return self.footer