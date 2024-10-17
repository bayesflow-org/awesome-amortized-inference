# Contributing to the Awesome Amortized Inference Resources

Thank you for your interest in contributing to the Awesome Amortized Inference repository! This is a community-driven project, and contributions are always welcome. You can add new resources by simply adding a BibTeX entry to the `resources.bib` file.
Information on how to contribute to the backend code can be found at the bottom of this file.

## How to Contribute

To contribute a new resource, follow these steps:

1. **Clone the Repository**: Fork this repository and clone it to your local machine.

2. **Edit the `resources.bib` File**: Add your resource to the `resources.bib` file.

   - Make sure to follow the guidelines below when creating a new BibTeX entry.

3. **Create a Pull Request**: Once you have added your BibTeX entry, create a pull request so that your contribution can be reviewed and added to the project.

## Guidelines for BibTeX Entries

- **Mandatory Fields**: Every BibTeX entry must include:

  - `title`: The title of the resource.
  - `author`: The list of authors. Use the standard BibTeX format (e.g., `author = {Doe, John and Smith, Jane}`).

- **Awesome Fields**: You can add important meta-information for the resource list in the `awesome-` fields:
  - `awesome-category`: The category of the paper, choose from `software, method, application, overview`.
  - `awesome-tldr`: A short one-sentence summary of the paper (TL;DR = too long, didn't read). Please try to make the TLDR say more than the title. We know it's hard but it's well worth the effort because it helps others get the gist of a resource.
  - These fields will **not** be included in the BibTeX export.

- **Awesome Links**: You can add any additional links using fields of the form `awesome-link-<key> = {<value>}`. These fields will create links in the `README.md`:

  - For example: `awesome-link-paper = {https://arxiv.org/abs/2302.09125}` will render as `[Paper](https://arxiv.org/abs/2302.09125)`.
  - These fields will **not** be included in the BibTeX export.

- **Other Fields**: All other fields, such as `journal`, `year`, etc., will be included in the BibTeX export and are optional.

### Example BibTeX Entry

```bibtex
@article{example2023,
  title = {An Example Resource},
  author = {Doe, John and Smith, Jane},
  journal = {Journal of Example Studies},
  year = {2023},
  awesome-category = {method},
  awesome-tldr = {Creating examples for resources significantly increases the quality of contributions.},
  awesome-link-paper = {https://arxiv.org/abs/2302.09125},
  awesome-link-code = {https://github.com/example/software}
}
```

In the above example:

- The `title`, `author`, `journal`, and `year` fields are standard BibTeX fields.
- The resource will be categorized in the "Methodological Papers" section and have the TLDR _Creating examples for resources significantly increases the quality of contributions._
- The `awesome-link-paper` and `awesome-link-software` fields will generate links labeled `[Paper]` and `[Code]`, respectively, in the `README.md`.

## Important Note

The `README.md` file is automatically generated from the `resources.bib` file by a GitHub Action workflow. **Do not edit the `README.md` file directly**, as your changes will be overwritten. Instead, make all changes by editing the `data.bib` file.

## Submitting Your Contribution

Once you have added your BibTeX entry to `resources.bib`, follow these steps to submit your contribution:

1. **Commit Your Changes**: Commit your changes with a clear commit message.

2. **Push to Your Fork**: Push the changes to your fork of the repository.

3. **Create a Pull Request**: Go to the original repository on GitHub and create a pull request. Please provide a brief description of the resource you are adding.

## Questions or Issues?

If you have any questions or run into any issues, feel free to open an issue in the repository. We're here to help!

Thank you for contributing and helping make this resource more useful for everyone!

# Contributing to the Backend Code

If you are interested in contributing to the backend code that generates the `README.md` file, you can find the code in the `.github/workflows/` directory.
The generation of the `README.md` file is handled by a GitHub Action workflow, which in turn calls the Python backend.
Please lint your code with `ruff` before submitting a pull request that involves Python code.
