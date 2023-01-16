# SPDX-FileCopyrightText: 2023 Matthew Nickson < mnickson@sidingsmedia.com >
# SPDX-License-Identifier: MIT

from standalonehtml.elements.element import Element, VoidElement


class Base(VoidElement):
    """
    Base Specify base URL to use for all relative URLs in document
    """

    tag = "base"

    def __init__(self, href: str = "", target: str = "") -> None:
        """
        __init__ Constructor method

        :param href: Base URL to be used, defaults to
        :type href: str
        :param target: Default browsing context, defaults to ""
        :type target: str, optional
        """

        super().__init__(href=href, target=target)


class Link(VoidElement):
    """
    Link Specify relationships between documents
    """

    tag = "link"


class Meta(VoidElement):
    """
    Meta Represent metadata that cannot be represented by other elements
    """

    tag = "meta"
    name_mapping = {
        "http_equiv": "http-equiv"
    }


class Style(Element):
    """
    Style Inline style
    """

    tag = "style"

    def __init__(self, css: str, **kwargs) -> None:
        """
        __init__ Constructor method

        :param css: CSS to insert
        :type css: str
        """

        super().__init__(**kwargs)
        self._children.append(css)


class Title(Element):
    """
    Page title
    """

    tag = "title"

    def __init__(self, title: str, **kwargs) -> None:
        """
        __init__ Constructor method

        :param title: Title of page
        :type title: str
        """

        super().__init__(**kwargs)
        self._children.append(title)
