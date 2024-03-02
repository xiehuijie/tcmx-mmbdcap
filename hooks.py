from typing import Literal, Union, cast, Iterable
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.nav import Navigation, Section
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page


def on_nav(nav: Navigation, config: MkDocsConfig, files: Files):
    def rename_nav(item: list[Union[Section, Page]]):
        def rename_section(item: Section):
            for child in item.children:
                if isinstance(child, Section):
                    rename_section(child)
                    break
                if isinstance(child, Page) and child.file.src_path.endswith("index.md"):
                    child.read_source(config)
                    print(child, child.meta)
                    item.title = child.title if isinstance(child.title, str) else item.title
                    break
        for child in item:
            if isinstance(child, Section):
                rename_section(child)

    def sort_nav(item: list[Union[Section, Page]]):
        def get_order(item: Union[Section, Page]):
            order = 0
            if isinstance(item, Page):
                if item == nav.homepage:
                    return float("inf")
                item.read_source(config)
                order = item.meta.get("order", 0)
            elif isinstance(item, Section):
                for child in item.children:
                    if isinstance(child, Page) and child.file.src_path.endswith("index.md"):
                        child.read_source(config)
                        order = child.meta.get("order", 0)
            return order if isinstance(order, int) else 0
        item.sort(key=get_order, reverse=True)
        for child in item:
            if isinstance(child, Section):
                sort_nav(cast(list[Union[Section, Page]], child.children))

    def transform_i18n():
        def find_i18n_section():
            for item in nav.items:
                if isinstance(item, Section) and item.title == 'I18n':
                    return item
        i18n = find_i18n_section()
        if i18n is None:
            return
        nav.items.remove(i18n)

    sort_nav(nav.items)
    rename_nav(nav.items)
    transform_i18n()

    return nav
