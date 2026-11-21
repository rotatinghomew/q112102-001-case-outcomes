# 结案抽查与整改台账：资料契约

台账以 `item` 追踪独立待处置事项。`report` 是来源单号。只有 `active` 认定可令两事项共享抽签对象，`revoke` 以 `target` 指向原认定；同一对象内各事项仍须各自有适用证据。历史名册 `object` 同周期可占多行以列出成员。`basis` 为 `mandatory` 或 `random`；抽签参数中的 `slots` 是必查之外的名额。随档通知记录为原抽查签发事实，不应根据新名册复造。
所有时间为当地时间，观察区间左闭右开。证据 `transfer` 不能终结事项，`performed` 为具体处置事实；`unfulfilled` 由复核人确认原处置未兑现，`recurrence` 指完成后出现新事件，使用独立 `item`。复核 `covered_item` 只表明实际调查了该事项。缺陷率目标是冻结时期的原名册对象；同组随机件的概率是所抽常规件数除以可抽常规件数。对象层质量以至少一项已核实缺陷为缺陷；尚未覆盖且没有已知缺陷为未知，可采用缺失结果界限，并与抽样不确定性分别表明。整改 `resolved` 事件须引用新的核实证据。

## 输入表

- `intake.csv`：`report`、`item`、`household`、`street`、`category`、`at`
- `recognition.csv`：`id`、`left_item`、`right_item`、`action`、`target`、`signed_by`、`at`
- `disposition.csv`：`id`、`item`、`basis`、`prior_item`、`at`
- `roster.csv`：`cycle`、`object`、`item`、`street`、`category`、`basis`、`frozen_at`
- `draw_policy.csv`：`cycle`、`street`、`category`、`slots`、`seed`
- `dispatch.csv`：`cycle`、`object`、`basis`、`sent_at`
- `inspections.csv`：`id`、`cycle`、`object`、`covered_item`、`evidence`、`finding`、`at`
