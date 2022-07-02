https://docs.gitlab.com/runner/install/kubernetes.html

For some tests, I use my own namespace: `kibi9872`.

To start from scratch, run:

```
helm uninstall --namespace kibi9872 gitlab-runner-tira-evaluators; \
helm uninstall --namespace kibi9872 gitlab-runner-tira-user-software; \
helm uninstall --namespace kibi9872 gitlab-runner-tira-copy
```

Then, install the runners:

```
helm install --namespace kibi9872 gitlab-runner-tira-evaluators -f k8s-gitlab-runner-tira-evaluators-config.yml gitlab/gitlab-runner \
helm install --namespace kibi9872 gitlab-runner-tira-user-software -f k8s-gitlab-runner-tira-user-software-config.yml gitlab/gitlab-runner
```

After this command, the runner should be available in  "Settings" -> "CI/CD Settings" -> "Runners" -> "Specific runners" section.


