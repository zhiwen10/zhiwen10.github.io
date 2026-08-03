# Python

## 学习 Python

- {{LEARNING_RESOURCE_1}} — 例如实验室推荐的课程或书籍
- {{LEARNING_RESOURCE_2}}
- 最好的学习方式：挑一个小型真实分析任务，并请实验室同事帮你审查代码 — 参见[专家名单](../science/expert-list.md)

## 实验室开发环境

实验室的标准配置。有所偏差没关系，但这是已知可用、且其他人能帮你排查问题的配置。

我们使用 **conda**（miniconda 或 anaconda）进行环境管理：

```bash
conda create -n myproject python=3.11
conda activate myproject
```

约定：

- 每个项目一个环境，绝不要安装到 `base` 中
- 每个项目仓库都应包含 `environment.yml` 或 `requirements.txt`
- 标准软件包：{{STANDARD_PACKAGES}} — 例如 numpy、scipy、pytorch 等

## 编辑器

{{EDITOR_POLICY}} — 例如实验室常用 VS Code；remote-ssh 对计算服务器很好用。

## Dotfiles / 共享配置

{{DOTFILES_REPO}} — 如果有实验室 dotfiles 仓库，在此附上链接。

## 实验室网络说明

{{LOCAL_SETUP_NOTES}} — 代理设置、内部镜像源，以及在实验室网络环境下所需的任何信息。

```bash
# 示例：在国内更快地安装软件包
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
