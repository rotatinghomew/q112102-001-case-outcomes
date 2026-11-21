# 数据说明

民生诉求办理、回访与复开情况的分析资料。

下列文件仅包含合成记录。空值按 CSV 空单元格保存；时间字段使用当地业务记录时间，不预设统计结论。

## `requests.csv`

字段：`request_id`、`resident_ref`、`grid_ref`、`topic`、`created_at`、`status`。当前演练样本 4 条。

## `actions.csv`

字段：`action_id`、`request_id`、`kind`、`owner_ref`、`occurred_at`、`note`。当前演练样本 4 条。

## `feedback.csv`

字段：`feedback_id`、`request_id`、`submitted_at`、`result`、`supersedes`。当前演练样本 3 条。
