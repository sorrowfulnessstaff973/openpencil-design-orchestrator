# openpencil-design-orchestrator

[English](./README.md) | **简体中文**

[![Release](https://img.shields.io/github/v/release/ziiinian/openpencil-design-orchestrator?display_name=tag)](https://github.com/ziiinian/openpencil-design-orchestrator/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Repo](https://img.shields.io/badge/OpenClaw-Agent%20Skill-blue)](https://github.com/ziiinian/openpencil-design-orchestrator)

一个面向 Pencil / OpenPencil 的 Agent Skill，用来把 AI 辅助设计任务拆成**分阶段、可控、可验证**的 MCP-first 工作流。

## 快速开始

### 方式 1：直接下载打包好的 skill
前往 Release 页面下载：

- [`openpencil-design-orchestrator.skill`](https://github.com/ziiinian/openpencil-design-orchestrator/releases/latest)

### 方式 2：直接查看源码
你也可以直接阅读仓库里的 skill 源码：

- `SKILL.md`
- `references/`
- `scripts/`

## 安装 / 使用方式

这个仓库同时提供：

- **skill 源码**
- **打包好的 `.skill` 发布产物**

推荐使用流程：

1. 从最新 Release 下载 `.skill`
2. 导入 / 安装到你的 skill 环境
3. 在需要 Pencil / OpenPencil 分阶段设计编排时调用它

典型触发说法：

- “用 Pencil/OpenPencil 重做这个 Hero 区，但要分 section 安全推进。”
- “先审查这个设计稿的 spacing、字体层级、token 一致性，再决定是否修改。”
- “先做页面结构规划，再只搭 skeleton。”

## 安装与验证

安装与首次验证请直接看：

- [中文安装说明](./docs/INSTALL.zh-CN.md)
- [English Installation Guide](./docs/INSTALL.md)

## 这个 skill 是做什么的

`openpencil-design-orchestrator` 的核心目标，不是让 AI 一次性“整稿乱冲”，而是把设计任务拆成稳定流程：

1. **Preflight（预检）** – 检查 Pencil / OpenPencil、MCP 连接和当前结构
2. **Planning（规划）** – 将任务拆成页面、区块、组件、token 和执行顺序
3. **Skeleton（骨架）** – 先搭结构，不急着精修
4. **Section Content（分区填充）** – 一次只改一个 section
5. **Refinement（精修）** – 统一间距、层级、一致性和视觉细节
6. **Save / Handoff（保存 / 交付）** – 总结变更与遗留问题

它强调的是：
- 优先 MCP
- 小步修改
- 先读后写
- 限定改动范围
- MCP 不可用时要安全降级

## 适用场景

适合在这些情况下使用：

- 通过 MCP 与 Pencil / OpenPencil 协作
- 做 AI 辅助设计改稿
- 对已有设计稿做局部、安全的 section 级修改
- 做设计一致性检查（spacing / typography / token / 结构）
- 在 Claude Code、Codex、Cursor、Windsurf 等客户端之间统一工作流

## 不适合的场景

这个 skill 不适合作为主路径来做：

- 不受约束的一次性整产品生成
- 在未知结构下盲改整个设计稿
- 高风险、无审查的大范围破坏性修改
- 在 MCP 不可用时假装自己还在实时编辑
- 默认放开高风险 `eval` 自动化

## 仓库结构

```text
.
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── references/
├── scripts/
├── dist/
│   └── openpencil-design-orchestrator.skill
├── source/
│   └── NOTICE.txt
└── LICENSE
```

## 关键文件说明

- `SKILL.md`
  - skill 触发说明、工作流规则、约束条件
- `references/`
  - 提示词框架、工作流顺序、fallback 模式、风险矩阵、客户端适配说明
- `scripts/preflight-check.sh`
  - 预检 MCP 与环境状态
- `scripts/scaffold-phase-prompt.py`
  - 生成分阶段提示词骨架
- `dist/openpencil-design-orchestrator.skill`
  - 可直接分发/安装的打包产物

## 典型用法

### 1. 新建页面
例如：
- “帮我做一个 SaaS 首页，先只搭 skeleton。”

### 2. 局部改稿
例如：
- “只改 Hero 区，不要动其他 section。”

### 3. 审查设计稿
例如：
- “先检查 spacing、层级、token 一致性，再决定要不要改。”

## Roadmap

后续还可以继续增强：

- 增加更多设计场景示例提示词
- 补更多客户端适配说明
- 扩展 fallback 工作流示例
- 为后续版本增加更细的 release note

## 发布

- 最新发布：<https://github.com/ziiinian/openpencil-design-orchestrator/releases/latest>
- 首个公开版本：<https://github.com/ziiinian/openpencil-design-orchestrator/releases/tag/v1.0.0>

## License

本仓库使用 MIT License，详见 [LICENSE](./LICENSE)。
