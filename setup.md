https://docs.gitlab.com/runner/install/kubernetes.html

For some tests, I use my own namespace: `kibi9872`.
Disable shared group runners for the project, we want that everything runs via our own runners.

Create service account for TIRA, used by the runner to create pods.

```
kubectl -n kibi9872 apply -f k8s-tira-service-account.yml
kubectl -n kibi9872 apply -f k8s-no-internet-network-policy.yml
```

To start from scratch, run:

```
helm uninstall --namespace kibi9872 gitlab-runner-tira-evaluators; \
helm uninstall --namespace kibi9872 gitlab-runner-tira-user-software; \
helm uninstall --namespace kibi9872 gitlab-runner-tira-copy
```

Then, install the runners:

```
helm install --namespace kibi9872 gitlab-runner-tira-evaluators -f k8s-gitlab-runner-tira-evaluators-config.yml gitlab/gitlab-runner; \
helm install --namespace kibi9872 gitlab-runner-tira-user-software -f k8s-gitlab-runner-tira-user-software-config.yml gitlab/gitlab-runner; \
helm install --namespace kibi9872 gitlab-runner-tira-copy -f k8s-gitlab-runner-tira-copy-config.yml gitlab/gitlab-runner
```

After this command, the runner should be available in  "Settings" -> "CI/CD Settings" -> "Runners" -> "Specific runners" section.


