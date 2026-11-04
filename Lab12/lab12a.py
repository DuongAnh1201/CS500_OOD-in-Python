from __future__ import annotations
from abc import ABC, abstractmethod

class Node(ABC):
    def __init__(self, content = "", attributes: dict[str:str] = {}) -> None:
        self._content = content
        self._attributes = attributes
        self._children: list[Node] = []
    
    #Factory method
    @abstractmethod
    def create_tag(self):
        pass

    def html(self) -> str:
        output = "<" + self.create_tag()
        for k, v in self._attributes.items():
            output += " " + k +"=\"" + v + "\""
        output += ">"
        for child in self._children:
            output += child.html()
        output += self._content
        output += "</"+ self.create_tag()+ ">"
        return output
        
    def appendChild(self, child: Node) -> None:
        if child not in self._children:
            self._children.append(child)

class B(Node):
    def create_tag(self) -> str:
        return "b"

class Title(Node):
    def create_tag(self) -> str:
        return "title"

class Head(Node):
    def create_tag(self) -> str:
        return "head"

class Html(Node):
    def html(self) -> str:
        return "<!DOCTYPE html>" + super().html()
    def create_tag(self) -> str:
        return "html"

class Div(Node):
    def create_tag(self) -> str:
        return "div"

class Body(Node):
    def create_tag(self) -> str:
        return "body"



def main():
    divAtts = {}
    divAtts['id'] = 'first'
    divAtts['class'] = 'foo'
    divA = Div('This is a test A', divAtts)
    divAtts = {}
    divAtts['id'] = 'second'
    divAtts['class'] = 'bar'
    divB = Div('This is a test B', divAtts)
    divAtts = {}
    divAtts['id'] = 'third'
    divAtts['class'] = 'dump'
    divC = Div('This is a test C', divAtts)

    b = B('This is a simple HTML file')
    divC.appendChild(b)
    body = Body()
    body.appendChild(divA)
    body.appendChild(divB)
    body.appendChild(divC)
    title = Title('Example')
    head = Head()
    head.appendChild(title)
    htmlAtts = {}
    htmlAtts['lang'] = 'en'
    html = Html('', htmlAtts)
    html.appendChild(head)
    html.appendChild(body)
    print(html.html())

if __name__ == "__main__":
    main()