#! /usr/bin/python3

import random
import string

import cherrypy

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="8" name="length" />
              <button type="submit">set random value now!</button>
            </form>
          see <a href="http://localhost:8080/display">http://localhost:8080/display</a> <br>
          AFTER choose lenght (error if not)
          </body>
        </html>
        """

    @cherrypy.expose
    def generate(self, length=8):
        some_string = ''.join(random.sample(string.hexdigits, int(length)))
        cherrypy.session['mystring'] = some_string
        return some_string + """<br>
        Now you can go to <a href="http://localhost:8080">http://localhost:8080/</a>
        """

    @cherrypy.expose
    def display(self):
        return "session-id: " + cherrypy.session['mystring']

if __name__ == '__main__':
    """
    usually apps needs to follow the user’s activity for a while.
    The usual mechanism: session-id carried during conversation.
    """
    conf = {
        '/': {
            'tools.sessions.on': True
        }
    }
    cherrypy.quickstart(StringGenerator(), '/', conf)
