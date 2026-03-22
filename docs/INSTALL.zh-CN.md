# 安装说明

## 适用范围

本说明用于安装并验证 `openpencil-design-orchestrator` 这个 skill 仓库产物。

它**不是**通用 MCP 安装说明，也**不**声称自动支持所有客户端或环境。  
请只按本仓库已经明确说明过的工作流使用。

## 安装前先确认

在安装前，请先确认：

- 你已经有可用的 OpenClaw / skill 环境
- 该环境支持导入或放置 `.skill` 文件
- 如果你的任务依赖实时 MCP 编辑，那么 Pencil / OpenPencil 与 MCP 接入应当先单独处理好

这个仓库解决的是：  
**设计任务如何被分阶段编排**  
而不是：  
**所有 MCP 如何一键装好**

## 方式 1：从 `.skill` 安装包安装

1. 从最新 Release 下载 `.skill`
2. 将该 `.skill` 导入或放入你的目标 skill 环境
3. 如果你的环境需要，重启或重新加载

## 方式 2：直接使用源码

1. 克隆本仓库
2. 将 skill 源码复制到本地 skill 目录
3. 将本仓库保留为后续维护与迭代的 source-of-truth

## 最小验证方式

第一次不要拿整稿大任务做验证。  
请先用一个**小范围、可控**的任务验证。

推荐验证说法：

- “先规划页面结构，再只搭 skeleton。”
- “只重做 Hero 区，不要动其他部分。”
- “先审查 spacing、层级和 token 一致性，再决定是否编辑。”

成功的最小验证，应该体现出：

- 分阶段工作流
- 改动范围受控
- 不会直接整页乱改
- 改前先读结构
- MCP 不可用时会明确 fallback，而不是硬装成功

## 什么算成功

如果工作正常，你应该看到它倾向于：

1. 改之前先做 preflight
2. 先规划，再动结构
3. 一次只改一个 section
4. 结构稳定后再 refinement
5. MCP 不可用时明确降级

## 什么算失败信号

如果出现下面这些情况，说明当前使用方式不对：

- 一上来就整页重做
- 没读当前结构就直接改
- 一次跨多个 section 大改
- 没检查 MCP 就默认能 live edit
- fallback 模式下却假装自己在实时编辑

## 出问题先查什么

按这个顺序排查：

1. 你装的是不是正确版本的 `.skill`
2. 你调用的是“分阶段设计编排”，还是其实在要求“自由生成整稿”
3. MCP 当前到底可不可用
4. 你的任务范围有没有明确限定到一个页面或一个 section
5. 你要的是 orchestration，还是在误把它当成一键生成器

## 相关文件

- `../SKILL.md`
- `../references/prompt-framework.md`
- `../references/workflow-sequence.md`
- `../references/fallback-mode.md`
- `../references/risk-matrix.md`
