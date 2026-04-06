# obsidian-archiver-skill

把公众号或小红书内容归档到 Obsidian 知识库。

## Installation

This skill is intended to run in the local Codex/Gemini skill workspace.

If you are working in this repository, use the skill directly from:

```bash
~/.agents/skills/obsidian-archiver-skill
```

## Documentation

# Obsidian Archiver Skill

## Codex Compatibility
- 适合作为流水线的可选收尾步骤，不应默认自动执行。
- 小红书默认归档 `01-polished.md`，微信默认归档 `02-final.md`。
- 默认优先使用项目约定的 `.venv` 运行归档脚本。
- 如需同步到 GitHub，可在归档时启用 `--sync-github`。

## Command

```bash
./.venv/bin/python ~/.agents/skills/obsidian-archiver-skill/scripts/archive.py \
  --title "My Article Title" \
  --type "Xiaohongshu" \
  --summary "A brief summary" \
  --category "Category Name" \
  --tags tag1 tag2 \
  --content_file "input.md" \
  --sync-github
```
