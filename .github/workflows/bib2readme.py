from collections import defaultdict
from typing import Dict, List

import bibtexparser

# Define the categories to be printed in the README
VALID_CATEGORIES = ["overview", "software", "paper", "uncategorized"]

README_HEADER = """
Welcome to the Awesome Amortized Inference repository!
This is a curated list of resources, including overviews, software, papers, and other resources related to amortized inference.
Feel free to explore the entries below and use the provided BibTeX information for citation purposes.
Contributioons always welcome, this shall be a community-driven project.
Contribution guide will follow ASAP.
"""


# Define Entry class
class Entry:
    def __init__(self, title: str, authors: str, url: str, category: str, bibtex: str):
        self.title = title
        self.authors = authors
        self.url = url
        self.category = category
        self.bibtex = bibtex

    @classmethod
    def from_bibtex(cls, entry: dict) -> "Entry":
        title = entry.get("title", "No title").replace("{", "").replace("}", "")
        authors = entry.get("author", "No author").replace(" and ", ", ")
        url = entry.get("url", "")
        category = entry.get("category", "uncategorized").lower()
        bibtex = cls.format_bibtex(entry)
        return cls(title, authors, url, category, bibtex)

    @staticmethod
    def format_bibtex(entry: dict) -> str:
        bibtex_type = entry.get("ENTRYTYPE", "misc")
        bibtex_key = entry.get("ID", "unknown")
        bibtex_fields = [
            f"  {key} = {{{value}}}"
            for key, value in entry.items()
            if key not in ["ENTRYTYPE", "ID"]
        ]
        bibtex_str = (
            f"@{bibtex_type}{{{bibtex_key},\n  " + ",\n  ".join(bibtex_fields) + "\n}"
        )
        return bibtex_str

    def to_string(self) -> str:
        entry_str = f"- **{self.title}**\n  {self.authors}\n"
        if self.url:
            entry_str += f"  [Link]({self.url})\n"
        entry_str += (
            f"<details>\n"
            f"<summary>Show BibTeX</summary>\n"
            f"<pre>```\n"
            f"{self.bibtex}\n"
            f"```</pre>\n"
            f"</details>\n"
        )
        entry_str += "\n"
        return entry_str


def organize_entries(bib_database) -> Dict[str, List[Entry]]:
    entries_by_category: Dict[str, List[Entry]] = defaultdict(list)
    for entry in bib_database.entries:
        entry_obj = Entry.from_bibtex(entry)
        entries_by_category[entry_obj.category].append(entry_obj)
    return entries_by_category


def create_readme(entries_by_category: Dict[str, List[Entry]]) -> str:
    readme_content = "# Awesome Amortized Inference\n\n"
    readme_content += README_HEADER

    for category in VALID_CATEGORIES:
        if category in entries_by_category:
            readme_content += f"## {category.capitalize()}\n\n"
            readme_content += "\n".join(
                [entry.to_string() for entry in entries_by_category[category]]
            )
            readme_content += "\n"
    return readme_content


def main():
    try:
        with open("data.bib") as bibtex_file:
            bib_database = bibtexparser.load(bibtex_file)
    except FileNotFoundError:
        print("The data.bib file was not found.")
        exit(1)

    entries_by_category = organize_entries(bib_database)
    readme_content = create_readme(entries_by_category)

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)


if __name__ == "__main__":
    main()
