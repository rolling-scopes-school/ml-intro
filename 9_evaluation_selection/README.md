# Model evaluation and selection

> "Here is a system. I'm very sure that it's terrible." - *Yaser Abu-Mostafa*

Welcome to the evaluation and selection module of the RS School Machine Learning course. Hopefully, this module will help you to learn:
- How to select the best model and evaluate its performance.
- How to track your model experiments.
- How to organize your ML project.
- How to write a clean, reproducible, and flexible code.

This module has an assignment that is quite voluminous. Start working early to complete it before the deadline.

## Model evaluation and selection
1. A series of blog posts on model evaluation and selection from Sebastian Raschka (parts [1](https://sebastianraschka.com/blog/2016/model-evaluation-selection-part1.html), [2](https://sebastianraschka.com/blog/2016/model-evaluation-selection-part2.html), [3](https://sebastianraschka.com/blog/2016/model-evaluation-selection-part3.html), and [4](https://sebastianraschka.com/blog/2018/model-evaluation-selection-part4.html)). It discusses what evaluation and selection are and how to estimate their uncertainty. Feel free to skip any complicated maths, rather try to focus on what may be useful for you: holdout, k-fold, and nested cross-validation.
2. [Cross Validation in Time Series](https://medium.com/@soumyachess1496/cross-validation-in-time-series-566ae4981ce4). This article will tell you about validating time series models. However, the concept described there is very important and often used with any temporal features data, even if it's not time series. So study it carefully and try to understand well why we can't use a simple random split in this case.
3. Scikit learn [guide](https://scikit-learn.org/stable/model_selection.html) to cross-validation with code examples
4. Another [guide](https://weina.me/nested-cross-validation/) to nested cross-validation with a nice visualization. 

## Tracking experiments
1. [ML Experiment Tracking: What It Is, Why It Matters, and How to Implement It](https://neptune.ai/blog/ml-experiment-tracking)
2. [How We Track Machine Learning Experiments with MLFlow](https://www.datarevenue.com/en-blog/how-we-track-machine-learning-experiments-with-mlflow)

## Organizing your projects
Usually using Jupyter notebooks to write all or even some of your project code is not a good idea: it's difficult to manage versions with git, test, format, reproduce and run such code. You can watch [this talk](https://www.youtube.com/watch?v=7jiPeIFXb6U) by Joel Grus for a more detailed argumentation. But if using notebooks is a bad practice, what should we do instead?  
There is no universal pattern for project organization. Python is a flexible language – it allows you to choose layouts and tools that are best for your specific case. The best advice that you should follow in all cases is [The Zen of Python](https://www.python.org/dev/peps/pep-0020/), which works for project structures as well as for code.  
However, you don't have to reinvent the wheel. Below are the links to what worked well for other people: study them, adapt, and possibly combine the approaches.
Also, stay updated on new instruments since they are emerging every time.  
In most cases and with any structures you should use a separate virtual environment for each of your projects. If you are unfamiliar with the concept, watch [this video](https://www.youtube.com/watch?v=KxvKCSwlUv8). There are alternatives to venv popular among data scientists, such as conda or poetry, but try to understand venv first as the most simple one.
1. [Structuring Your Project](https://docs.python-guide.org/writing/structure/) from The Hitchhiker's Guide to Python. Simple, vanilla Python approach with no additional tools. Even if you prefer more modern approaches, read this guide to understand what's happening under the hood and learn best practices. 
2. Go through the chapters of [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) by Claudio Jolowicz. Here you can look at a (hyper)modern approach to structuring a Python package. Well, at least for 2020 when this article was written. The approach is to use lots of fancy tools that make our life much easier but sometimes introduce annoying bugs. It will teach you not only to structure your project but to test, format, lint, document, etc., etc. It also has a [cookiecutter](https://github.com/cjolowicz/cookiecutter-hypermodern-python) that's being updated and maybe even more hypermodern than the article itself.
3. [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) offers you a structure developed specifically for ML projects. 

## Code style, reproducibility, testing
It's a myth that Data Scientists shouldn't write high-quality code since they are more researchers than engineers. ML systems can be more complex than any others and they possess even more risks for [technical debt](https://proceedings.neurips.cc/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf). That's why it's important to design solutions of high quality, follow style guides, and test your applications.  
1. [PEP-8](https://www.python.org/dev/peps/pep-0008/) is a style guide to follow when writing Python code. You don't have to remember all the rules – there are the instruments that will detect if you break them automatically, such as [flake8](https://flake8.pycqa.org/en/latest/).
2. You can make Python development more pleasurable and efficient if you use type annotations. Watch [this talk](https://www.youtube.com/watch?v=pMgmKJyWKn8) if you want to know why and how to do it.
3. [Reproducibility, Replicability, and Data Science](https://www.kdnuggets.com/2019/11/reproducibility-replicability-data-science.html).
4. [Here](https://realpython.com/python-testing/) is the tutorial for beginners at testing Python code. 
5. Testing machine learning models can be trickier than testing traditional software, see [this article](https://www.jeremyjordan.me/testing-ml/) for details. 
6. There are several approaches to testing software. If you already know how to write tests in Python and are thinking about when to write them, how to find the balance between reliability and complexity of your tests, you may find [this talk](https://www.youtube.com/watch?v=EZ05e7EMOLM) on Test-Driven Development helpful. 

## Assignment
You can see the assignment for this module in the HOMEWORK.md file. Good luck!
