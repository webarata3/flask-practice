from flask import Markup

if __name__ == '__main__':
    print(Markup('<strong>Hello {}!</strong>'.format('<blink>hacker</blink>')))
    print(Markup.escape('<blink>hacker</blink>'))
    print(Markup('<em>Marked up</em> &raquo; HTML').striptags())
