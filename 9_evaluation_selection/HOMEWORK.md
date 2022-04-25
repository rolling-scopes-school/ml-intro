# Evaluation-selection homework

Welcome to the assignment of evaluation and selection module. This time we encourage you to implement an ML project from scratch with a structure close to production ML projects. To simplify things a little bit, you will implement only model training, evaluation, and selection steps. As a challenge, you can try to add deployment and inference steps later after finishing the RS course. 

## How to solve it?

Carefully read all the instructions before writing any code. Don't worry if it seems too complicated at first glance — it's meant to be. Decompose the big task into small and easy tasks and implement them one by one. We prepared a [demo solution](https://github.com/rolling-scopes-school/ml-project-demo) for another dataset that can help you while implementing yours. You don't have and shouldn't follow it entirely, but use it as a guide. For some tasks, you'll have to do things that are not implemented in the demo: that's an exercise for finding the necessary information on your own. 

There are three kinds of tasks: necessary conditions, good to have, and optional. Everything that is not marked as optional or necessary is good to have. You'll need to pass the necessary conditions to get more than 0 points for this homework, but there are not so many of them. Concentrate on good to have tasks, do them as well as you can. Do optional tasks only if you have some time and energy left, and are confident that other tasks are implemented with great quality.

If you're worried that someone may steal your work, start with a private Github repository. You'll need to make it public before submitting it for peer review, all your previous commits will become public after that. Submit a link to your public repository. Before submitting, check that everything is shown correctly to other people by opening the link you provide in a private window.  

## How to review it?

If you're reviewing someone else's homework, you should receive a link to a public Github repository with this person's solution. Calculate points as stated in bold font after most of the tasks in the statement. If you see that some tasks are done not fully, you can count a partial number of points for these tasks. If there is nothing specified in bold font, it means either that there are no points for this task or it's comprised fully of sub-tasks and doesn't have value on its own. To calculate the total result, sum up points from all tasks that have points. 

The maximum number of points for this HW is 100, 22 of them are for optional tasks.

Please, leave feedback for each task: don't just write the total number of points a student received.  

You can use [this spreadsheet](https://docs.google.com/spreadsheets/d/14QBY9aSRnKsx2mTYm-5OFBIV_NBg0Xh-QbcO6U3QlpY/edit?usp=sharing) as a template for your review. Make a copy of it and fill it out during the review: you'll see a total amount of points at the bottom. Send a final version to the person you were reviewing.

## Homework statement

1. Use the [Forest train dataset](https://www.kaggle.com/competitions/forest-cover-type-prediction). You will solve the task of forest cover type prediction and compete with other participants. **(necessary condition, 0 points for the whole homework if not done)**
2. Format your homework as a Python package. Use an [src layout](https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure) or choose some other layout that seems reasonable to you, explain your choice in the README file. Don't use Jupyter Notebooks for this homework. Instead, write your code in .py files. **(necessary condition, 0 points for the whole homework if not done)**
3. Publish your code to Github. **(necessary condition, 0 points for the whole homework if not done)**
    1. Commits should be small and pushed while you're working on a project (not at the last moment, since storing unpublished code locally for a long time is not reliable: imagine something bad happens to your PC and you lost all your code). Your repository should have at least 30 commits if you do all non-optional parts of this homework. **(12 points)**
4. Use [Poetry](https://python-poetry.org/) to manage your package and dependencies. **(6 points)**
    1. When installing dependencies, think if these dependencies will be used to run scripts from your package, or you'll need them only for development purposes (such as testing, formatting code, etc.). For development dependencies, use [the dev option of add command](https://python-poetry.org/docs/cli/#add). If you decided not to use Poetry, list your dependencies in requirements.txt and requirements-dev.txt files. **(4 points)**
5. Create a data folder and place the dataset there. **(necessary condition, 0 points for the whole homework if not done. *Note for reviewers: data folder won't be seen on GitHub if added to gitignore, it's OK, check gitignore*)**
    1. Don't forget to add your data to gitignore. **(5 points)**
    2. (optional) Write a script that will generate you an EDA report, e.g. with [pandas profiling](https://pandas-profiling.github.io/pandas-profiling/docs/master/rtd/)
6. Write a script that trains a model and saves it to a file. Your script should be runnable from the terminal, receive some arguments such as the path to data, model configurations, etc. To create CLI, you can use argparse, click (as in the demo), hydra, or some other alternatives. **(10 points)**
    1. (optional) Register your script in pyproject.toml. This way you can run it without specifying a full path to a script file. **(2 points)**
7. Choose some metrics to validate your model (at least 3) and calculate them after training. Use K-fold cross-validation. **(10 points maximum: 2 per metric + 4 for K-fold. *Note for reviewers: K-fold CV may be overwritten by nested CV if the 9th task is implemented, check the history of commits in this case. If more than 3 metrics were chosen, only 3 are graded*)**
8. Conduct experiments with your model. Track each experiment into MLFlow. Make a screenshot of the results in the MLFlow UI and include it in README. You can see the screenshot example below, but in your case, it may be more complex than that. Choose the best configuration with respect to a single metric (most important of all metrics you calculate, according to your opinion). 
    1. Try at least three different sets of hyperparameters for each model. **(3 points)**
    2. Try at least two different feature engineering techniques for each model. **(4 points)**
    3. Try at least two different ML models. **(4 points)**
    
    ![MLFlow experiments example](https://user-images.githubusercontent.com/40484210/147333877-8acc8c51-00f6-4278-bf76-05abf51301ab.png)
    
9. Instead of tuning hyperparameters manually, use automatic hyperparameter search for each model (choose a single metric again). Estimate quality with nested cross-validation, e.g. as described [here](https://machinelearningmastery.com/nested-cross-validation-for-machine-learning-with-python/). Although you used a single metric for model selection, the quality should be measured with all the metrics you chose in task 7. **(10 points)**
10. In your README, write instructions on how to run your code (training script and optionally other scripts you created, such as EDA). If someone who cloned your repository correctly follows the steps you describe, the script should work for them and produce the same results as it produced on your PC (so don't forget about specifying random seeds). The instructions should be as unambiguous and easy to follow as possible. **(10 points)**
    1. (optional) If you do the optional tasks below, add a development guide to README. You should specify what other developers should do to continue working on your code: what dependencies they should install, how they should run tests, formatting, etc. **(2 points)**
11. (optional) Test your code. Tests should be reproducible and depend only on your code, not on the data folder or external resources. To provide some data for a test, you should either [generate random data](https://faker.readthedocs.io/en/master/) during the test run or put a small sample of real data to the *tests/* folder, that will be excluded from gitignore. You should have at least one test that describes a situation when everything works fine (exit code 0, valid model produced), and one test that checks if it fails or returns an error message with invalid usage. Since you're working with files, you'll also need to create an isolated filesystem that will temporarily store test files and remove them after tests are finished.  Read how to do it [here](https://click.palletsprojects.com/en/8.0.x/testing/) for click, or find the solution yourself if you use other options for CLI. Provide a screenshot that tests are passed.
    1. (optional) Single or more tests for error cases without using fake/sample data and filesystem isolation, as in the demo. **(3 points)**
    2. (optional) Test for a valid input case with test data, filesystem isolation, and checking saved model for correctness. **(5 points)**
12. (optional) Format your code with black and lint it with flake8. Provide a screenshot that linting and formatting are passed. **(2 points)**
13. (optional) Type annotate your code, run mypy to ensure the types are correct. It's not necessary to use strict mode as in the demo, but make sure all of the methods you implemented are type annotated and used correctly throughout the code. Provide a screenshot of mypy report, it should be successful. **(3 points)**
14. (optional) To combine steps of testing and linting into a single command, use nox or tox session. Provide a single screenshot for all sessions, such as in the example below. **(2 points)**

![nox report](https://user-images.githubusercontent.com/40484210/147333990-86db2125-5aff-4bb7-9431-e92e4e8894cc.png)

15. (optional) Create a Github action that runs tests and linters against your code automatically each time you push to the main branch. Run it to see if it works. The status of your workflow should be 'completed successfully'. **(3 points *If you check someone else's work, you can verify the presence of passed Github actions as shown in the example below: if actions are present, you'll see the workflow runs after clicking on a button*)**

![GitHub actions button](https://user-images.githubusercontent.com/40484210/147334036-6915e696-f5ea-46a2-86ba-170c72ef578c.png)

![GitHub actions workflows](https://user-images.githubusercontent.com/40484210/147334079-6097c5db-762e-4f1c-ae3c-f01b7d98823f.png)
