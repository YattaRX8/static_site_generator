from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    node2 = HTMLNode("p", "Test string", None, {"href": "https://www.google.com"})
    leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    html_child = HTMLNode("div", "Littel baby node", None, {"href": "https://www.github.com"})
    node2.children = html_child
    parent_child = LeafNode("b", "Don't click me")
    parent_node = ParentNode("a", [parent_child], {"href": "https://www.youtube.com"})
    parent_node.children.append(parent_child)
    node_convert = text_node_to_html_node(node)
    split_test = TextNode("`This` is text `with` a code block `word`", TextType.TEXT)
    split_test = split_nodes_delimiter([split_test], "`", TextType.CODE)
    print(node)
    print(node2)
    print(node2.children)
    print(html_child)
    print(leaf)
    print(leaf.to_html())
    print(parent_child.to_html())
    print(parent_node.to_html())
    print(node_convert)
    print(node_convert.to_html())
    print(split_test)
    print(extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"))
    print(extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"))
main()