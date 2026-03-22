# openpencil-design-orchestrator

[English](./README.md) | **简体中文**

一个面向 Pencil / OpenPencil 的 Agent Skill，用来把 AI 辅助设计任务拆成**分阶段、可控、可验证**的 MCP-first 工作流。

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

## 获取方式

### 源码仓库
- GitHub 仓库：
  - <https://github.com/ziiinian/openpencil-design-orchestrator>

### 打包发布
- Release 页面：
  - <https://github.com/ziiinian/openpencil-design-orchestrator/releases>

其中包含：
- `openpencil-design-orchestrator.skill`

## License

本仓库使用 MIT License，详见 [LICENSE](./LICENSE)。
