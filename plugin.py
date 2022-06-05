import sublime
from pathlib import Path

MD_TEMPLATE = """
%YAML 1.2
---
# http://www.sublimetext.com/docs/syntax.html
name: Markdown (Astro)
scope: text.html.markdown.astro
version: 2

extends: {base_syntax}

contexts:
  prototype:
    - meta_prepend: true
    - include: HTML (Astro).sublime-syntax#astro-interpolations

  html-content:
    - include: HTML (Astro).sublime-syntax#html

  fenced-syntaxes:
    - meta_append: true
    - include: fenced-astro

  fenced-astro:
    - match: |-
         (?x)
          {{{{fenced_code_block_start}}}}
          ((?i:astro))
          {{{{fenced_code_block_trailing_infostring_characters}}}}
      captures:
        0: meta.code-fence.definition.begin.markdown-gfm
        2: punctuation.definition.raw.code-fence.begin.markdown
        5: constant.other.language-name.markdown
      embed: scope:text.html.astro
      embed_scope: markup.raw.code-fence.markdown-gfm text.html.astro
      escape: '{{{{fenced_code_block_escape}}}}'
      escape_captures:
        0: meta.code-fence.definition.end.markdown-gfm
        1: punctuation.definition.raw.code-fence.end.markdown
"""


def select_base_syntax():
    # prefer MarkdownEditing if present
    for base_syntax in sublime.find_syntax_by_name("Markdown"):
        if "MarkdownEditing" in base_syntax.path:
            return base_syntax.path
    # fallback to default markdown
    return "Packages/Markdown/Markdown.sublime-syntax"


def create_markdown_syntax():
    """
    Creates an inherit Markdown (astro).sublime-syntax.

    If present MarkdownEditing's Markdown.sublime-syntax is extended.
    Otherwise ST's Markdown package is used.
    """
    syntax_file = (
        Path(sublime.packages_path())
        / __package__
        / "Syntaxes"
        / "Markdown (Astro).sublime-syntax"
    )
    syntax_content = MD_TEMPLATE.lstrip().format(base_syntax=select_base_syntax())

    # check existance and content to avoid touching unchanged files
    try:
        with open(syntax_file) as f:
            if f.read() == syntax_content:
                return
    except FileNotFoundError:
        pass

    # create or update markdown syntax definition
    with open(syntax_file, "w") as f:
        f.write(syntax_content)


def plugin_loaded():
    create_markdown_syntax()
