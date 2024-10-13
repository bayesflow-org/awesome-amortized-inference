from collections import defaultdict
from typing import Dict, List

from pybtex.database import parse_file
from pybtex.scanner import PybtexSyntaxError
from pylatexenc.latex2text import LatexNodes2Text

# Define the categories to be printed in the README
VALID_CATEGORIES = ["overview", "software", "paper", "uncategorized"]

README_BADGES = """
![Awesome](https://img.shields.io/badge/Awesome-List-blue)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)
![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey)
"""

README_INTRO = """
Welcome to the Awesome Amortized Inference repository!
This is a curated list of resources, including overviews, software, papers, and other resources related to amortized inference.
Feel free to explore the entries below and use the provided BibTeX information for citation purposes.
Contributions are always welcome, this is a community-driven project.
"""


# Define Entry class
class Entry:
    def __init__(
        self,
        title: str,
        authors: str,
        url: str,
        category: str,
        awesome_fields: Dict[str, str],
        bibtex: str,
    ):
        self.title = title
        self.authors = authors
        self.url = url
        self.category = category
        self.awesome_fields = awesome_fields
        self.bibtex = bibtex

    @classmethod
    def from_bibtex(cls, entry) -> "Entry":
        title = entry.fields.get("title", "No title").replace("{", "").replace("}", "")
        authors = (
            ", ".join(
                cls.person_to_first_last(person)
                for person in entry.persons.get("author", [])
            )
            or "No author"
        )
        url = entry.fields.get("url", "")
        category = entry.fields.get("category", "uncategorized").lower()

        # get all fields that start with 'awesome-' and save them in a separate field
        awesome_fields = {
            key[len("awesome-") :]: value
            for key, value in entry.fields.items()
            if key.startswith("awesome-")
        }

        if category not in VALID_CATEGORIES:
            print(
                f"Warning: Unrecognized category '{category}' for entry '{title}'. Categorizing as 'uncategorized'."
            )
            category = "uncategorized"
        bibtex = cls.format_bibtex(entry)
        return cls(title, authors, url, category, awesome_fields, bibtex)

    @staticmethod
    def person_to_first_last(person) -> str:
        name_parts = [
            " ".join(part)
            for part in [
                person.first_names,
                person.middle_names,
                person.prelast_names,
                person.last_names,
                person.lineage_names,
            ]
            if part
        ]
        name = " ".join(name_parts)

        return LatexNodes2Text().latex_to_text(name)

    @staticmethod
    def format_bibtex(entry) -> str:
        bibtex_type = entry.type if entry.type else "misc"
        bibtex_key = entry.key if entry.key else "unknown"
        bibtex_fields = [
            f"{key} = {{{value}}}"
            for key, value in entry.fields.items()
            if not key.startswith("awesome-")  # exclude awesome fields from BibTeX
        ]
        if "author" in entry.persons:
            bibtex_fields.append(
                f"author = {{{' and '.join(str(person) for person in entry.persons.get('author', []))}}}"
            )
        bibtex_str = (
            f"@{bibtex_type}{{{bibtex_key},\n&nbsp;&nbsp;"
            + ",\n&nbsp;&nbsp;".join(bibtex_fields)
            + "\n  }"
        )
        return bibtex_str

    def to_string(self) -> str:
        entry_str = f"- **{self.title}**."
        if self.awesome_fields:
            entry_str += " "
            for key, value in self.awesome_fields.items():
                entry_str += f"[[{key.capitalize()}]]({value}) "
        entry_str += f"<br />  {self.authors}<br />"
        entry_str += f"""
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  {self.bibtex}
  </code>
  </pre></details>
"""
        return entry_str


def organize_entries(bib_database) -> Dict[str, List[Entry]]:
    entries_by_category: Dict[str, List[Entry]] = defaultdict(list)
    for entry_key, entry in bib_database.entries.items():
        entry_obj = Entry.from_bibtex(entry)
        entries_by_category[entry_obj.category].append(entry_obj)
    return entries_by_category


def create_readme(entries_by_category: Dict[str, List[Entry]]) -> str:
    readme_content = "# Awesome Amortized Inference\n\n"
    readme_content += README_BADGES + "\n\n"
    readme_content += README_INTRO

    for category in VALID_CATEGORIES:
        if category in entries_by_category:
            readme_content += f"## {category.capitalize()}\n\n"
            readme_content += "\n".join(
                [entry.to_string() for entry in entries_by_category[category]]
            )
    return readme_content


def main():
    try:
        bib_database = parse_file("data.bib")
    except FileNotFoundError:
        print("The data.bib file was not found.")
        exit(1)
    except PybtexSyntaxError as e:
        print(f"Error parsing BibTeX file: {e}")
        exit(1)

    entries_by_category = organize_entries(bib_database)
    readme_content = create_readme(entries_by_category)

    with open("README.md", "w") as readme_file:
        readme_file.write(readme_content)


if __name__ == "__main__":
    main()
