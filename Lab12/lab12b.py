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

class AbstractNodeFactory(ABC):
    @abstractmethod
    def make_node(self, type_attr:str,content = "", attributes:dict[str:str] = {}) -> Node:
        pass
class StandardNodeFactory(AbstractNodeFactory):
    def make_node(self, type_attr:str, content = "", attributes:dict[str:str] = {}) -> Node:
        if type_attr == "b":
            return B(content, attributes)
        elif type_attr == "title":
            return Title(content, attributes)
        elif type_attr == "head":
            return Head(content, attributes)
        elif type_attr == "html":
            return Html(content, attributes)
        elif type_attr == "div":
            return Div(content, attributes)
        elif type_attr == "body":
            return Body(content, attributes)
        else:
            raise ValueError(f"Invalid node type: {type_attr}")

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
    factory = StandardNodeFactory()
    div = factory.make_node("div", "This is a test A", {"id": "first", "class": "foo"})
    div2 = factory.make_node("div", "This is a test B", {"id": "second", "class": "bar"})
    div3 = factory.make_node("div", "This is a test C", {"id": "third", "class": "dump"})
    b = factory.make_node("b", "This is a simple HTML file")
    div3.appendChild(b)
    body = factory.make_node("body")
    body.appendChild(div)
    body.appendChild(div2)
    body.appendChild(div3)
    title = factory.make_node("title", "Example")
    head = factory.make_node("head")
    head.appendChild(title)
    html = factory.make_node("html", "", {"lang": "en"})
    html.appendChild(head)
    html.appendChild(body)
    print(html.html())

if __name__ == "__main__":
    main()