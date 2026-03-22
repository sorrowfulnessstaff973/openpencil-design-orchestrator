# 排障说明

## 适用范围

本页用于诊断 `openpencil-design-orchestrator` 的常见失败模式。

它不是通用 MCP 故障手册，而是专门处理那些会破坏本 skill「分阶段、边界清晰、小步推进」工作方式的问题。

## 快速分型

如果结果不对，先判断故障属于哪一类：

1. **环境故障**
   - Pencil / OpenPencil 没开
   - MCP 不可用或不稳定
   - transport 模式判断错了

2. **流程故障**
   - 跳过 planning
   - 一上来直接大改
   - 改前没有重新读取结构

3. **范围故障**
   - 任务范围过大
   - 跨多个 section 无控制地修改
   - 输出漂移到批准范围之外

4. **降级故障**
   - MCP 不可用，但流程还装作 live edit 正常
   - 实际应切 fallback，却没有明确声明

## 常见症状与可能原因

### 症状：一上来就整页重做
可能原因：
- 你的请求本身像“自由生成整稿”
- 跳过了 skeleton 阶段
- 没先限定 section / page 范围

优先检查：
1. 你的提示词是不是在要求整页重构？
2. 任务有没有收敛到一个页面或一个 section？
3. 是否先做了 planning？

### 症状：明明只想改一个 section，却改了很多地方
可能原因：
- 范围描述不够清楚
- 改之前没再次确认 section 边界
- refinement 漂移成了重构

优先检查：
1. 你有没有明确说“只改这一块”？
2. section 有没有被清楚命名？
3. 流程有没有在继续前说明 touched nodes？

### 症状：它表现得像 MCP 可用，但实际上没连上
可能原因：
- 跳过 preflight
- 把环境可用性当成默认成立
- 其实应该走 fallback，但没有承认

优先检查：
1. 先跑 `scripts/preflight-check.sh`
2. 确认 Pencil/OpenPencil 是否真的在运行
3. 判断当前是否应该改为 fallback 模式

### 症状：输出很漂亮，但不是可执行的编排方案
可能原因：
- 提示词偏向创意生成，而不是 orchestration
- planning 输出格式没被约束
- 被当成普通设计脑暴来处理了

优先检查：
1. 是否明确要求 plan / skeleton / section / refine？
2. 输出里有没有写当前 mode 和 phase？
3. 在提修改前有没有明确 scope？

### 症状：refinement 阶段改了信息架构
可能原因：
- refinement 启动得太早
- skeleton 没被当成已批准基线
- 视觉精修和结构重排混在一起

优先检查：
1. skeleton 是否已经被确认？
2. 当前 refinement 改的是视觉细节，还是结构本身？
3. 这件事是不是应该退回 planning？

## 最小恢复顺序

当结果开始漂移时，按这个顺序收束：

1. 停止扩大修改范围
2. 重述当前 mode：MCP-first / fallback
3. 重述当前 phase
4. 把范围缩回一个页面或一个 section
5. 重新读取当前结构
6. 只继续下一步边界清晰的动作

## 什么时候切 fallback 模式

满足以下任一情况时，就该切 fallback：
- MCP 不通
- Pencil/OpenPencil 不可用
- 环境无法确认 live-edit readiness
- 虽然不能实时改稿，但仍可继续做 planning / structure / audit

## 什么时候应该停下，而不是硬接着改

出现以下情况时，应停止并汇报，而不是继续脑补：
- 当前结构未知
- 目标 section 无法可靠定位
- 新请求与已批准结构冲突
- 名义上是“小修”，实际上会变成结构重写

## 相关文件

- `INSTALL.zh-CN.md`
- `../references/risk-matrix.md`
- `../references/fallback-mode.md`
- `../references/workflow-sequence.md`
