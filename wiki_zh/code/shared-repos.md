# 共享仓库

实验室所有代码都存放在 **yelab0** Gitee 组织下：https://gitee.com/yelab0。平台策略、git 访问配置与镜像规则：见 [Git 与 Gitee 规范](git-gitee.md)。

## 实验室自有仓库

| 仓库 | 说明 | 维护者 |
|---|---|---|
| [yelab-wiki](https://gitee.com/yelab0/yelab-wiki) | 本 wiki | {{NAME}} |
| {{REPO_1}} | {{DESCRIPTION}} | {{NAME}} |

## 第三方镜像

- 非本实验室所有的仓库镜像统一命名为 `mirror-<owner>-<repo>`，设为私有、只读——详见 [Git 与 Gitee 规范](git-gitee.md#third-party-upstream-repos)

## 实验室仓库的规范

- 命名：`lowercase-with-dashes`
- 默认分支为 `main`；共享项目使用功能分支 + pull request 流程
- 每个仓库都要有 README：它是什么、如何安装、如何运行、由谁维护
- 目录结构：`src/` 放库代码，`scripts/` 放入口脚本，`notebooks/` 放探索性分析，`configs/` 放实验配置，`tests/` 放测试
- 代码风格：{{STYLE}}——例如 Python 使用 black/ruff，并配置 pre-commit 钩子

## 协作开发共享代码

- 修改共享文件时，先 ping 最近改过该文件的人，做一次非正式评审
- 勤提交、勤推送——不要让未提交的修改堆积在服务器上
- 大数据、权重和结果文件永远不要放进 git——见 [数据服务器](../experimental/data-server.md)
