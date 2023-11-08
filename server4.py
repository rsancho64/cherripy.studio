#! /usr/bin/python3

import random
import string

import cherrypy


class StringGenerator(object):

    @cherrypy.expose
    def index(self):
        return """
        <html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <input type="text" value="8" name="length" />
              <button type="submit">go!</button>
            </form>
          </body>
        </html>
        """

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':
    """
    CherryPy is a web FW upon which you build webapps.
    A traditional shape taken by apps: A HTML UI speaking to a server.
    Now handle HTML forms.
    .
    In this example, the form uses `GET` method and when you pressed the `go!`button,
    the form is sent using the same URL as in the previous (3rd) tutorial.
    HTML forms also support the `POST` method, in that case the query-string 
    is not appended to the URL but it sent to the server as the body of the client's request.
    However, this would not change your app's exposed method because CherryPy handles both the same way 
    and uses the exposed's handler parameters to deal with the query-string (key, value) pairs.
    """
    cherrypy.quickstart(StringGenerator())
