import re
from pathlib import Path

def convert_relative_links(markdown: str, github_base_url: str) -> str:
    def replacer(match):
        label = match.group(1)
        url = match.group(2)
        if not url.startswith(("http://", "https://", "#")):
            return f"[{label}]({github_base_url}{url})"
        return match.group(0)

    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replacer, markdown)

def embed_readme_in_setup(setup_content: str, github_base_url: str) -> str:
    readme_path = Path("README.md")

    if not readme_path.exists():
        print("README.md not found.")
        return setup_content  # No-op fallback

    readme_content = readme_path.read_text(encoding="utf-8")
    readme_content = convert_relative_links(readme_content, github_base_url)

    updated_content = re.sub(
        r'long_description="""\s*.*?\s*"""',
        f'long_description="""{readme_content}"""',
        setup_content,
        flags=re.DOTALL
    )
    return updated_content

def update_setup():
    path = Path("setup.py")
    if not path.exists():
        print("setup.py not found.")
        return

    content = path.read_text(encoding="utf-8")

    # Extract VERSION from setup.py content
    match = re.search(r'VERSION\s*=\s*["\']([^"\']+)["\']', content)
    version = match.group(1) if match else "main"
    github_base_url = f"https://github.com/curvegrid/multibaas-sdk-python/blob/v{version}/"

    content = re.sub(
        r'\sdescription=\s*["\'].*?["\']',
        ' description="Python SDK for MultiBaas"',
        content
    )
    content = re.sub(
        r'keywords\s*=\s*\[[^\]]*\]',
        'keywords = ["multibaas", "blockchain", "ethereum", "curvegrid"]',
        content
    )

    content = embed_readme_in_setup(content, github_base_url)

    path.write_text(content, encoding="utf-8")
    print(f"✅ Updated setup.py metadata")

if __name__ == "__main__":
    update_setup()
