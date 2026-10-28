# Daily LeetCode Coach

每天 5 道题：**3 道新题 + 2 道间隔复习**。每道题都带中文切入点、面试英文口述稿、复杂度和易错点。

## 每天怎么用

```bash
python3 coach/next.py            # 生成今天的讲义 coach/daily/YYYY-MM-DD.md
python3 coach/next.py --stats    # 看进度：出过几题、复习池还有多少
```

讲义里的顺序是刻意设计的：

1. **先看题面，自己用中文讲思路**（不写代码）
2. **看「面试英文」那段，跟读一遍**
3. **合上讲义，用英文重讲 40 秒**
4. 写代码 → 对复杂度 → 看易错点

复习题不给答案，只给自测提示，逼你从记忆里取。

## 目录

| 文件 | 作用 |
| --- | --- |
| `bank.json` | 题库，55 道未做的题，按学习顺序排列 |
| `state.json` | 出题历史（自动维护，决定「没出过的题」和「最久没复习的题」） |
| `daily/` | 每天生成的讲义 |
| `next.py` | 选题 + 渲染 + 标记已解决 |

## 选题逻辑

- **新题**：按 `bank.json` 顺序取，跳过已出过的、以及 `problems.md` 里已标记完成的。做过的题不会重复出。
- **复习**：从 `problems.md` 的已解列表里选，优先选与今天新题 pattern 相同的（趁热打铁），其次选最久没复习的。每个 pattern 隔几天会再出现一次，对应遗忘曲线的 D+3 / D+7。
- 做完新题后标记，下次复习池就会带上它：

```bash
python3 coach/next.py --solved 560 239
```

## 扩充题库

`bank.json` 是一个数组，加一条就多一道题：

```json
{
  "lc": 33,
  "title": "Search in Rotated Sorted Array",
  "diff": "Medium",
  "pattern": "Binary Search",
  "cn": "中文：关键观察 + 具体怎么做的",
  "en": "English: how you would say it out loud in an interview, first person.",
  "cx": "O(log n) time / O(1) space",
  "trap": "最容易写错的那一处"
}
```

`en` 要写成口语，不是题解。面试官要听的是「我怎么想」，不是「这题的标准答案」。

## 其它参数

```bash
python3 coach/next.py --date 2026-10-28          # 指定日期
python3 coach/next.py --new 5 --review 0         # 调整每天配比
python3 coach/next.py --preview                  # 只看不写、不动 state
```

题库少于 12 道时，讲义末尾会提示补充。
