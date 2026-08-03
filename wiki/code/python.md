# Python

## Learning python

- {{LEARNING_RESOURCE_1}} — e.g. a course or book the lab recommends
- {{LEARNING_RESOURCE_2}}
- Best way to learn: pick a small real analysis task and ask a labmate to review your code — see the [expert list](../science/expert-list.md)

## Lab dev environment

The lab-standard setup. Deviations are fine, but this is what's known to work and what others can help you debug.

We use **conda** (miniconda or anaconda) for environment management:

```bash
conda create -n myproject python=3.11
conda activate myproject
```

Conventions:

- One environment per project, never install into `base`
- Every project repo should include an `environment.yml` or `requirements.txt`
- Standard packages: {{STANDARD_PACKAGES}} — e.g. numpy, scipy, pytorch, ...

## Editors

{{EDITOR_POLICY}} — e.g. VS Code is common in the lab; remote-ssh works well for the compute servers.

## Dotfiles / shared configs

{{DOTFILES_REPO}} — link to lab dotfiles repo if one exists.

## Lab network notes

{{LOCAL_SETUP_NOTES}} — proxy settings, internal mirrors, anything needed on the lab network.

```bash
# example: faster package installs inside China
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
