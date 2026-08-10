# Git 与 Gitee 使用规范

## 平台策略

- **Gitee 是实验室的主力平台**（部分实验室网络无法访问 GitHub）
- 实验室组织：https://gitee.com/yelab0
- 部分实验室自有的仓库会推送镜像到 GitHub，以便国际同行访问
- 默认可见性：**私有**。在 Gitee 上将仓库设为公开需要经过平台人工审核——务必慎重操作

## 安装 git

Gitee 只是一个托管服务器——所有交互都通过 `git` 命令完成，所以请先安装 git。用 `git --version` 检查；如果能看到版本号，说明已经装好了。

**macOS**

```bash
xcode-select --install
```

这会安装 Apple 的 Command Line Tools，其中包含 git。（如果你已经在用 Homebrew，也可以 `brew install git`。）

**Windows**

从 https://git-scm.com 下载 Git for Windows。如果在国内下载速度慢，可以改用 npmmirror 镜像：https://registry.npmmirror.com/binary.html?path=git-for-windows/ —— 选择最新的 `Git-*-64-bit.exe`。安装时使用默认选项即可。

## 将 git 连接到 Gitee

你通过常规的 `git` 命令与 Gitee 交互——Gitee 只是托管仓库的服务器。当你执行 `git clone` / `pull` / `push` 时，git 需要验证你的身份。有两种方式：

**HTTPS + 个人访问令牌（推荐）**

1. 使用仓库的 HTTPS URL 进行克隆，例如 `git clone https://gitee.com/yelab0/yelab-wiki.git`
2. 当 git 要求输入密码时，粘贴**个人访问令牌**，而不是登录密码——在 https://gitee.com/profile/personal_access_tokens 创建（勾选 `projects` 权限即可）
3. 在 macOS 上，钥匙串会记住令牌，因此只需操作一次

**SSH 密钥（可选）**

效果相同，机制不同——无需管理令牌，但配置稍繁琐。除非你更偏好这种方式，否则可以跳过。

```bash
# 生成密钥(如果已有则跳过)
ssh-keygen -t ed25519 -C "your-gitee-email@example.com"

# 打印公钥,并在 https://gitee.com/profile/sshkeys 页面添加
cat ~/.ssh/id_ed25519.pub

# 测试
ssh -T git@gitee.com
```

## 仓库规范

- 命名：`lowercase-with-dashes`（小写字母加连字符），例如 `spike-sorting-pipeline`
- 每个仓库都要有一个 README，内容包括：项目是什么、如何安装、如何运行、由谁维护
- 默认分支：`main`。多人协作的项目请使用功能分支 + pull request
- 大型数据、模型权重和结果**不要**放进 git —— 参见 [computers/storage](../the-lab/computers.md#storage)

## 第三方（上游）仓库

对于我们不拥有、但需要本地访问的仓库：

1. **私有镜像，只读** —— 从 GitHub 导入（`+` → 从 GitHub 导入仓库），或推送一个 `--mirror` 克隆
2. 将其命名为 `mirror-<owner>-<repo>`，并在描述中注明上游 URL 和同步日期
3. 保留 LICENSE 和完整的 git 历史；镜像前先检查许可证
4. **永远不要直接向镜像仓库提交** —— 要修改上游代码，请基于镜像单独创建一个实验室仓库
5. 通过 Gitee 的 pull-mirror 功能（仓库设置 → 仓库镜像管理 → Pull）或定时执行 `git fetch && git push --mirror` 来保持镜像最新

## 向 GitHub 项目回馈贡献

请在 GitHub 上操作（在 GitHub 上 fork + 提 PR）。Gitee 只是我们的本地访问层；从 Gitee 副本向 GitHub 上游提交贡献既不规范也很麻烦。
