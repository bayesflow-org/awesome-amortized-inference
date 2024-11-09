
# Awesome Amortized Inference

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)
![License: CC0](https://img.shields.io/badge/License-CC0_1.0-lightgrey)

Welcome to the Awesome Amortized Inference repository!
This is a curated list of resources, including reviews, software, papers, and other resources related to amortized inference.
Feel free to explore the entries below and use the provided BibTeX information for citation purposes.
This is a community-driven project which is currently maintained by [Marvin Schmitt](https://www.marvinschmitt.com).
Contributions are always welcome, see [`CONTRIBUTING.md`](https://github.com/bayesflow-org/awesome-amortized-inference/blob/main/CONTRIBUTING.md) for a contribution guide 🧡

This list currently has some overlap with the `awesome-neural-sbi` list ([Link](https://github.com/smsharma/awesome-neural-sbi)) because
amortized inference has gained popularity in the context of simulation-based inference (SBI) with neural networks.
However, there is a trend towards broader amortized inference methods that are not necessarily simulation-based.
This list aims to cover all amortized inference methods, including but not limited to simulation-based inference.
We highly recommend checking out these lists for more resources on modern simulation-based inference:

- [awesome-neural-sbi](https://github.com/smsharma/awesome-neural-sbi)
- [simulation-based inference website](https://simulation-based-inference.org/)
- [Introduction to simulation-based inference by TransferLab](https://transferlab.ai/trainings/simulation-based-inference/)



## Contents

- [Review Articles](#review-articles)
- [Software](#software)
- [Methodological Papers](#methodological-papers)
- [Application Papers](#application-papers)


## Review Articles

- **Neural Methods for Amortised Parameter Inference** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Andrew Zammit-Mangion, Matthew Sainsbury-Dale, Raphaël Huser<br />[[Paper]](https://arxiv.org/abs/2404.12484) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @misc{zammit2024neural,
  title = {Neural Methods for Amortised Parameter Inference},
  year = {2024},
  number = {arXiv:2404.12484},
  eprint = {2404.12484},
  primaryclass = {cs},
  publisher = {arXiv},
  archiveprefix = {arXiv},
  author = {Zammit-Mangion and Sainsbury-Dale and Huser}
  }
  </code>
  </pre></details>

- **Simulation Intelligence: Towards a New Generation of Scientific Methods** (2022)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Alexander Lavin, David Krakauer, Hector Zenil, Justin Gottschlich, Tim Mattson, Johann Brehmer, Anima Anandkumar, Sanjay Choudry, Kamil Rocki, Atılım Güneş Baydin, Carina Prunkl, Brooks Paige, Olexandr Isayev, Erik Peterson, Peter L. McMahon, Jakob Macke, Kyle Cranmer, Jiaxin Zhang, Haruko Wainwright, Adi Hanuka, Manuela Veloso, Samuel Assefa, Stephan Zheng, Avi Pfeffer<br />[[Paper]](https://arxiv.org/abs/2112.03235) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @misc{lavin2022simulation,
  title = {Simulation {{Intelligence}}: {{Towards}} a {{New Generation}} of {{Scientific Methods}}},
  shorttitle = {Simulation {{Intelligence}}},
  year = {2022},
  number = {arXiv:2112.03235},
  eprint = {2112.03235},
  primaryclass = {cs},
  publisher = {arXiv},
  archiveprefix = {arXiv},
  author = {Lavin and Krakauer and Zenil and Gottschlich and Mattson and Brehmer and Anandkumar and Choudry and Rocki and Baydin and Prunkl and Paige and Isayev and Peterson and McMahon and Macke and Cranmer and Zhang and Wainwright and Hanuka and Veloso and Assefa and Zheng and Pfeffer}
  }
  </code>
  </pre></details>

- **Normalizing Flows for Probabilistic Modeling and Inference** (2021)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by George Papamakarios, Eric Nalisnick, Danilo Jimenez Rezende, Shakir Mohamed, Balaji Lakshminarayanan<br />[[Paper]](https://www.jmlr.org/papers/v22/19-1028.html) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{papamakarios2021normalizing,
  title = {Normalizing Flows for Probabilistic Modeling and Inference},
  year = {2021},
  journal = {Journal of Machine Learning Research},
  volume = {22},
  number = {57},
  pages = {1--64},
  author = {Papamakarios and Nalisnick and Rezende and Mohamed and Lakshminarayanan}
  }
  </code>
  </pre></details>

- **The Frontier of Simulation-Based Inference** (2020)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Kyle Cranmer, Johann Brehmer, Gilles Louppe<br />[[Paper]](https://www.pnas.org/doi/abs/10.1073/pnas.1912789117) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{cranmer2020frontier,
  title = {The Frontier of Simulation-Based Inference},
  year = {2020},
  journal = {Proceedings of the National Academy of Sciences},
  volume = {117},
  number = {48},
  pages = {30055--30062},
  issn = {0027-8424, 1091-6490},
  doi = {10.1073/pnas.1912789117},
  langid = {english},
  author = {Cranmer and Brehmer and Louppe}
  }
  </code>
  </pre></details>
## Software

- **BayesFlow: Amortized Bayesian Workflows with Neural Networks**<br />[[Paper]](https://joss.theoj.org/papers/10.21105/joss.05702) [[Code]](https://github.com/bayesflow-org/bayesflow) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{radev2023bayesflow,
  title = {{{BayesFlow}}: {{Amortized Bayesian}} Workflows with Neural Networks},
  year = {2023},
  journal = {Journal of Open Source Software},
  volume = {8},
  number = {89},
  pages = {5702},
  publisher = {The Open Journal},
  doi = {10.21105/joss.05702},
  author = {Radev and Schmitt and Schumacher and Elsemüller and Pratz and Schälte and Köthe and Bürkner}
  }
  </code>
  </pre></details>

- **sbi: A Toolkit for Simulation-Based Inference**<br />[[Paper]](https://joss.theoj.org/papers/10.21105/joss.02505) [[Code]](https://github.com/sbi-dev/sbi) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{tejero-cantero2020sbi,
  title = {{sbi}: {{A}} Toolkit for Simulation-Based Inference},
  year = {2020},
  journal = {Journal of Open Source Software},
  volume = {5},
  number = {52},
  pages = {2505},
  publisher = {The Open Journal},
  doi = {10.21105/joss.02505},
  author = {Tejero-Cantero and Boelts and Deistler and Lueckmann and Durkan and Gonçalves and Greenberg and Macke}
  }
  </code>
  </pre></details>
## Methodological Papers

- **An amortized approach to non-linear mixed-effects modeling based on neural posterior estimation** (2024)<br />_TLDR: Neural posterior estimation for hierarchical models, where the NPE is used in a first stage on a local level and then repeatedly used for global inference leveraging amortization._<br />by Jonas Arruda, Yannik Schälte, Clemens Peiter, Olga Teplytska, Ulrich Jaehde, Jan Hasenauer<br />┃🏷️ parameter estimation┃ ┃🏷️ hierarchical models┃<br />[[Paper]](https://openreview.net/forum?id=uCdcXRuHnC) [[Code]](https://github.com/arrjon/Amortized-NLME-Models/tree/ICML2024) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{arruda2024anamortized,
  title = {An amortized approach to non-linear mixed-effects modeling based on neural posterior estimation},
  booktitle = {Forty-first International Conference on Machine Learning},
  year = {2024},
  author = {Arruda and Schälte and Peiter and Teplytska and Jaehde and Hasenauer}
  }
  </code>
  </pre></details>

- **A Practical Guide to Sample-Based Statistical Distances for Evaluating Generative Models in Science** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Sebastian Bischoff, Alana Darcher, Michael Deistler, Richard Gao, Franziska Gerken, Manuel Gloeckler, Lisa Haxel, Jaivardhan Kapoor, Janne K Lappalainen, Jakob H. Macke, Guy Moss, Matthijs Pals, Felix C Pei, Rachel Rapp, A Erdem Sağtekin, Cornelius Schröder, Auguste Schulz, Zinovia Stefanidi, Shoji Toyota, Linda Ulmer, Julius Vetter<br />┃🏷️ diagnostics┃ ┃🏷️ model evaluation┃<br />[[Paper]](https://openreview.net/forum?id=isEFziui9p) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{bischoff2024practical,
  title = {A Practical Guide to Sample-Based Statistical Distances for Evaluating Generative Models in Science},
  year = {2024},
  journal = {Transactions on Machine Learning Research},
  issn = {2835-8856},
  author = {Bischoff and Darcher and Deistler and Gao and Gerken and Gloeckler and Haxel and Kapoor and Lappalainen and Macke and Moss and Pals and Pei and Rapp and Sağtekin and Schröder and Schulz and Stefanidi and Toyota and Ulmer and Vetter}
  }
  </code>
  </pre></details>

- **Amortized Probabilistic Conditioning for Optimization, Simulation and Inference** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Paul E. Chang, Nasrulloh Loka, Daolang Huang, Ulpu Remes, Samuel Kaski, Luigi Acerbi<br />┃🏷️ meta-learning┃ ┃🏷️ optimization┃ ┃🏷️ simulation-based inference┃<br />[[Paper]](https://arxiv.org/abs/2410.15320) [[Code]](https://github.com/acerbilab/amortized-conditioning-engine/) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @misc{chang2024amortized,
  title = {Amortized Probabilistic Conditioning for Optimization, Simulation and Inference},
  year = {2024},
  eprint = {2410.15320},
  url = {https://arxiv.org/abs/2410.15320},
  author = {Chang and Loka and Huang and Remes and Kaski and Acerbi}
  }
  </code>
  </pre></details>

- **A Deep Learning Method for Comparing Bayesian Hierarchical Models.** (2024)<br />_TLDR: Proposes a multilevel neural architecture for compressing hierarchical data structures in Bayesian model comparison._<br />by Lasse Elsemüller, Martin Schnuerch, Paul-Christian Bürkner, Stefan T. Radev<br />┃🏷️ hierarchical models┃ ┃🏷️ model comparison┃ ┃🏷️ simulation-based┃<br />[[Paper]](https://arxiv.org/abs/2301.11873) [[Code]](https://github.com/bayesflow-org/Hierarchical-Model-Comparison) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{elsemuller2024deep,
  title = {A Deep Learning Method for Comparing {{Bayesian}} Hierarchical Models.},
  year = {2024},
  journal = {Psychological Methods},
  issn = {1939-1463, 1082-989X},
  doi = {10.1037/met0000645},
  author = {Elsemüller and Schnuerch and Bürkner and Radev}
  }
  </code>
  </pre></details>

- **Sensitivity-Aware Amortized Bayesian Inference** (2024)<br />_TLDR: Proposes a framework for amortized and thus efficient sensitivity analyses on all major dimensions of a Bayesian model._<br />by Lasse Elsemüller, Hans Olischläger, Marvin Schmitt, Paul-Christian Bürkner, Ullrich Köthe, Stefan T. Radev<br />┃🏷️ sensitivity analysis┃ ┃🏷️ simulation-based┃ ┃🏷️ meta learning┃<br />[[Paper]](https://openreview.net/forum?id=Kxtpa9rvM0) [[Code]](https://github.com/bayesflow-org/SA-ABI) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{elsemuller2024sensitivityaware,
  title = {Sensitivity-Aware Amortized {{Bayesian}} Inference},
  year = {2024},
  journal = {Transactions on Machine Learning Research},
  issn = {2835-8856},
  author = {Elsemüller and Olischläger and Schmitt and Bürkner and Köthe and Radev}
  }
  </code>
  </pre></details>

- **Amortized Bayesian Multilevel Models** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Daniel Habermann, Marvin Schmitt, Lars Kühmichel, Andreas Bulling, Stefan T. Radev, Paul-Christian Bürkner<br />┃🏷️ parameter estimation┃ ┃🏷️ hierarchical models┃ ┃🏷️ simulation-based┃<br />[[Paper]](https://arxiv.org/abs/2408.13230) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @misc{habermann2024amortized,
  title = {Amortized {{Bayesian Multilevel Models}}},
  year = {2024},
  number = {arXiv:2408.13230},
  eprint = {2408.13230},
  publisher = {arXiv},
  archiveprefix = {arXiv},
  author = {Habermann and Schmitt and Kühmichel and Bulling and Radev and Bürkner}
  }
  </code>
  </pre></details>

- **Likelihood-Free Parameter Estimation with Neural Bayes Estimators** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Matthew Sainsbury-Dale, Andrew Zammit-Mangion, Raphaël Huser<br />┃🏷️ parameter estimation┃ ┃🏷️ point estimation┃ ┃🏷️ simulation-based┃<br />[[Paper]](https://www.tandfonline.com/doi/full/10.1080/00031305.2023.2249522) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{sainsbury-dale2024likelihoodfree,
  title = {Likelihood-{{Free Parameter Estimation}} with {{Neural Bayes Estimators}}},
  year = {2024},
  journal = {The American Statistician},
  volume = {78},
  number = {1},
  pages = {1--14},
  issn = {0003-1305, 1537-2731},
  doi = {10.1080/00031305.2023.2249522},
  langid = {english},
  author = {Sainsbury-Dale and Zammit-Mangion and Huser}
  }
  </code>
  </pre></details>

- **Amortized Bayesian Workflow (Extended Abstract)** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Marvin Schmitt, Chengkun Li, Aki Vehtari, Luigi Acerbi, Paul-Christian Bürkner, Stefan T. Radev<br />┃🏷️ likelihood-based┃ ┃🏷️ workflow┃<br />[[Paper]](https://arxiv.org/abs/2409.04332) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{schmitt2024amortized,
  title = {Amortized {{Bayesian Workflow}} ({{Extended Abstract}})},
  booktitle = {{{NeurIPS Workshop}} on {{Bayesian Decision-Making}} and {{Uncertainty}}},
  year = {2024},
  publisher = {arXiv},
  author = {Schmitt and Li and Vehtari and Acerbi and Bürkner and Radev}
  }
  </code>
  </pre></details>

- **Consistency Models for Scalable and Fast Simulation-Based Inference** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Marvin Schmitt, Valentin Pratz, Ullrich Köthe, Paul-Christian Bürkner, Stefan T. Radev<br />┃🏷️ simulation-based┃<br />[[Paper]](https://arxiv.org/abs/2312.05440) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{schmitt2024consistency,
  title = {Consistency {{Models}} for {{Scalable}} and {{Fast Simulation-Based Inference}}},
  booktitle = {Proceedings of the 38th International Conference on Neural Information Processing Systems},
  year = {2024},
  author = {Schmitt and Pratz and Köthe and Bürkner and Radev}
  }
  </code>
  </pre></details>

- **Detecting Model Misspecification in Amortized Bayesian Inference with Neural Networks** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Marvin Schmitt, Paul-Christian Bürkner, Ullrich Köthe, Stefan T. Radev<br />┃🏷️ diagnostics┃ ┃🏷️ workflow┃<br />[[Paper]](https://link.springer.com/chapter/10.1007/978-3-031-54605-1_35) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{schmitt2024detecting,
  title = {Detecting Model Misspecification in Amortized {{Bayesian}} Inference with Neural Networks},
  booktitle = {Pattern Recognition},
  year = {2024},
  pages = {541--557},
  publisher = {Springer Nature Switzerland},
  address = {Cham},
  isbn = {978-3-031-54605-1},
  author = {Schmitt and Bürkner and Köthe and Radev}
  }
  </code>
  </pre></details>

- **Leveraging Self-Consistency for Data-Efficient Amortized Bayesian Inference** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Marvin Schmitt, Desi R. Ivanova, Daniel Habermann, Ullrich Köthe, Paul-Christian Bürkner, Stefan T. Radev<br />┃🏷️ likelihood-based┃ ┃🏷️ simulation-based┃<br />[[Paper]](https://arxiv.org/abs/2310.04395) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{schmitt2024leveraging,
  title = {Leveraging Self-Consistency for Data-Efficient Amortized {{Bayesian}} Inference},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning},
  year = {2024},
  series = {Proceedings of Machine Learning Research},
  volume = {235},
  pages = {43723--43741},
  publisher = {PMLR},
  author = {Schmitt and Ivanova and Habermann and Köthe and Bürkner and Radev}
  }
  </code>
  </pre></details>

- **Sequential Neural Score Estimation: Likelihood-free Inference with Conditional Score Based Diffusion Models** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Louis Sharrock, Jack Simons, Song Liu, Mark Beaumont<br />┃🏷️ simulation-based┃<br />[[Paper]](https://arxiv.org/abs/2210.04872) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{sharrock2024sequential,
  title = {Sequential Neural Score Estimation: {{Likelihood-free}} Inference with Conditional Score Based Diffusion Models},
  booktitle = {Proceedings of the 41st International Conference on Machine Learning},
  year = {2024},
  series = {Proceedings of Machine Learning Research},
  volume = {235},
  pages = {44565--44602},
  publisher = {PMLR},
  author = {Sharrock and Simons and Liu and Beaumont}
  }
  </code>
  </pre></details>

- **Fast and Reliable Probabilistic Reflectometry Inversion with Prior-Amortized Neural Posterior Estimation** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Vladimir Starostin, Maximilian Dax, Alexander Gerlach, Alexander Hinderhofer, Álvaro Tejero-Cantero, Frank Schreiber<br />┃🏷️ physics┃ ┃🏷️ meta learning┃<br />[[Paper]](https://arxiv.org/abs/2407.18648) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @misc{starostin2024fast,
  title = {Fast and {{Reliable Probabilistic Reflectometry Inversion}} with {{Prior-Amortized Neural Posterior Estimation}}},
  year = {2024},
  number = {arXiv:2407.18648},
  eprint = {2407.18648},
  primaryclass = {cond-mat, physics:physics, stat},
  publisher = {arXiv},
  archiveprefix = {arXiv},
  author = {Starostin and Dax and Gerlach and Hinderhofer and Tejero-Cantero and Schreiber}
  }
  </code>
  </pre></details>

- **Missing data in amortized simulation-based neural posterior estimation** (2024)<br />_TLDR: Encoding missing data in a time series by augmenting the data vector with binary indicators for presence or absence yields the most robust performance._<br />by Zijian Wang, Jan Hasenauer, Yannik Schälte<br />┃🏷️ missing data┃ ┃🏷️ simulation-based┃ ┃🏷️ parameter estimation┃<br />[[Paper]](https://doi.org/10.1371/journal.pcbi.1012184) [[Code]](https://github.com/emune-dev/Data-missingness-paper) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{wang2024missing,
  doi = {10.1371/journal.pcbi.1012184},
  journal = {PLOS Computational Biology},
  publisher = {Public Library of Science},
  title = {Missing data in amortized simulation-based neural posterior estimation},
  year = {2024},
  month = {06},
  volume = {20},
  pages = {1-17},
  number = {6},
  author = {Wang and Hasenauer and Schälte}
  }
  </code>
  </pre></details>

- **Conditional Generative Models Are Provably Robust: Pointwise Guarantees for Bayesian Inverse Problems** (2023)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Fabian Altekrüger, Paul Hagemann, Gabriele Steidl<br />┃🏷️ diagnostics┃ ┃🏷️ theory┃<br />[[Paper]](https://arxiv.org/abs/2303.15845) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{altekruger2023conditional,
  title = {Conditional Generative Models Are Provably Robust: {{Pointwise}} Guarantees for Bayesian Inverse Problems},
  year = {2023},
  journal = {Transactions on Machine Learning Research},
  issn = {2835-8856},
  author = {Altekrüger and Hagemann and Steidl}
  }
  </code>
  </pre></details>

- **Neural Importance Sampling for Rapid and Reliable Gravitational-Wave Inference** (2023)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Maximilian Dax, Stephen R. Green, Jonathan Gair, Michael Pürrer, Jonas Wildberger, Jakob H. Macke, Alessandra Buonanno, Bernhard Schölkopf<br />┃🏷️ likelihood-based┃ ┃🏷️ physics┃ ┃🏷️ parameter estimation┃<br />[[Paper]](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.130.171403) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{dax2023neural,
  title = {Neural Importance Sampling for Rapid and Reliable Gravitational-Wave Inference},
  year = {2023},
  journal = {Physical Review Letters},
  volume = {130},
  number = {17},
  pages = {171403},
  doi = {10.1103/PhysRevLett.130.171403},
  author = {Dax and Green and Gair and Pürrer and Wildberger and Macke and Buonanno and Schölkopf}
  }
  </code>
  </pre></details>

- **Calibrating Neural Simulation-Based Inference with Differentiable Coverage Probability** (2023)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Maciej Falkiewicz, Naoya Takeishi, Imahn Shekhzadeh, Antoine Wehenkel, Arnaud Delaunoy, Gilles Louppe, Alexandros Kalousis<br />┃🏷️ diagnostics┃ ┃🏷️ simulation-based┃<br />[[Paper]](https://proceedings.neurips.cc/paper_files/paper/2023/file/03a9a9c1e15850439653bb971a4ad4b3-Paper-Conference.pdf) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{falkiewicz2023calibrating,
  title = {Calibrating Neural Simulation-Based Inference with Differentiable Coverage Probability},
  booktitle = {Thirty-Seventh Conference on Neural Information Processing Systems},
  year = {2023},
  author = {Falkiewicz and Takeishi and Shekhzadeh and Wehenkel and Delaunoy and Louppe and Kalousis}
  }
  </code>
  </pre></details>

- **Amortized Bayesian Model Comparison With Evidential Deep Learning** (2023)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Stefan T. Radev, Marco D'Alessandro, Ulf K. Mertens, Andreas Voss, Ullrich Köthe, Paul-Christian Bürkner<br />┃🏷️ model comparison┃<br />[[Paper]](https://ieeexplore.ieee.org/abstract/document/9612724?casa_token=knr0jyL2bTAAAAAA:Dh8KfjVW9QJympB0c8UbUq8HozJjOw-BPBSdy1g-QUhPskT1IL-cN5RHFHU7EVJNyZnY78Id) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{radev2023amortized,
  title = {Amortized {{Bayesian Model Comparison With Evidential Deep Learning}}},
  year = {2023},
  journal = {IEEE Transactions on Neural Networks and Learning Systems},
  volume = {34},
  number = {8},
  pages = {4903--4917},
  issn = {2162-237X, 2162-2388},
  doi = {10.1109/TNNLS.2021.3124052},
  author = {Radev and D'Alessandro and Mertens and Voss and Köthe and Bürkner}
  }
  </code>
  </pre></details>

- **JANA: Jointly Amortized Neural Approximation of Complex Bayesian Models** (2023)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Stefan T. Radev, Marvin Schmitt, Valentin Pratz, Umberto Picchini, Ullrich Köthe, Paul-Christian Bürkner<br />┃🏷️ joint learning┃ ┃🏷️ simulation-based┃ ┃🏷️ diagnostics┃<br />[[Paper]](https://proceedings.mlr.press/v216/radev23a.html) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{radev2023jana,
  title = {{{JANA}}: {{Jointly}} Amortized Neural Approximation of Complex {{Bayesian}} Models},
  booktitle = {Proceedings of the Thirty-Ninth Conference on Uncertainty in Artificial Intelligence},
  year = {2023},
  series = {Proceedings of Machine Learning Research},
  volume = {216},
  pages = {1695--1706},
  publisher = {PMLR},
  author = {Radev and Schmitt and Pratz and Picchini and Köthe and Bürkner}
  }
  </code>
  </pre></details>

- **Fuse It or Lose It: Deep Fusion for Multimodal Simulation-Based Inference** (2023)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Marvin Schmitt, Stefan T. Radev, Paul-Christian Bürkner<br />┃🏷️ summary learning┃ ┃🏷️ parameter estimation┃<br />[[Paper]](https://arxiv.org/abs/2311.10671) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @misc{schmitt2023fuse,
  title = {Fuse {{It}} or {{Lose It}}: {{Deep Fusion}} for {{Multimodal Simulation-Based Inference}}},
  shorttitle = {Fuse {{It}} or {{Lose It}}},
  year = {2023},
  number = {arXiv:2311.10671},
  eprint = {2311.10671},
  publisher = {arXiv},
  archiveprefix = {arXiv},
  author = {Schmitt and Radev and Bürkner}
  }
  </code>
  </pre></details>

- **Flow Matching for Scalable Simulation-Based Inference** (2023)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Jonas Wildberger, Maximilian Dax, Simon Buchholz, Stephen Green, Jakob H Macke, Bernhard Schölkopf<br />┃🏷️ simulation-based┃<br />[[Paper]](https://arxiv.org/abs/2305.17161) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{wildberger2023flow,
  title = {Flow Matching for Scalable Simulation-Based Inference},
  booktitle = {Advances in Neural Information Processing Systems},
  year = {2023},
  volume = {36},
  pages = {16837--16864},
  author = {Wildberger and Dax and Buchholz and Green and Macke and Schölkopf}
  }
  </code>
  </pre></details>

- **Investigating the Impact of Model Misspecification in Neural Simulation-based Inference** (2022)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Patrick Cannon, Daniel Ward, Sebastian M. Schmon<br />┃🏷️ diagnostics┃ ┃🏷️ misspecification┃ ┃🏷️ simulation-based┃<br />[[Paper]](https://arxiv.org/abs/2209.01845) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @misc{cannon2022investigating,
  title = {Investigating the {{Impact}} of {{Model Misspecification}} in {{Neural Simulation-based Inference}}},
  year = {2022},
  number = {arXiv:2209.01845},
  eprint = {2209.01845},
  primaryclass = {stat},
  publisher = {arXiv},
  archiveprefix = {arXiv},
  author = {Cannon and Ward and Schmon}
  }
  </code>
  </pre></details>

- **Robust Neural Posterior Estimation and Statistical Model Criticism** (2022)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Daniel Ward, Patrick Cannon, Mark Beaumont, Matteo Fasiolo, Sebastian M. Schmon<br />┃🏷️ model evaluation┃ ┃🏷️ simulation-based┃<br />[[Paper]](https://proceedings.neurips.cc/paper_files/paper/2022/hash/db0eac6747e3631eb91095cd76065611-Abstract-Conference.html) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{ward2022robust,
  title = {Robust Neural Posterior Estimation and Statistical Model Criticism},
  booktitle = {Proceedings of the 36th International Conference on Neural Information Processing Systems},
  year = {2022},
  author = {Ward and Cannon and Beaumont and Fasiolo and Schmon}
  }
  </code>
  </pre></details>

- **Deep Adaptive Design: Amortizing Sequential Bayesian Experimental Design** (2021)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Adam Foster, Desi R. Ivanova, Malik Ilyas, Tom Rainforth<br />┃🏷️ experimental design┃ ┃🏷️ adaptive design┃<br />[[Paper]](http://proceedings.mlr.press/v139/foster21a.html) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{foster2021deep,
  title = {Deep {{Adaptive Design}}: {{Amortizing Sequential Bayesian Experimental Design}}},
  booktitle = {Proceedings of the 38th {{International Conference}} on {{Machine Learning}}},
  year = {2021},
  volume = {139},
  publisher = {PMLR},
  author = {Foster and Ivanova and Ilyas and Rainforth}
  }
  </code>
  </pre></details>

- **BayesFlow: Learning Complex Stochastic Models With Invertible Neural Networks** (2020)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Stefan T. Radev, Ulf K. Mertens, Andreas Voss, Lynton Ardizzone, Ullrich Köthe<br />┃🏷️ simulation-based┃ ┃🏷️ summary learning┃ ┃🏷️ parameter estimation┃<br />[[Paper]](https://ieeexplore.ieee.org/abstract/document/9298920?casa_token=fdTVHBVa5Z4AAAAA:Un2ZODPlovOuoZZaCPLPrBwA58re3eYXPMbBx9u_WAj9PRUJj34W3hTEuSG1osciKgjzZpiS) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{radev2020bayesflow,
  title = {{{BayesFlow}}: {{Learning Complex Stochastic Models With Invertible Neural Networks}}},
  shorttitle = {{{BayesFlow}}},
  year = {2020},
  journal = {IEEE Transactions on Neural Networks and Learning Systems},
  volume = {33},
  number = {4},
  pages = {1452--1466},
  issn = {2162-237X, 2162-2388},
  doi = {10.1109/TNNLS.2020.3042395},
  author = {Radev and Mertens and Voss and Ardizzone and Köthe}
  }
  </code>
  </pre></details>
## Application Papers

- **Advancing Tools for Simulation-Based Inference** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Henning Bahl, Victor Bresó, Giovanni De Crescenzo, Tilman Plehn<br />┃🏷️ physics┃ ┃🏷️ simulation-based┃<br />[[Paper]](https://arxiv.org/abs/2410.07315) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @misc{bahl2024advancing,
  title = {Advancing {{Tools}} for {{Simulation-Based Inference}}},
  year = {2024},
  number = {arXiv:2410.07315},
  eprint = {2410.07315},
  primaryclass = {hep-ph},
  publisher = {arXiv},
  archiveprefix = {arXiv},
  author = {Bahl and Bresó and Crescenzo and Plehn}
  }
  </code>
  </pre></details>

- **Amortized Template-Matching of Molecular Conformations from Cryo-Electron Microscopy Images Using Simulation-Based Inference** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Lars Dingeldein, David Silva-Sánchez, Luke Evans, Edoardo D'Imprima, Nikolaus Grigorieff, Roberto Covino, Pilar Cossio<br />┃🏷️ biology┃ ┃🏷️ simulation-based┃ ┃🏷️ parameter estimation┃<br />[[Paper]](https://www.biorxiv.org/content/10.1101/2024.07.23.604154v2.abstract) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{dingeldein2024amortized,
  title = {Amortized Template-Matching of Molecular Conformations from Cryo-Electron Microscopy Images Using Simulation-Based Inference},
  year = {2024},
  journal = {bioRxiv : the preprint server for biology},
  pages = {2024.07.23.604154},
  doi = {10.1101/2024.07.23.604154},
  author = {Dingeldein and Silva-Sánchez and Evans and D'Imprima and Grigorieff and Covino and Cossio}
  }
  </code>
  </pre></details>

- **Simulation-Based Inference for Cardiovascular Models** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Antoine Wehenkel, Jens Behrmann, Andrew C. Miller, Guillermo Sapiro, Ozan Sener, Marco Cuturi Cameto, Jörn-Henrik Jacobsen<br />┃🏷️ medicine┃ ┃🏷️ simulation-based┃ ┃🏷️ parameter estimation┃<br />[[Paper]](https://arxiv.org/abs/2307.13918) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{wehenkel2024simulationbased,
  title = {Simulation-Based Inference for Cardiovascular Models},
  booktitle = {{{NeurIPS}} Workshop},
  year = {2024},
  author = {Wehenkel and Behrmann and Miller and Sapiro and Sener and Cameto and Jacobsen}
  }
  </code>
  </pre></details>

- **Evaluating Sparse Galaxy Simulations via Out-of-Distribution Detection and Amortized Bayesian Model Comparison** (2024)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Lingyi Zhou, Stefan T. Radev, William H. Oliver, Aura Obreja, Zehao Jin, Tobias Buck<br />┃🏷️ physics┃ ┃🏷️ model evaluation┃ ┃🏷️ model comparison┃<br />[[Paper]](https://arxiv.org/abs/2410.10606) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{zhou2024evaluating,
  title = {Evaluating {{Sparse Galaxy Simulations}} via {{Out-of-Distribution Detection}} and {{Amortized Bayesian Model Comparison}}},
  booktitle = {38th {{Conference}} on {{Neural Information Processing Systems}}},
  year = {2024},
  author = {Zhou and Radev and Oliver and Obreja and Jin and Buck}
  }
  </code>
  </pre></details>

- **A General Integrative Neurocognitive Modeling Framework to Jointly Describe EEG and Decision-making on Single Trials** (2023)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Amin Ghaderi-Kangavari, Jamal Amani Rad, Michael D. Nunez<br />┃🏷️ cognitive modeling┃ ┃🏷️ simulation-based┃ ┃🏷️ parameter estimation┃<br />[[Paper]](https://link.springer.com/article/10.1007/s42113-023-00167-4) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{ghaderi-kangavari2023general,
  title = {A {{General Integrative Neurocognitive Modeling Framework}} to {{Jointly Describe EEG}} and {{Decision-making}} on {{Single Trials}}},
  year = {2023},
  journal = {Computational Brain \& Behavior},
  volume = {6},
  number = {3},
  pages = {317--376},
  issn = {2522-0861, 2522-087X},
  doi = {10.1007/s42113-023-00167-4},
  author = {Ghaderi-Kangavari and Rad and Nunez}
  }
  </code>
  </pre></details>

- **Amortized Inference with User Simulations** (2023)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Hee-Seung Moon, Antti Oulasvirta, Byungjoo Lee<br />┃🏷️ human-computer interaction┃ ┃🏷️ simulation-based┃ ┃🏷️ user interfaces┃<br />[[Paper]](https://dl.acm.org/doi/pdf/10.1145/3544548.3581439) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{moon2023amortized,
  title = {Amortized Inference with User Simulations},
  booktitle = {Proceedings of the 2023 {{CHI}} Conference on Human Factors in Computing Systems},
  year = {2023},
  series = {Chi '23},
  publisher = {Association for Computing Machinery},
  doi = {10.1145/3544548.3581439},
  author = {Moon and Oulasvirta and Lee}
  }
  </code>
  </pre></details>

- **Neural Superstatistics for Bayesian Estimation of Dynamic Cognitive Models** (2023)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Lukas Schumacher, Paul-Christian Bürkner, Andreas Voss, Ullrich Köthe, Stefan T. Radev<br />┃🏷️ simulation-based┃ ┃🏷️ dynamic modeling┃ ┃🏷️ parameter estimation┃<br />[[Paper]](https://www.nature.com/articles/s41598-023-40278-3) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{schumacher2023neural,
  title = {Neural Superstatistics for {{Bayesian}} Estimation of Dynamic Cognitive Models},
  year = {2023},
  journal = {Scientific Reports},
  volume = {13},
  number = {1},
  pages = {13778},
  issn = {2045-2322},
  doi = {10.1038/s41598-023-40278-3},
  langid = {english},
  author = {Schumacher and Bürkner and Voss and Köthe and Radev}
  }
  </code>
  </pre></details>

- **Reliable Amortized Variational Inference with Physics-Based Latent Distribution Correction** (2023)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Ali Siahkoohi, Gabrio Rizzuti, Rafael Orozco, Felix J. Herrmann<br />┃🏷️ physics┃ ┃🏷️ correction┃ ┃🏷️ misspecification┃<br />[[Paper]](https://library.seg.org/doi/abs/10.1190/geo2022-0472.1) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{siahkoohi2023reliable,
  title = {Reliable Amortized Variational Inference with Physics-Based Latent Distribution Correction},
  year = {2023},
  journal = {GEOPHYSICS},
  volume = {88},
  number = {3},
  pages = {R297-R322},
  issn = {0016-8033, 1942-2156},
  doi = {10.1190/geo2022-0472.1},
  langid = {english},
  author = {Siahkoohi and Rizzuti and Orozco and Herrmann}
  }
  </code>
  </pre></details>

- **Probabilistic Damage Detection Using a New Likelihood-Free Bayesian Inference Method** (2023)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Jice Zeng, Michael D. Todd, Zhen Hu<br />┃🏷️ structural health monitoring┃<br />[[Paper]](https://link.springer.com/article/10.1007/s13349-022-00638-5) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{zeng2023probabilistic,
  title = {Probabilistic Damage Detection Using a New Likelihood-Free {{Bayesian}} Inference Method},
  year = {2023},
  journal = {Journal of Civil Structural Health Monitoring},
  volume = {13},
  number = {2-3},
  pages = {319--341},
  issn = {2190-5452, 2190-5479},
  doi = {10.1007/s13349-022-00638-5},
  langid = {english},
  author = {Zeng and Todd and Hu}
  }
  </code>
  </pre></details>

- **Towards Reliable Parameter Extraction in MEMS Final Module Testing Using Bayesian Inference** (2022)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Monika E. Heringhaus, Yi Zhang, Andr'e Zimmermann, Lars Mikelsons<br />┃🏷️ parameter estimation┃ ┃🏷️ simulation-based┃ ┃🏷️ engineering┃<br />[[Paper]](https://www.mdpi.com/1424-8220/22/14/5408) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{heringhaus2022reliable,
  title = {Towards {{Reliable Parameter Extraction}} in {{MEMS Final Module Testing Using Bayesian Inference}}},
  year = {2022},
  journal = {Sensors},
  volume = {22},
  number = {14},
  pages = {5408},
  issn = {1424-8220},
  doi = {10.3390/s22145408},
  author = {Heringhaus and Zhang and Zimmermann and Mikelsons}
  }
  </code>
  </pre></details>

- **Mental Speed Is High until Age 60 as Revealed by Analysis of over a Million Participants** (2022)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Mischa von Krause, Stefan T. Radev, Andreas Voss<br />┃🏷️ cognitive modeling┃ ┃🏷️ parameter estimation┃<br />[[Paper]](https://www.nature.com/articles/s41562-021-01282-7) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{vonkrause2022mental,
  title = {Mental Speed Is High until Age 60 as Revealed by Analysis of over a Million Participants},
  year = {2022},
  journal = {Nature Human Behaviour},
  volume = {6},
  number = {5},
  pages = {700--708},
  issn = {2397-3374},
  doi = {10.1038/s41562-021-01282-7},
  langid = {english},
  author = {von Krause and Radev and Voss}
  }
  </code>
  </pre></details>

- **Model Updating of Wind Turbine Blade Cross Sections with Invertible Neural Networks** (2022)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Pablo Noever-Castelos, Lynton Ardizzone, Claudio Balzani<br />┃🏷️ simulation-based┃<br />[[Paper]](https://onlinelibrary.wiley.com/doi/full/10.1002/we.2687) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{noever-castelos2022model,
  title = {Model Updating of Wind Turbine Blade Cross Sections with Invertible Neural Networks},
  year = {2022},
  journal = {Wind Energy},
  volume = {25},
  number = {3},
  pages = {573--599},
  issn = {1095-4244, 1099-1824},
  doi = {10.1002/we.2687},
  langid = {english},
  author = {Noever-Castelos and Ardizzone and Balzani}
  }
  </code>
  </pre></details>

- **Inverse Design under Uncertainty Using Conditional Normalizing Flows** (2022)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Panagiotis Tsilifis, Sayan Ghosh<br />┃🏷️ engineering┃ ┃🏷️ aerospace┃ ┃🏷️ simulation-based┃<br />[[Paper]](https://arc.aiaa.org/doi/abs/10.2514/6.2022-0631) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @inproceedings{tsilifis2022inverse,
  title = {Inverse {{Design}} under {{Uncertainty}} Using {{Conditional Normalizing Flows}}},
  booktitle = {{{AIAA SCITECH}} 2022 {{Forum}}},
  year = {2022},
  publisher = {{American Institute of Aeronautics and Astronautics}},
  address = {San Diego, CA \& Virtual},
  doi = {10.2514/6.2022-0631},
  isbn = {978-1-62410-631-6},
  langid = {english},
  author = {Tsilifis and Ghosh}
  }
  </code>
  </pre></details>

- **Measuring QCD Splittings with Invertible Networks** (2021)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Sebastian Bieringer, Anja Butter, Theo Heimel, Stefan Höche, Ullrich Köthe, Tilman Plehn, Stefan T. Radev<br />┃🏷️ simulation-based┃ ┃🏷️ physics┃ ┃🏷️ parameter estimation┃<br />[[Paper]](https://www.scipost.org/10.21468/SciPostPhys.10.6.126?acad_field_slug=astronomy) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{bieringer2021measuring,
  title = {Measuring {{QCD}} Splittings with Invertible Networks},
  year = {2021},
  journal = {SciPost Physics},
  volume = {10},
  pages = {126},
  doi = {10.21468/SciPostPhys.10.6.126},
  author = {Bieringer and Butter and Heimel and Höche and Köthe and Plehn and Radev}
  }
  </code>
  </pre></details>

- **OutbreakFlow: Model-based Bayesian Inference of Disease Outbreak Dynamics with Invertible Neural Networks and Its Application to the COVID-19 Pandemics in Germany** (2021)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Stefan T. Radev, Frederik Graw, Simiao Chen, Nico T. Mutters, Vanessa M. Eichel, Till Bärnighausen, Ullrich Köthe<br />┃🏷️ epidemiology┃ ┃🏷️ public health┃ ┃🏷️ simulation-based┃<br />[[Paper]](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009472) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{radev2021outbreakflow,
  title = {{{OutbreakFlow}}: {{Model-based Bayesian}} Inference of Disease Outbreak Dynamics with Invertible Neural Networks and Its Application to the {{COVID-19}} Pandemics in {{Germany}}},
  shorttitle = {{{OutbreakFlow}}},
  year = {2021},
  journal = {PLOS Computational Biology},
  volume = {17},
  number = {10},
  pages = {e1009472},
  issn = {1553-7358},
  doi = {10.1371/journal.pcbi.1009472},
  langid = {english},
  author = {Radev and Graw and Chen and Mutters and Eichel and Bärnighausen and Köthe}
  }
  </code>
  </pre></details>

- **Estimation of Agent-Based Models Using Bayesian Deep Learning Approach of BayesFlow** (2021)<br />_Reading this paper? Please consider contributing a TLDR summary._<br />by Takashi Shiono<br />┃🏷️ agent modeling┃ ┃🏷️ simulation-based┃<br />[[Paper]](https://www.sciencedirect.com/science/article/pii/S0165188921000178?casa_token=lM5bqeFY9-AAAAAA:usisG1ypAZdWNDwk39x_KdFGIvgKXoxYD9x0fukFWDyiqBEtXHaLPRIFhShjyeXdAmvoKgwNmA) 
  <details>
  <summary>Show BibTeX</summary>
  <pre><code>
  @article{shiono2021estimation,
  title = {Estimation of Agent-Based Models Using {{Bayesian}} Deep Learning Approach of {{BayesFlow}}},
  year = {2021},
  journal = {Journal of Economic Dynamics and Control},
  volume = {125},
  pages = {104082},
  issn = {01651889},
  doi = {10.1016/j.jedc.2021.104082},
  langid = {english},
  author = {Shiono}
  }
  </code>
  </pre></details>
