import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        
        child = HTMLNode(
            "p",
            "Little baby node",
        )
        node.children = child

        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            child,
        )
        self.assertEqual(
            node.props,
            None,
        )
        self.assertEqual(
            node.children.tag,
            "p",
            child.tag,
        )
        self.assertEqual(
            node.children.value,
            "Little baby node",
            child.value,
        )
    

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        child = HTMLNode(
            "div",
            "Hello world",
            None,
            {"class": "secondary"}
        )
        node.children = child
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: HTMLNode(div, Hello world, children: None, {'class': 'secondary'}), {'class': 'primary'})",
        )
        self.assertEqual(
            node.children.__repr__(),
            "HTMLNode(div, Hello world, children: None, {'class': 'secondary'})",
            child.__repr__(),
        )


if __name__ == "__main__":
    unittest.main()
