# Simple Static Site Generator Project

This repo was created following the Static Site Generator project on
[boot.dev](https://boot.dev). It is capable of the following:

- Recursively copying static assets from the `/static` directory into `/public`
- Recursively converting markdown files from the `/content` directory into HTML
  files in `/public`, based on a template

To use, simply run `./main.sh` which will automatically copy static content, generate static html, and start a local web server on port 8888 to host the generated content.

To run tests, simply run `./test.sh`, which will execute all created unit tests.

## Markdown Support

Based on the project, this simple static site generator does not support full markdown syntax. Instead, it supports a limited subset as specified by the project on `Boot.dev`.

The short version, it is expected that any markdown fed into this generator:
 - Must be well-formed
 - Must have all top-level blocks separated by an empty line
 - Must not have any nested inline markdown
 - Will only include supported markdown syntax

### Block Support

The supported syntax for top level blocks includes the following:

- `# headings, h1-h6`
- `> block quotes`
- ` ```code blocks``` `
- `1. ordered lists`
- `* unordered lists` or `- unordered lists`
- `paragraph`

Ordered lists must begin at 1 and be in order, unlike some markdown implementations. If out of order or not starting at 1, a paragraph will be generated instead.

Unordered lists can use `*` or `-`, but cannot mix these characters between items. A list that mixes these characters will instead generate a paragraph.

Code blocks currently will retain all new lines including at the beginning and end of the block, in the case that the code block is spread for readability, for example:

````
```
This will have an extra new line at the beginning and the end.
```
````

This could be considered a minor bug, but this was the resultant behavior of following the project and will be maintained for now.

### Inline Markdown

Inline markdown can be used inside of any block, but must not be nested. For example, the following does not work: `**Bold with nested *italic* text**`.

- `*italics*`
- `**bold**`
- `` `code` ``
- `![images](https://img.img/img.jpg)`
- `[links](https://boot.dev)`

## Potential Improvements

1. Additional code comments and documentation
2. Use Python style for documenting method and variable types to improve
   intellisense
3. Expand to allow nested markdown
4. Extend unit tests to include additional test cases, including more complex combinations