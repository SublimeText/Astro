| SYNTAX TEST "Markdown (Astro).sublime-syntax"

# About the Author
| <- markup.heading.1.markdown punctuation.definition.heading.begin.markdown
|^^^^^^^^^^^^^^^^^^ markup.heading.1.markdown

The {frontmatter.author} is {frontmatter.age} and lives in Toronto, Canada.
|   ^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.interpolation.astro
|   ^ punctuation.section.interpolation.begin.astro - source.tsx
|    ^^^^^^^^^^^^^^^^^^ source.tsx.embedded.astro
|                      ^ punctuation.section.interpolation.end.astro - source.tsx
|                           ^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.interpolation.astro
|                           ^ punctuation.section.interpolation.begin.astro - source.tsx
|                            ^^^^^^^^^^^^^^^ source.tsx.embedded.astro
|                                           ^ punctuation.section.interpolation.end.astro - source.tsx

# Import Components

<Author name={frontmatter.author}/>
| <- meta.disable-markdown meta.tag.component.begin.astro punctuation.definition.tag.begin.astro
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown meta.tag.component.begin.astro
|^^^^^^ entity.name.tag.component.astro support.class.component.astro
|       ^^^^^^^^^^^^^^^^^^^^^^^^^ meta.attribute-with-value.html
|       ^^^^ entity.other.attribute-name.html
|           ^ punctuation.separator.key-value.html
|            ^^^^^^^^^^^^^^^^^^^^ meta.string.html meta.interpolation.astro
|                                  ^ meta.disable-markdown - meta.tag
|            ^ punctuation.section.interpolation.begin.astro
|             ^^^^^^^^^^^ source.tsx.embedded.astro variable.other.readwrite.js
|                        ^ source.tsx.embedded.astro punctuation.accessor.js
|                         ^^^^^^ source.tsx.embedded.astro meta.property.object.js
|                               ^ punctuation.section.interpolation.end.astro
|                                ^^ punctuation.definition.tag.end.astro

<Biography client:visible>
| <- meta.disable-markdown meta.tag.component.begin.astro punctuation.definition.tag.begin.astro
|^^^^^^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown meta.tag.component.begin.astro
|                         ^ meta.disable-markdown - meta.tag
|^^^^^^^^^ entity.name.tag.component.astro support.class.component.astro
|          ^^^^^^^^^^^^^^ meta.attribute-with-value.astro
|          ^^^^^^ keyword.control.directive.astro
|                ^ punctuation.separator.key-value.astro
|                 ^^^^^^^ variable.parameter.astro
|                        ^ punctuation.definition.tag.end.astro
  {frontmatter.author} lives in Toronto, Canada and enjoys photography.
| ^^^^^^^^^^^^^^^^^^^^ meta.disable-markdown meta.interpolation.astro
</Biography>
| <- meta.disable-markdown meta.tag.component.end.astro punctuation.definition.tag.begin.astro
|^^^^^^^^^^^ meta.disable-markdown meta.tag.component.end.astro
|^ punctuation.definition.tag.begin.astro
| ^^^^^^^^^ entity.name.tag.component.astro support.class.component.astro
|          ^ punctuation.definition.tag.end.astro

<namespace.Component attr:value is:raw attr:value>
| <- meta.paragraph.markdown meta.tag.component.begin.astro punctuation.definition.tag.begin.astro
|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.tag.component.begin.astro
|^^^^^^^^^^^^^^^^^^^ entity.name.tag.component.astro
|^^^^^^^^^ support.namespace.astro
|         ^ punctuation.accessor.dot.astro
|          ^^^^^^^^^ support.class.component.astro
|                    ^^^^^^^^^^ meta.attribute-with-value.astro
|                               ^^^^^^ meta.attribute-with-value.astro
|                                      ^^^^^^^^^^ meta.attribute-with-value.astro

  <p>Text</p>
| ^^^^^^^^^^^^ meta.paragraph.markdown - meta.tag

</namespace.Component>
| <- meta.paragraph.markdown meta.tag.component.end.astro punctuation.definition.tag.begin.astro
|^^^^^^^^^^^^^^^^^^^^^ meta.paragraph.markdown meta.tag.component.end.astro
|^ punctuation.definition.tag.begin.astro
| ^^^^^^^^^^^^^^^^^^^ entity.name.tag.component.astro
| ^^^^^^^^^ support.namespace.astro
|          ^ punctuation.accessor.dot.astro
|           ^^^^^^^^^ support.class.component.astro
|                    ^ punctuation.definition.tag.end.astro

<Header />
| <- meta.disable-markdown meta.tag.component.begin.astro punctuation.definition.tag.begin.astro
|^^^^^^^^^ meta.disable-markdown meta.tag.component.begin.astro
|^^^^^^ entity.name.tag.component.astro support.class.component.astro
|       ^^ punctuation.definition.tag.end.astro


# Fenced Astro Code Blocks

```astro
---
| <- markup.raw.code-fence.markdown-gfm text.html.astro meta.frontmatter.astro punctuation.section.block.begin.frontmatter.astro
|^^^ markup.raw.code-fence.markdown-gfm text.html.astro meta.frontmatter.astro
|^^ punctuation.section.block.begin.frontmatter.astro

| <- markup.raw.code-fence.markdown-gfm text.html.astro meta.frontmatter.astro source.ts.embedded.astro
---
| <- markup.raw.code-fence.markdown-gfm text.html.astro meta.frontmatter.astro punctuation.section.block.end.frontmatter.astro
|^^^ markup.raw.code-fence.markdown-gfm text.html.astro meta.frontmatter.astro
|^^ punctuation.section.block.end.frontmatter.astro

<ul>
  {posts.map(post => <li>{post.frontmatter.title}</li>)}
| ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ markup.raw.code-fence.markdown-gfm text.html.astro meta.interpolation.astro
| ^ punctuation.section.interpolation.begin.astro
|  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ source.tsx.embedded.astro meta.function-call.method.js
|                                                      ^ punctuation.section.interpolation.end.astro
</ul>
```
| <- meta.code-fence.definition.end.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|^^ meta.code-fence.definition.end.markdown-gfm punctuation.definition.raw.code-fence.end.markdown
|  ^ meta.code-fence.definition.end.markdown-gfm - punctuation
