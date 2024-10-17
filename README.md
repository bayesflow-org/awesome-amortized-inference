
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


## Contents

- [Overview Articles](#overview-articles)
- [Software](#software)
- [Methodological Papers](#methodological-papers)
- [Application Papers](#application-papers)
- [Uncategorized](#uncategorized)


## Overview Articles

- **Neural Methods for Amortized Inference** (2024)<br />_TLDR: Overview paper of amortized point estimators and full posterior estimators._<br />by Andrew Zammit-Mangion, Matthew Sainsbury-Dale, Raphaël Huser<br />[[Paper]](https://arxiv.org/abs/2404.12484) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @misc{zammit-mangion2024neural,
  title = {Neural Methods for Amortized Inference},
  publisher = {arXiv},
  year = {2024},
  author = {Zammit-Mangion, Andrew and Sainsbury-Dale, Matthew and Huser, Raphaël}
  }
  </code>
  </pre></details>

- **Normalizing flows for probabilistic modeling and inference** (2021)<br />_TLDR: Reading this paper? Please consider contributing a TLDR summary._<br />by George Papamakarios, Eric Nalisnick, Danilo Jimenez Rezende, Shakir Mohamed, Balaji Lakshminarayanan<br />[[Paper]](https://arxiv.org/abs/1912.02762) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{papamakarios2021normalizing,
  title = {Normalizing flows for probabilistic modeling and inference},
  year = {2021},
  publisher = {JMLR.org},
  volume = {22},
  number = {1},
  issn = {1532-4435},
  journal = {J. Mach. Learn. Res.},
  month = {jan},
  articleno = {57},
  numpages = {64},
  author = {Papamakarios, George and Nalisnick, Eric and Rezende, Danilo Jimenez and Mohamed, Shakir and Lakshminarayanan, Balaji}
  }
  </code>
  </pre></details>

- **The frontier of simulation-based inference** (2020)<br />_TLDR: Reading this paper? Please consider contributing a TLDR summary._<br />by Kyle Cranmer, Johann Brehmer, Gilles Louppe<br />[[Paper]](http://dx.doi.org/10.1073/pnas.1912789117) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{Cranmer2020,
  title = {The frontier of simulation-based inference},
  volume = {117},
  ISSN = {1091-6490},
  DOI = {10.1073/pnas.1912789117},
  number = {48},
  journal = {Proceedings of the National Academy of Sciences},
  publisher = {Proceedings of the National Academy of Sciences},
  year = {2020},
  pages = {30055-30062},
  author = {Cranmer, Kyle and Brehmer, Johann and Louppe, Gilles}
  }
  </code>
  </pre></details>
## Software

- **BayesFlow: Amortized Bayesian Workflows With Neural Networks**<br />_TLDR: Reading this paper? Please consider contributing a TLDR summary._<br />[[Code]](https://bayesflow.org/) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{radev2023bayesflow,
  doi = {10.21105/joss.05702},
  year = {2023},
  publisher = {The Open Journal},
  volume = {8},
  number = {89},
  pages = {5702},
  title = {BayesFlow: Amortized Bayesian Workflows With Neural Networks},
  journal = {Journal of Open Source Software},
  author = {Radev, Stefan T. and Schmitt, Marvin and Schumacher, Lukas and Elsemüller, Lasse and Pratz, Valentin and Schälte, Yannik and Köthe, Ullrich and Bürkner, Paul-Christian}
  }
  </code>
  </pre></details>

- **sbi: A toolkit for simulation-based inference**<br />_TLDR: Reading this paper? Please consider contributing a TLDR summary._<br />[[Code]](https://sbi-dev.github.io/sbi/latest/) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{tejero-cantero2020sbi,
  doi = {10.21105/joss.02505},
  year = {2020},
  publisher = {The Open Journal},
  volume = {5},
  number = {52},
  pages = {2505},
  title = {sbi: A toolkit for simulation-based inference},
  journal = {Journal of Open Source Software},
  author = {Tejero-Cantero, Alvaro and Boelts, Jan and Deistler, Michael and Lueckmann, Jan-Matthis and Durkan, Conor and Gonçalves, Pedro J. and Greenberg, David S. and Macke, Jakob H.}
  }
  </code>
  </pre></details>
## Methodological Papers

- **ASPIRE: Iterative Amortized Posterior Inference for Bayesian Inverse Problems** (2024)<br />_TLDR: Reading this paper? Please consider contributing a TLDR summary._<br />by Rafael Orozco, Ali Siahkoohi, Mathias Louboutin, Felix J. Herrmann
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @misc{orozco2024aspire,
  Title = {ASPIRE: Iterative Amortized Posterior Inference for Bayesian Inverse Problems},
  Year = {2024},
  Eprint = {arXiv:2405.05398},
  author = {Orozco, Rafael and Siahkoohi, Ali and Louboutin, Mathias and Herrmann, Felix J.}
  }
  </code>
  </pre></details>

- **Sensitivity-Aware Amortized Bayesian Inference** (2024)<br />_TLDR: Efficient amortized sensitivity analyses with context variables_<br />by Lasse Elsemüller, Hans Olischläger, Marvin Schmitt, Paul-Christian Bürkner, Ullrich Koethe, Stefan T. Radev<br />[[Code]](https://github.com/bayesflow-org/SA-ABI) [[Paper]](https://openreview.net/forum?id=Kxtpa9rvM0) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{elsemueller2024sensitivity,
  title = {Sensitivity-Aware Amortized Bayesian Inference},
  journal = {Transactions on Machine Learning Research},
  issn = {2835-8856},
  year = {2024},
  author = {Elsem{\"u}ller, Lasse and Olischl{\"a}ger, Hans and Schmitt, Marvin and B{\"u}rkner, Paul-Christian and Koethe, Ullrich and Radev, Stefan T.}
  }
  </code>
  </pre></details>

- **Neural Importance Sampling for Rapid and Reliable Gravitational-Wave Inference** (2023)<br />_TLDR: Reading this paper? Please consider contributing a TLDR summary._<br />by Maximilian Dax, Stephen R. Green, Jonathan Gair, Michael Pürrer, Jonas Wildberger, Jakob H. Macke, Alessandra Buonanno, Bernhard Schölkopf<br />[[Paper]](http://dx.doi.org/10.1103/PhysRevLett.130.171403) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{dax2023neural,
  title = {Neural Importance Sampling for Rapid and Reliable Gravitational-Wave Inference},
  volume = {130},
  ISSN = {1079-7114},
  DOI = {10.1103/physrevlett.130.171403},
  number = {17},
  journal = {Physical Review Letters},
  publisher = {American Physical Society (APS)},
  year = {2023},
  author = {Dax, Maximilian and Green, Stephen R. and Gair, Jonathan and P\"{u}rrer, Michael and Wildberger, Jonas and Macke, Jakob H. and Buonanno, Alessandra and Sch\"{o}lkopf, Bernhard}
  }
  </code>
  </pre></details>

- **JANA: Jointly Amortized Neural Approximation of Complex Bayesian Models** (2023)<br />_TLDR: Reading this paper? Please consider contributing a TLDR summary._<br />by Stefan T. Radev, Marvin Schmitt, Valentin Pratz, Umberto Picchini, Ullrich Köthe, Paul-Christian Bürkner<br />[[Paper]](https://proceedings.mlr.press/v216/radev23a) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{radev2023jana,
  title = {{JANA: Jointly Amortized Neural Approximation of Complex Bayesian Models}},
  booktitle = {Proceedings of the 39th Conference on Uncertainty in Artificial Intelligence},
  pages = {1695--1706},
  year = {2023},
  volume = {216},
  series = {Proceedings of Machine Learning Research},
  publisher = {PMLR},
  author = {Radev, Stefan T. and Schmitt, Marvin and Pratz, Valentin and Picchini, Umberto and K\"othe, Ullrich and B\"urkner, Paul-Christian}
  }
  </code>
  </pre></details>
## Application Papers

- **Evaluating Sparse Galaxy Simulations via Out-of-Distribution Detection and Amortized Bayesian Model Comparison** (2024)<br />_TLDR: Reading this paper? Please consider contributing a TLDR summary._<br />by Lingyi Zhou, Stefan T. Radev, William H. Oliver, Aura Obreja, Zehao Jin, Tobias Buck<br />[[Paper]](https://arxiv.org/abs/2410.10606) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{zhou2024EvaluatingSparseGalaxy,
  title = {Evaluating {{Sparse Galaxy Simulations}} via {{Out-of-Distribution Detection}} and {{Amortized Bayesian Model Comparison}}},
  booktitle = {38th {{Conference}} on {{Neural Information Processing Systems}}},
  year = {2024},
  author = {Zhou, Lingyi and Radev, Stefan T. and Oliver, William H. and Obreja, Aura and Jin, Zehao and Buck, Tobias}
  }
  </code>
  </pre></details>
## Uncategorized

- **Flow Matching for Scalable Simulation-Based Inference** (2023)<br />_TLDR: Reading this paper? Please consider contributing a TLDR summary._<br />by Jonas Bernhard Wildberger, Maximilian Dax, Simon Buchholz, Stephen R Green, Jakob H. Macke, Bernhard Schölkopf<br />[[Paper]](https://openreview.net/forum?id=D2cS6SoYlP) [[Code]](https://github.com/dingo-gw/flow-matching-posterior-estimation) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{wildberger2023flow,
  title = {Flow Matching for Scalable Simulation-Based Inference},
  booktitle = {Thirty-seventh Conference on Neural Information Processing Systems},
  year = {2023},
  url = {https://openreview.net/forum?id=D2cS6SoYlP},
  author = {Wildberger, Jonas Bernhard and Dax, Maximilian and Buchholz, Simon and Green, Stephen R and Macke, Jakob H. and Sch{\"o}lkopf, Bernhard}
  }
  </code>
  </pre></details>
