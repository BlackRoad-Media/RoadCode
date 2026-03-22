"""Blog engine — markdown to HTML with BlackRoad branding."""
from dataclasses import dataclass, field
from pathlib import Path
import time

@dataclass
class BlogPost:
    slug: str
    title: str
    content: str
    author: str = "Alexa Amundson"
    published_at: float = field(default_factory=time.time)
    tags: list[str] = field(default_factory=list)

    def to_html(self) -> str:
        return f"""<!DOCTYPE html>
<html><head><title>{self.title} — BlackRoad</title></head>
<body style="background:#0a0a0a;color:#f5f5f5;font-family:Inter,sans-serif;max-width:800px;margin:0 auto;padding:40px">
<h1>{self.title}</h1>
<p style="color:#999">By {self.author} | {", ".join(self.tags)}</p>
<article>{self.content}</article>
<footer style="color:#666;margin-top:60px">&copy; 2025 BlackRoad OS, Inc.</footer>
</body></html>"""

class BlogEngine:
    def __init__(self):
        self.posts: list[BlogPost] = []

    def publish(self, post: BlogPost) -> str:
        self.posts.append(post)
        return post.slug
