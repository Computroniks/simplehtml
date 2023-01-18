# SPDX-FileCopyrightText: 2023 Matthew Nickson < mnickson@sidingsmedia.com >
# SPDX-License-Identifier: MIT

from abc import ABC


class Element(ABC):
    """
    Element Base HTML element

    :param tag: HTML tag for this element
    :type tag: str
    :param attributes: HTML attributes for this element
    :type attributes: str
    """

    tag = ""
    name_mapping = {}

    def __init__(self, **kwargs) -> None:
        """
        __init__ Constructor method
        """

        self._children = []

        # TODO: Validate attributes
        self.attributes = kwargs

    def __str__(self) -> str:
        """
        __str__ Return string representation of element and all children

        :return: Element
        :rtype: str
        """

        return f"<{self.tag}{self.get_attributes()}>{''.join(self._children)}</{self.tag}>"

    def get_attributes(self) -> str:
        """
        get_attributes Get attributes string

        :return: Formatted attributes
        :rtype: str
        """

        output = []
        for attribute, value in self.attributes.items():
            if value != "" and value is not None:
                if attribute in self.name_mapping:
                    output.append(
                        f"{self.name_mapping[attribute]}=\"{value}\"")
                else:
                    output.append(
                        f"{attribute}=\"{value}\"")
        if len(output) == 0:
            return ""

        # Extra space for gap between tag and attribute
        return " " + " ".join(output)

    def render(self) -> str:
        """
        render Render this element

        This is just a wrapper for the __str__ method for this class

        :return: Rendered HTML
        :rtype: str
        """

        return str(self)


class VoidElement(Element, ABC):
    """
    VoidElement Void elements
    """

    def __str__(self) -> str:
        """
        __str__ Return string representation of element and all children

        :return: Element
        :rtype: str
        """

        return f"<{self.tag}{self.get_attributes()} />"
