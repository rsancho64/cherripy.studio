#! /usr/bin/python3

import random
import string

import cherrypy


class StringGenerator(object):

    @cherrypy.expose
    def index(self):
        """method to handle `/` route """
        content = """
        Hello world!</br>
        Now: try <a href="http://localhost:8080/generate?length=LENGTH">http://localhost:8080/generate</a><br>
        with LENGTH as short unsigned integer
        and your browser will display a random string with that LENGTH
        """
        return content

    # @cherrypy.expose
    # def generate(self):
    #     """method to handle `/generate` route """
    #     return ''.join(random.sample(string.hexdigits, 8))

    @cherrypy.expose
    def generate(self, length=8):
        return ''.join(random.sample(string.hexdigits, int(length)))


if __name__ == '__main__':

    """now, URLs w parameters
    """
    cherrypy.quickstart(StringGenerator())
