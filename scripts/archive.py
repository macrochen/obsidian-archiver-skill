import argparse
import os
import yaml
import re
from datetime import datetime

def strip_existing_frontmatter(content):
    if not content.startswith("---\n"):
        return content
    parts = content.split("---\n", 2)
    if len(parts) < 3:
        return content
    return parts[2].lstrip("\n")

def archive_article(title, type, summary, category, date, tags, content, output_dir, content_file=None, feature_image=None):
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Determine platform suffix for filename
    platform_map = {
        "WeChat": "公众号",
        "Xiaohongshu": "小红书"
    }
    platform_suffix = platform_map.get(type, type)
    
    # If title is just a filename or placeholder, try to extract from content or directory
    if title.endswith(".md") or title in ["01-polished", "02-final", "placeholder"]:
        # Try to find H1 in content
        h1_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
        else:
            # Fallback to directory name
            dir_name = os.path.basename(os.path.dirname(os.path.abspath(content_file))) if content_file else ""
            if dir_name:
                title = dir_name.replace("_", " ").title()
    
    # Sanitize title for filename
    safe_title = title.replace("/", "-").replace(":", "-")
    filename = f"{safe_title}.md"
    file_path = os.path.join(output_dir, filename)

    # Prepare frontmatter
    metadata = {
        "title": title,
        "summary": summary,
        "type": type,
        "category": category,
        "date": date or datetime.now().strftime("%Y-%m-%d"),
        "tags": tags or []
    }
    if feature_image:
        metadata["featureImage"] = feature_image

    # Generate frontmatter string
    frontmatter = "---\n" + yaml.dump(metadata, allow_unicode=True, default_flow_style=False) + "---\n\n"

    # Avoid nested frontmatter when archiving finalized markdown files.
    clean_content = strip_existing_frontmatter(content)

    # Write to file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(frontmatter)
        f.write(clean_content)

    print(f"Successfully archived to: {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Archive an article to Obsidian.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--type", required=True, choices=["WeChat", "Xiaohongshu"])
    parser.add_argument("--summary", default="")
    parser.add_argument("--category", default="未分类")
    parser.add_argument("--date", help="YYYY-MM-DD")
    parser.add_argument("--tags", nargs="*", help="List of tags")
    parser.add_argument("--content_file", help="Path to a file containing the markdown content")
    parser.add_argument("--content", help="Direct markdown content")
    parser.add_argument("--feature_image", help="Feature image filename")
    parser.add_argument("--output_dir", default="/Users/shi/workspace/my-skills/Obsidian-Knowledge-Base")

    args = parser.parse_args()

    if args.content_file:
        with open(args.content_file, "r", encoding="utf-8") as f:
            content = f.read()
    elif args.content:
        content = args.content
    else:
        print("Error: Either --content_file or --content must be provided.")
        exit(1)

    archive_article(
        args.title, args.type, args.summary, args.category, args.date, 
        args.tags, content, args.output_dir, args.content_file, args.feature_image
    )
