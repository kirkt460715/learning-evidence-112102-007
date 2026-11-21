# 记录格式

论证记录以 id、round、claim、evidence、counterclaim、response、position 描述轮次、主张、证据、反方及回应。

记录以 UTF-8 JSON 保存，顶层包含 dataset 和 records。每条记录的 id 在文件中唯一。`fixtures/records.json` 中的例子用于说明输入字段和状态取值。
