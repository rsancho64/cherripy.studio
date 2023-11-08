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
        Now: try <a href="http://localhost:8080/generate">http://localhost:8080/generate</a><br>
        and your browser will display a random string.
        """
        return content

    @cherrypy.expose
    def generate(self):
        """method to handle `/generate` route """        
        return ''.join(random.sample(string.hexdigits, 8))


if __name__ == '__main__':

    """Different URLs lead to different functions
    """
    cherrypy.quickstart(StringGenerator())


