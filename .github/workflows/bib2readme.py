from collections import defaultdict
from typing import Dict, List

from pybtex.database import parse_file
from pybtex.scanner import PybtexSyntaxError
from pylatexenc.latex2text import LatexNodes2Text

from slugify import slugify

# Define the categories to be printed in the README
VALID_CATEGORIES = {
    "overview": "Overview Articles",
    "software": "Software",
    "method": "Methodological Papers",
    "application": "Application Papers",
    "uncategorized": "Uncategorized",
}

README_HEADERS = """
# Awesome Amortized Inference

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)
![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey)

Welcome to the Awesome Amortized Inference repository!
This is a curated list of resources, including overviews, software, papers, and other resources related to amortized inference.
Feel free to explore the entries below and use the provided BibTeX information for citation purposes.
This is a community-driven project which is currently maintained by [Marvin Schmitt](https://www.marvinschmitt.com).
Contributions are always welcome, see [`CONTRIBUTING.md`](https://github.com/bayesflow-org/awesome-amortized-inference/blob/main/CONTRIBUTING.md) for a contribution guide.

This awesome list currently has some overlap with the `awesome-neural-sbi` list ([Link](https://github.com/smsharma/awesome-neural-sbi)) because
amortized inference has gained populatity in the context of simulation-based inference (SBI) with neural networks.
However, there is a trend towards broader amortized inference methods that are not necessarily simulation-based.
This list aims to cover all amortized inference methods, including but not limited to simulation-based inference.
We highly recommend checking out the `awesome-neural-sbi` list for more resources on modern simulation-based inference with neural networks.


> 🚧 **Under construction** 🚧
> This repository is a development version under construction. The list of resources is just a small set for debugging and development purposes.
> For now, we focus on developing features that we think could be useful for the community (e.g., `BibTeX`-first structure).
> Then, we will evaluate whether this project has the potential to be useful for the community in addition to existing lists
> that are specifically designated to *simulation-based inference* and not *amortized inference* (which doesn't need to be simulation-based).
> Once we figure out the direction and deem the project potentially useful for the community, we'll launch and add an extensive set of resources 
> -- hopefully with the help of many awesome people from the community 🧡
"""


# Define Entry class
class Entry:
    def __init__(
        self,
        title: str,
        authors: str,
        year: str,
        url: str,
        awesome_category: str,
        awesome_link_fields: Dict[str, str],
        bibtex: str,
        awesome_tldr: str = "",
    ):
        self.title = title
        self.authors = authors
        self.year = year
        self.url = url
        self.awesome_category = awesome_category
        self.awesome_link_fields = awesome_link_fields
        self.bibtex = bibtex
        self.awesome_tldr = awesome_tldr

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
        year = entry.fields.get("year", "")
        awesome_category = entry.fields.get("awesome-category", "uncategorized").lower()

        # get all fields that start with 'awesome-link-' and save them in a separate field
        awesome_link_fields = {
            key[len("awesome-link-") :]: value
            for key, value in entry.fields.items()
            if key.startswith("awesome-link-")
        }

        # get the TL;DR field
        awesome_tldr = entry.fields.get("awesome-tldr", "")

        if awesome_category not in VALID_CATEGORIES:
            print(
                f"Warning: Unrecognized category '{awesome_category}' for entry '{title}'. Categorizing as 'uncategorized'."
            )
            awesome_category = "uncategorized"
        bibtex = cls.format_bibtex(entry)
        return cls(
            title,
            authors,
            year,
            url,
            awesome_category,
            awesome_link_fields,
            bibtex,
            awesome_tldr,
        )

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
            if not key.startswith("awesome-")  # exclude all awesome fields from BibTeX
        ]
        if "author" in entry.persons:
            bibtex_fields.append(
                f"author = {{{' and '.join(str(person) for person in entry.persons.get('author', []))}}}"
            )
        bibtex_str = (
            f"@{bibtex_type}{{{bibtex_key},\n  " + ",\n  ".join(bibtex_fields) + "\n  }"
        )
        return bibtex_str

    def to_string(self) -> str:
        entry_str = f"- **{self.title}**"

        if self.awesome_category == "software":
            if self.awesome_tldr:
                entry_str += f"<br />_TLDR: {self.awesome_tldr}_"

        elif self.awesome_category != "software":
            if self.year:
                entry_str += f" ({self.year})"

            if self.awesome_tldr:
                entry_str += f"<br />_TLDR: {self.awesome_tldr}_"
            # for papers: ask for a contribution if no TLDR is available yet
            elif self.awesome_category in ["overview", "method", "application"]:
                entry_str += "<br />_Reading this paper? Please consider contributing a TLDR summary._"

            if self.authors:
                entry_str += f"<br />by {self.authors}"

        if self.awesome_link_fields:
            entry_str += "<br />"
            for key, value in self.awesome_link_fields.items():
                entry_str += f"[[{key.capitalize()}]]({value}) "
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
        entries_by_category[entry_obj.awesome_category].append(entry_obj)
    return entries_by_category


def create_readme(entries_by_category: Dict[str, List[Entry]]) -> str:
    readme_content = README_HEADERS

    # Add Table of Contents
    readme_content += "\n\n"
    readme_content += "## Contents\n\n"
    for category_key, category_value in VALID_CATEGORIES.items():
        if category_key in entries_by_category:
            readme_content += f"- [{category_value}](#{slugify(category_value)})\n"
    readme_content += "\n\n"

    # Add Sections
    for category_key, category_value in VALID_CATEGORIES.items():
        if category_key in entries_by_category:
            if category_key in ["overview", "method", "application", "uncategorized"]:
                entries_by_category[category_key].sort(
                    key=lambda x: x.year if x.year.isdigit() else "0000", reverse=True
                )
            readme_content += f"## {category_value}\n\n"
            readme_content += "\n".join(
                [entry.to_string() for entry in entries_by_category[category_key]]
            )
    return readme_content


def main():
    try:
        bib_database = parse_file("resources.bib")
    except FileNotFoundError:
        print("The resources.bib file was not found.")
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
