from bs4 import BeautifulSoup
from typing import Optional


# tweak these defaults to change behavior/site styling
IMG_CLASSES = ("rounded-lg", "max-w-full", "h-auto", "block", "mx-auto")
FIGURE_CLASS = "article-figure m-6"
FIGCAP_CLASS = "article-caption mt-1 text-sm text-center underline decoration-persian-red"

def _is_single_child(parent, child) -> bool:
    """Return True if parent only contains that child node (ignoring whitespace)."""
    # BeautifulSoup may include strings for whitespace; check direct children
    direct = [n for n in parent.contents if not (n.string and not n.string.strip())]
    return len(direct) == 1 and direct[0] is child


def wrap_images(html: Optional[str]) -> str:
    """
    Wrap <img> tags in <figure> and add <figcaption> from alt text.
    - Preserves links (<a>) and <picture> parents (wraps the parent instead of breaking the link)
    - Adds utility classes to <img> while preserving existing classes
    - Skips images already in <figure>
    """
    if not html:
        return html or ""

    soup = BeautifulSoup(html, "html.parser")

    for img in soup.find_all("img"):
        # Skip if already in a <figure>
        if img.find_parent("figure"):
            continue

        # Add Tailwind utility classes (without overwriting existing classes)
        classes = list(img.get("class") or [])
        for c in IMG_CLASSES:
            if c not in classes:
                classes.append(c)
        img['class'] = classes

        # Get caption text from alt (trim whitespace)
        alt = (img.get("alt") or "").strip()

        # If img is the only child of an <a> or <picture>, wrap that parent to preserve semantics
        parent = img.parent
        parent_name = getattr(parent, "name", None)

        # Decide what to wrap: prefer wrapping <a> or <picture> if they're the direct single parent
        to_wrap = None
        if parent_name in ("a", "picture") and _is_single_child(parent, img):
            to_wrap = parent
        else:
            to_wrap = img

        # Build the <figure> and move the node(s) inside it
        figure = soup.new_tag("figure", **{"class": FIGURE_CLASS})
        to_wrap.replace_with(figure)
        # If we wrapped the parent, append that parent (anchor or picture); else append the img
        figure.append(to_wrap if to_wrap is parent else img)

        # Append figcaption only if alt is not empty
        if alt:
            figcap = soup.new_tag("figcaption", **{"class": FIGCAP_CLASS})
            figcap.string = alt  # BeautifulSoup will escape as needed
            figure.append(figcap)

    return str(soup)