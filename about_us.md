---
title: Welcome to the Site
substitutions:
    snippet: "I'm a **substitution**"
---

# About Us

Let's see the `snippet`: {{ snippet }}

## Course Reference Site:

[Jetbrains Tutorials - Sphinx Sites](https://www.jetbrains.com/pycharm/guide/tutorials/sphinx_sites)

We are Schlockchain, thought leaders in innovation.

We are **bold** and *innovative*.

Our `def mega_chain` function works really well:

    def mega_chain(): return

> I'm so glad I put my life savings in Schlockchain.
> >Said Nobody Ever
> >> Ha ha ha!

We have a patented algorithm:
- Glacially slow
- Which melts glaciers

... and a roadmap to success:
1. Start and LLC
2. Get a Series A investment round
3. Get a Series B investment round
4. Continue

Schlockchain is written in [Python](https://www.python.org/), [Markdown (CommonMark)](https://commonmark.org/), and [MyST](https://myst-parser.readthedocs.io/en/latest/). Plus is used [Sphinx](https://www.sphinx-doc.org/en/master/index.html) and [LiveReload](https://livereload.readthedocs.io/en/latest/).

```{note}
Schlockchain is written in [Python](https://www.python.org/) for some data science or something reasons.
```

```{warning}
Schlockchain is written in [Python](https://www.python.org/) for some data science or something reasons.

- Careful, python is **awesome**
- Using it will thus make you **awesome**
```

:::{warning}
MyST version using `:::`

Schlockchain is written in [Python](https://www.python.org/) for some data science or something reasons.

- Careful, python is **awesome**
- Using it will thus make you **awesome**
:::

Image from a URL:

![Python Logo](https://www.python.org/static/community_logos/python-logo.png)

Local image:

![Python Logo (local)](python-logo.png)

```{image} python-logo.png
:alt: Python Logo
:class: bg-primary
:width: 200px
:align: center
```
:::{figure-md} logo-target
:class: myclass

<img src="python-logo.png" alt="Python Logo" class="bg-primary" width="300px">

Python comes from the *Python Software Foundation*.
:::

For a sexy carousel of stock photos, visit this site's [homepage](./index).

Use the page title automatically- leave `[homepage]` blank! That is like this: `[]`.
This should use the page's title [](./index).

## More Authoring

## Headings and Roles

(investors)=
## Investors

Our investors are very proud to be involved with us.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc viverra turpis vitae est viverra, ut feugiat eros rutrum. In lacus leo, pharetra ut ultrices vitae, auctor et massa. Vivamus vel ultrices ipsum. Nam neque diam, sollicitudin eget augue a, dictum dignissim leo. Aliquam et lorem semper, porta magna vitae, porttitor libero. Mauris eget condimentum mi. Nulla sollicitudin dapibus massa, nec ornare felis varius sed. Donec dictum efficitur elit a pharetra. Aliquam erat volutpat. Nam ac lacus scelerisque, rhoncus libero at, aliquam risus. Nulla ultricies urna eget tempus sagittis.

Suspendisse fermentum lacus non nunc accumsan pellentesque. Pellentesque euismod tellus quis risus consequat lobortis. Maecenas placerat turpis facilisis erat faucibus suscipit. Phasellus quam ligula, pretium vitae ligula vitae, imperdiet feugiat ante. Suspendisse quis semper massa. Maecenas dignissim magna eget hendrerit scelerisque. Aliquam rhoncus luctus odio at efficitur. Cras egestas tempor tellus ac malesuada. Ut ex lacus, maximus a est id, cursus pretium ante. 

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc viverra turpis vitae est viverra, ut feugiat eros rutrum. In lacus leo, pharetra ut ultrices vitae, auctor et massa. Vivamus vel ultrices ipsum. Nam neque diam, sollicitudin eget augue a, dictum dignissim leo. Aliquam et lorem semper, porta magna vitae, porttitor libero. Mauris eget condimentum mi. Nulla sollicitudin dapibus massa, nec ornare felis varius sed. Donec dictum efficitur elit a pharetra. Aliquam erat volutpat. Nam ac lacus scelerisque, rhoncus libero at, aliquam risus. Nulla ultricies urna eget tempus sagittis.

Suspendisse fermentum lacus non nunc accumsan pellentesque. Pellentesque euismod tellus quis risus consequat lobortis. Maecenas placerat turpis facilisis erat faucibus suscipit. Phasellus quam ligula, pretium vitae ligula vitae, imperdiet feugiat ante. Suspendisse quis semper massa. Maecenas dignissim magna eget hendrerit scelerisque. Aliquam rhoncus luctus odio at efficitur. Cras egestas tempor tellus ac malesuada. Ut ex lacus, maximus a est id, cursus pretium ante. 

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc viverra turpis vitae est viverra, ut feugiat eros rutrum. In lacus leo, pharetra ut ultrices vitae, auctor et massa. Vivamus vel ultrices ipsum. Nam neque diam, sollicitudin eget augue a, dictum dignissim leo. Aliquam et lorem semper, porta magna vitae, porttitor libero. Mauris eget condimentum mi. Nulla sollicitudin dapibus massa, nec ornare felis varius sed. Donec dictum efficitur elit a pharetra. Aliquam erat volutpat. Nam ac lacus scelerisque, rhoncus libero at, aliquam risus. Nulla ultricies urna eget tempus sagittis.

Suspendisse fermentum lacus non nunc accumsan pellentesque. Pellentesque euismod tellus quis risus consequat lobortis. Maecenas placerat turpis facilisis erat faucibus suscipit. Phasellus quam ligula, pretium vitae ligula vitae, imperdiet feugiat ante. Suspendisse quis semper massa. Maecenas dignissim magna eget hendrerit scelerisque. Aliquam rhoncus luctus odio at efficitur. Cras egestas tempor tellus ac malesuada. Ut ex lacus, maximus a est id, cursus pretium ante. 

## Code in a Document

Python

```python
def hello(name):
   return f'Hello {name}'
```

Javascript

```javascript
 function hello(msg) {
    return `Hello ${msg}`
 }
```

Using MyST syntax:

```{code-block} javascript
 function hello(msg) {
   return `Hello ${msg}`
 }
```

With line numbers `:linenos:`:

```{code-block} javascript
:linenos:
 function hello(msg) {
   return `Hello ${msg}`
 }
```

With line numbers `:linenos:` & `:emphasis-lines:`

```{code-block} javascript
:linenos:
:emphasize-lines: 2
 function hello(msg) {
   return `Hello ${msg}`
 }
```

## Including Code from a File

### Using the `literalinclude` Directive

```{literalinclude} my_demo.py
```

### Using `emphsize-lines` Option

```{literalinclude} my_demo.py
:emphasize-lines: 2-3
```

### Referencing Symbols in Docs

As we can see in [our Python class](my_demo.MyDemo), Python is fun!

### Role-based syntax, with the Python domain as a prefix

As we can see in {py:class}`my_demo.MyDemo`, Python is fun!

### With Own Link Text

As we can see in {py:class}`HW <my_demo.MyDemo>`, Python is fun!

### Linking to a Role

#### In regular Markdown

Let's talk about the power of [Sphinx roles](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#ref-role).

#### MyST Syntax

Let's talk about the power of [Sphinx roles](sphinx:usage/restructuredtext/roles).

#### To a Page "Role"

Let's talk about the power of [Sphinx roles](sphinx:ref-role).

#### Let Remote Title Be Local Link Text i.e. using `[]`

Let's talk about the power of [](sphinx:ref-role).

### Linking to Domains

Let's talk about the power of {rst:dir}`code-block`.

## Debugging

