---
name: obsidian-archiver-skill
description: Archive articles (WeChat, Xiaohongshu) to Obsidian vault. Use when converting online articles into Obsidian-formatted notes with appropriate frontmatter, tags, and structure.
---

# Obsidian Archiver Skill

This skill automates the process of archiving articles from platforms like WeChat (公众号) and Xiaohongshu (小红书) into a structured Obsidian vault. It leverages the `obsidian-markdown` standards for high-quality note-taking.

## Workflows

### Standard Workflow
1. **Extract/Prepare Content**: Use other tools or manual input to get the article content in Markdown.
2. **Standardize Formatting**: Follow `obsidian-markdown` guidelines (callouts, wikilinks, bold/italics).
3. **Run Archive Script**: Execute the `archive.py` script.

### Deep Archive Workflow (Preferred)
Use this when archiving content from the `content/` project directories:
1. **Locate Source**: Find the article directory in `content/wechat/` or `content/xiaohongshu/`.
2. **Select File**:
    - **Xiaohongshu**: Always prefer `01-polished.md` (ensures depth).
    - **WeChat**: Always prefer `02-final.md` (includes final adjustments).
    - **Manual Override**: Support user-specified files if provided.
3. **Extract Metadata**:
    - **Title**: The script will automatically try to extract the first `# Heading` from the file.
    - **Type**: Based on the parent directory (`wechat` -> `WeChat`, `xiaohongshu` -> `Xiaohongshu`).
4. **Execute**: Run `archive.py` with the selected file.

## Formatting Guidelines (Obsidian Flavored)

- **Frontmatter**: Use the schema defined in `references/obsidian_schema.md`.
- **Callouts**: Use `> [!tip]`, `> [!info]`, etc., for highlights.
- **Wikilinks**: Use `[[Note Name]]` for internal references within the vault.
- **Tags**: Use `#tag` in body or `tags:` in frontmatter.

## Reusable Resources

### Scripts
- `scripts/archive.py`: Handles file creation and frontmatter generation.
  - Parameters: `--title`, `--type`, `--summary`, `--category`, `--date`, `--tags`, `--content_file`, `--feature_image`.

### References
- `references/obsidian_schema.md`: Detailed YAML schema and file naming conventions.

## Example Usage

```bash
python scripts/archive.py \
  --title "My Article Title" \
  --type "Xiaohongshu" \
  --summary "A brief summary" \
  --tags tag1 tag2 \
  --content_file "input.md"
```