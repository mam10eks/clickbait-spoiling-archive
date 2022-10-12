# Archive of the [Clickbait Challenge at SemEval 2023](https://pan.webis.de/semeval23/pan23-web/clickbait-challenge.html)

Clickbait posts link to web pages and advertise their content by arousing curiosity instead of providing informative summaries. Clickbait spoiling aims at generating short texts that satisfy the curiosity induced by a clickbait post. This repository serves as archive of the [shared task on clickbait spoiling](https://pan.webis.de/semeval23/pan23-web/clickbait-challenge.html) that did run as part of [SemEval 2023](https://semeval.github.io/SemEval2023/).

The following figure illustrates some example inputs and the expected output for clickbait spoiling:

![twitter-clickbait-examples](https://user-images.githubusercontent.com/10050886/195431904-2c53a25d-2bbc-4e10-bd6a-a69871c3ce9c.png)

The repository contains all datasets and (dockerized) software submissions and evaluators.
Those software submissions and evaluators can be easily applied to new/manipulated data, allowing novel evaluations and experiments, thereby maximizing the impact of a shared task (in terms of reproducibility/reusability/replicability/follow-up studies, etc.).

**This repository currently includes only the baselines as the shared task is currently running (to prevent side effects to participants). After completion of the shared task, all submitted approaches can be executed and evaluated (as they are all available in Docker images) as shown in the examples of this repository.**

The notebook [Tutorial.ipynb](Tutorial.ipynb) shows different use cases: (1)  Re-evaluation of submitted approaches, and (2) execution of submitted approaches on new or manipulated data (e.g., for ablation studies or ensembles).

# Quick Overview

All software submissions are dockerized.
So you can apply them easily to new data.

E.g., you can run the approach `express-pitch` of the group `princess-knight` from the `clickbait-spoiling` task by using the `tira` wrapper:

```
# Prepare a dataset
df = pd.DataFrame([
    {"uuid": "1", "postText": ["Some text"], "targetParagraphs": ["A bit of text from the linked page"], "targetTitle": "The title of the linked page", "spoiler": ["Does not exist."]},
])

# Apply the approach 'clickbait-spoiling/princess-knight/express-pitch' to the dataset
tira.run('clickbait-spoiling/princess-knight/express-pitch', data=df)
```



Similarly, you can directly get the predictions and directly evaluate them on task-2 on spoiler generation:

```
tira.run('clickbait-spoiling/princess-knight/express-pitch', data=df, evaluate='task-2-spoiler-generation')
```

A full documentation of the `tira` wrapper for post-hoc experimentations after a shared task is documented in [TIRA's documentation](https://github.com/tira-io/tira/wiki).

