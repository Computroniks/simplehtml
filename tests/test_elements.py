# SPDX-FileCopyrightText: 2023 Matthew Nickson < mnickson@sidingsmedia.com >
# SPDX-License-Identifier: MIT

# pylint: disable=line-too-long, missing-class-docstring, wildcard-import
# pylint: disable=missing-function-docstring, unused-wildcard-import

from standalonehtml.elements.metadata import *


class TestMetadata:
    def test_base_href(self):
        base = Base(href="https://www.example.com/")
        assert base.render() == "<base href=\"https://www.example.com/\" />"

    def test_base_target(self):
        base = Base(target="_blank")
        assert base.render() == "<base target=\"_blank\" />"

    def test_base_href_and_target(self):
        base = Base(target="_top", href="https://example.com/")
        assert base.render() == "<base href=\"https://example.com/\" target=\"_top\" />"

    def test_link_rel_stylesheet(self):
        link = Link(href="main.css", rel="stylesheet")
        assert link.render() == "<link href=\"main.css\" rel=\"stylesheet\" />"

    def test_link_image(self):
        link = Link(
            rel="apple-touch-icon-precomposed",
            sizes="114x114",
            href="apple-icon-114.png",
            type="image/png",
        )
        assert link.render() == '<link rel="apple-touch-icon-precomposed" sizes="114x114" href="apple-icon-114.png" type="image/png" />'

    def test_link_media(self):
        link = Link(
            href="print.css",
            rel="stylesheet",
            media="print"
        )
        assert link.render() == '<link href="print.css" rel="stylesheet" media="print" />'

    def test_meta_charset(self):
        meta = Meta(charset="utf-8")
        assert meta.render() == "<meta charset=\"utf-8\" />"

    def test_meta_http_equiv_and_content(self):
        meta = Meta(
            http_equiv="refresh",
            content="3;url=https://www.mozilla.org"
        )
        assert meta.render() == "<meta http-equiv=\"refresh\" content=\"3;url=https://www.mozilla.org\" />"

    def test_style(self):
        style = Style(
            "p {color: white; background-color: blue; padding: 5px; border: 1px solid black;}")
        assert style.render(
        ) == "<style>p {color: white; background-color: blue; padding: 5px; border: 1px solid black;}</style>"

    def test_style_with_media(self):
        style = Style(
            "p {color: blue; background-color: yellow;}",
            media="all and (max-width: 500px)"
        )
        assert style.render(
        ) == '<style media="all and (max-width: 500px)">p {color: blue; background-color: yellow;}</style>'

    def test_title(self):
        title = Title("Grandma's Heavy Metal Festival Journal")
        assert title.render() == "<title>Grandma's Heavy Metal Festival Journal</title>"
