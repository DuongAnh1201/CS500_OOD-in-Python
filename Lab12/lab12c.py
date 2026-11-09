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
            b = B(content, attributes)
            b.update(b)
            return b
        elif type_attr == "title":
            title = Title(content, attributes)
            title.update(title)
            return title
        elif type_attr == "head":
            head = Head(content, attributes)
            head.update(head)
            return head
        elif type_attr == "html":
            html = Html(content, attributes)
            html.update(html)
            return html
        elif type_attr == "div":
            div = Div(content, attributes)
            div.update(div)
            return div
        elif type_attr == "body":
            body = Body(content, attributes)
            body.update(body)
            return body
        else:
            raise ValueError(f"Invalid node type: {type_attr}")

class DebugNodeFactory(ABC):
    @abstractmethod
    def update(self, node: Node) -> None:
        pass
class B(Node, DebugNodeFactory):
    def update(self, node: Node) -> None:
        print(f"B node is created")
    def create_tag(self) -> str:
        return "b"

class Title(Node, DebugNodeFactory):
    def update(self, node: Node) -> None:
        print(f"Title node is created")
    def create_tag(self) -> str:
        return "title"

class Head(Node, DebugNodeFactory):
    def update(self, node: Node) -> None:
        print(f"Head node is created")
    def create_tag(self) -> str:
        return "head"

class Html(Node, DebugNodeFactory):
    def update(self, node: Node) -> None:
        print(f"Html node is created")
    def html(self) -> str:
        return "<!DOCTYPE html>" + super().html()
    def create_tag(self) -> str:
        return "html"

class Div(Node, DebugNodeFactory):
    def update(self, node: Node) -> None:
        print(f"Div node is created")
    def create_tag(self) -> str:
        return "div"

class Body(Node, DebugNodeFactory):
    def update(self, node: Node) -> None:
        print(f"Body node is created")
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