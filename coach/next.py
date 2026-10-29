#!/usr/bin/env python3
"""
Daily LeetCode coach.

Generates today's 5-problem worksheet:
  * 3 new problems from coach/bank.json (curated, in curriculum order)
  * 2 spaced-repetition reviews from problems.md (the problems you already solved)

Usage:
    python3 coach/next.py                # write coach/daily/<today>.md and update state
    python3 coach/next.py --preview      # print without writing / without touching state
    python3 coach/next.py --date 2026-10-28
    python3 coach/next.py --new 5 --review 0
    python3 coach/next.py --solved 560 239   # append solved problems to problems.md
    python3 coach/next.py --stats
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANK_PATH = ROOT / "coach" / "bank.json"
STATE_PATH = ROOT / "coach" / "state.json"
DAILY_DIR = ROOT / "coach" / "daily"
PROBLEMS_MD = ROOT / "problems.md"

# LeetCode slugs that cannot be derived mechanically from the title.
SLUG_OVERRIDES = {
    "Two Sum II": "two-sum-ii-input-array-is-sorted",
    "3Sum": "3sum",
    "Kth Smallest Element in BST": "kth-smallest-element-in-a-bst",
    "Lowest Common Ancestor of Binary Tree": "lowest-common-ancestor-of-a-binary-tree",
    "Remove Nth Node From End": "remove-nth-node-from-end-of-list",
    "Implement Trie (Prefix Tree)": "implement-trie-prefix-tree",
    "Serialize and Deserialize Binary Tree": "serialize-and-deserialize-binary-tree",
    "Construct Binary Tree from Preorder and Inorder": "construct-binary-tree-from-preorder-and-inorder-traversal",
    "Find Median from Data Stream": "find-median-from-data-stream",
    "Cheapest Flights Within K Stops": "cheapest-flights-within-k-stops",
    "Longest Increasing Path in a Matrix": "longest-increasing-path-in-a-matrix",
}

ENGLISH_FRAMES = [
    "I'd restate the problem in one sentence, sketch a brute force, name its bottleneck, then optimize.",
    "The key observation is ___. Once I see that, the rest is just bookkeeping.",
    "I'll use a ___ to bring the time down from O(n^2) to O(n).",
    "The invariant is ___; it holds before and after every iteration.",
    "Let me trace one small example to make sure the invariant actually holds.",
    "For edge cases I'd check empty input, a single element, and duplicates.",
    "Before coding I'll confirm the constraints, because they tell me which complexity is acceptable.",
    "That's O(n) time and O(1) space, which is optimal since we must read every element.",
]


def slugify(title: str) -> str:
    if title in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[title]
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower())
    return slug.strip("-")


def leetcode_url(title: str) -> str:
    return f"https://leetcode.com/problems/{slugify(title)}/"


def load_bank() -> list[dict]:
    with BANK_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_state() -> dict:
    if STATE_PATH.exists():
        with STATE_PATH.open(encoding="utf-8") as fh:
            return json.load(fh)
    return {"history": []}


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with STATE_PATH.open("w", encoding="utf-8") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def parse_solved() -> list[dict]:
    """Parse the markdown table in problems.md into problem dicts."""
    if not PROBLEMS_MD.exists():
        return []
    solved = []
    pattern = re.compile(r"^\|\s*(\d+)\s*\|\s*(\d+)\s*\|(.+?)\|\s*(\w+)\s*\|(.+?)\|")
    for line in PROBLEMS_MD.read_text(encoding="utf-8").splitlines():
        m = pattern.match(line.strip())
        if not m:
            continue
        solved.append(
            {
                "idx": int(m.group(1)),
                "lc": int(m.group(2)),
                "title": m.group(3).strip(),
                "diff": m.group(4).strip(),
                "pattern": m.group(5).strip(),
            }
        )
    return solved


def _pattern_tokens(pattern: str) -> set[str]:
    # "Prefix Sum + HashMap" -> {prefix, sum, hash, map}
    spaced = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", pattern)
    return {t for t in re.split(r"[^a-z0-9]+", spaced.lower()) if t}


def _affinity(a: str, b: str) -> int:
    return len(_pattern_tokens(a) & _pattern_tokens(b))


def pick(date_str: str, n_new: int, n_review: int, state: dict) -> tuple[list[dict], list[dict]]:
    bank = load_bank()
    solved = parse_solved()
    solved_lc = {p["lc"] for p in solved}
    history = state["history"]

    delivered_new = {lc for day in history for lc in day["new"]}
    last_reviewed: dict[int, str] = {}
    for day in history:
        for lc in day["review"]:
            last_reviewed[lc] = day["date"]

    fresh = [p for p in bank if p["lc"] not in delivered_new and p["lc"] not in solved_lc]
    new_picks = fresh[:n_new]

    # Review: prefer problems sharing a pattern with today's new material,
    # then the ones reviewed longest ago (never-reviewed first).
    new_patterns = " ".join(p["pattern"] for p in new_picks)
    candidates = [p for p in solved if p["lc"] not in {q["lc"] for q in new_picks}]
    candidates.sort(
        key=lambda p: (
            -_affinity(p["pattern"], new_patterns),
            last_reviewed.get(p["lc"], "0000-00-00"),
            p["lc"],
        )
    )
    by_lc = {p["lc"]: p for p in bank}
    pinned = [by_lc[lc] for lc in state.get("focus", []) if lc in by_lc]
    already = {p["lc"] for p in new_picks} | {p["lc"] for p in pinned}
    review_picks = (pinned + [p for p in candidates if p["lc"] not in already])[:n_review]
    return new_picks, review_picks


def render(
    day_no: int,
    date_str: str,
    new: list[dict],
    review: list[dict],
    bank_left: int,
    prev: dict | None = None,
    titles: dict[int, str] | None = None,
) -> str:
    d = datetime.strptime(date_str, "%Y-%m-%d")
    lines: list[str] = []
    add = lines.append

    total = len(new) + len(review)
    add(f"# Day {day_no} · {date_str} ({d.strftime('%A')})")
    add("")
    add(f"**今日 {total} 题** — {len(new)} 道新题 + {len(review)} 道间隔复习 · 建议 75–90 分钟")
    add("")
    add("> 每题的流程：**先自己用中文讲思路 → 再用英文讲 40 秒 → 最后写代码**。")
    add("> 讲不出来再看答案，看完立刻合上重讲一遍。")
    add("")

    if prev and prev.get("new"):
        titles = titles or {}
        add("## ⏪ 昨日回顾（90 秒）")
        add("")
        add("> 先别翻昨天的讲义。看标题说出 **pattern / 一句话思路 / 复杂度**，说完再对答案。")
        add("")
        for lc in prev["new"]:
            add(f"- LC {lc} · {titles.get(lc, f'LC {lc}')}")
        add("")
        add(f"答案在 `coach/daily/{prev['date']}.md`。")
        add("")

    if new:
        add("## 🆕 新题")
        add("")
        for i, p in enumerate(new, 1):
            add(f"### {i}. {p['title']} · LC {p['lc']} · {p['diff']}")
            add(f"`{p['pattern']}`  ·  <{leetcode_url(p['title'])}>")
            add("")
            add(f"**中文切入**：{p['cn']}")
            add("")
            add(f"**面试英文（照这个说）**：{p['en']}")
            add("")
            add(f"**复杂度**：{p['cx']}")
            add("")
            add(f"**⚠️ 易错**：{p['trap']}")
            add("")

    if review:
        add("## 🔁 间隔复习")
        add("")
        add("> 不给答案。先花 30 秒回忆：**pattern / 一句话思路 / 复杂度 / 一个边界**，说不出来再回去看自己的代码。")
        add("")
        for i, p in enumerate(review, len(new) + 1):
            add(f"### {i}. {p['title']} · LC {p['lc']} · {p['diff']}")
            add(f"`{p['pattern']}`  ·  <{leetcode_url(p['title'])}>")
            add("")
            add("- 30 秒自测：思路是什么？为什么成立？")
            add("- 英文 30 秒：*\"I solved this with ___. The key idea is ___, which gives ___ time.\"*")
            add("- 还能不能优化？换个输入规模会怎样？")
            add("")

    frames = [ENGLISH_FRAMES[(day_no - 1) % len(ENGLISH_FRAMES)],
              ENGLISH_FRAMES[(day_no + 2) % len(ENGLISH_FRAMES)]]
    add("## 🎯 今日英语句式")
    add("")
    for f in frames:
        add(f"- {f}")
    add("")
    add("## ✅ 收尾（2 分钟）")
    add("")
    add("- [ ] 今天最不熟的 pattern 是哪一个？写进一句话笔记。")
    add("- [ ] 把上面两个句式各用一次，录一段 60 秒的英文自述。")
    add(f"- [ ] 做完了就标记：`python3 coach/next.py --solved {' '.join(str(p['lc']) for p in new)}`")
    add("")
    if bank_left < 12:
        add(f"> ⚠️ 题库只剩 **{bank_left}** 道新题，记得补充 `coach/bank.json`。")
        add("")
    add(f"_题库剩余 {bank_left} 道 · 复习池 {len(parse_solved())} 道_")
    add("")
    return "\n".join(lines)


def mark_solved(lcs: list[int]) -> None:
    bank = {p["lc"]: p for p in load_bank()}
    solved = parse_solved()
    known = {p["lc"] for p in solved}
    todo = [lc for lc in lcs if lc not in known]
    if not todo:
        print("全部已在 problems.md 中，无需添加。")
        return
    text = PROBLEMS_MD.read_text(encoding="utf-8").rstrip("\n")
    rows = []
    idx = max((p["idx"] for p in solved), default=0)
    for lc in todo:
        idx += 1
        p = bank.get(lc)
        if p is None:
            title, diff, pattern = f"LC {lc}", "Medium", "TODO"
        else:
            title, diff, pattern = p["title"], p["diff"], p["pattern"]
        rows.append(f"| {idx:>2} | {lc:<3} | {title:<46} | {diff:<10} | {pattern:<24} |")
    PROBLEMS_MD.write_text(text + "\n" + "\n".join(rows) + "\n", encoding="utf-8")
    print(f"已追加 {len(rows)} 题到 problems.md：{', '.join(map(str, todo))}")


def print_stats() -> None:
    bank = load_bank()
    solved = parse_solved()
    state = load_state()
    history = state["history"]
    delivered = {lc for day in history for lc in day["new"]}
    reviewed = {lc for day in history for lc in day["review"]}
    print(f"天数        : {len(history)}")
    print(f"题库        : {len(bank)} 道（已出 {len(delivered)}，剩 {len(bank) - len(delivered)}）")
    print(f"已解题池    : {len(solved)} 道（复习过 {len(reviewed)}，未复习 {len(solved) - len(reviewed)}）")
    if history:
        print(f"最近一次    : {history[-1]['date']}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Daily LeetCode coach")
    ap.add_argument("--date", default=date.today().isoformat())
    ap.add_argument("--new", type=int, default=None)
    ap.add_argument("--review", type=int, default=None)
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--solved", nargs="+", type=int, metavar="LC")
    ap.add_argument("--focus", nargs="+", type=int, metavar="LC",
                    help="pin problems to the next review session")
    ap.add_argument("--stats", action="store_true")
    args = ap.parse_args()

    if args.stats:
        print_stats()
        return 0

    if args.solved:
        mark_solved(args.solved)
        return 0

    state = load_state()

    if args.focus:
        known = {p["lc"] for p in load_bank()} | {p["lc"] for p in parse_solved()}
        unknown = [lc for lc in args.focus if lc not in known]
        if unknown:
            print(f"⚠️ 题库里没有这些题号：{unknown}", file=sys.stderr)
        pins = state.get("focus", [])
        state["focus"] = pins + [lc for lc in args.focus if lc in known and lc not in pins]
        save_state(state)
        print(f"已加入下次复习：{state['focus']}")
        return 0
    history = state["history"]

    if args.date in {day["date"] for day in history} and not args.preview:
        print(f"{args.date} 已经生成过了。用 --preview 看内容，或换一个 --date。")
        return 0

    n_new = args.new if args.new is not None else (5 if not history else 3)
    n_review = args.review if args.review is not None else (0 if not history else 2)

    new, review = pick(args.date, n_new, n_review, state)
    if not new and not review:
        print("题库和复习池都空了，先补充 coach/bank.json。")
        return 1
    if len(new) < n_new:
        print(f"⚠️ 题库不足：只选到 {len(new)} 道新题（目标 {n_new}）。", file=sys.stderr)

    bank_left = len(load_bank()) - len({lc for day in history for lc in day["new"]} | {p["lc"] for p in new})
    titles = {p["lc"]: p["title"] for p in load_bank()}
    titles.update({p["lc"]: p["title"] for p in parse_solved()})
    prev = history[-1] if history else None
    md = render(len(history) + 1, args.date, new, review, bank_left, prev, titles)

    if args.preview:
        print(md)
        return 0

    DAILY_DIR.mkdir(parents=True, exist_ok=True)
    out = DAILY_DIR / f"{args.date}.md"
    out.write_text(md, encoding="utf-8")

    state["history"].append(
        {"date": args.date, "new": [p["lc"] for p in new], "review": [p["lc"] for p in review]}
    )
    delivered = {p["lc"] for p in review} | {p["lc"] for p in new}
    state["focus"] = [lc for lc in state.get("focus", []) if lc not in delivered]
    save_state(state)
    print(f"已生成 {out.relative_to(ROOT)}")
    print(f"新题: {', '.join(p['title'] for p in new) or '—'}")
    print(f"复习: {', '.join(p['title'] for p in review) or '—'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
