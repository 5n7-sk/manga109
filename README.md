# manga109

This library is a type-based API client for [Manga109](http://www.manga109.org).

Manga109 is a dataset of manga (Japanese comics) for academic research.
An API client already exists ([here](https://github.com/manga109/manga109api)) for the dataset, but the dictionary-based data structures require users to have a detailed understanding of the dataset (key names, value types, etc.).
This library makes active use of `dataclass`, introduced in Python 3.7 (there is also a backport for earlier versions), to allow users to access any data while benefiting from completions and type hints.

<details>
<summary>Show data structures as YAML.</summary>

```yml
books:
  - book:
      title: str
      characters:
        - character:
            id: str
            name: str
      pages:
        - page:
            index: int
            width: int
            height: int
            bodies:
              - body:
                  id: str
                  xmin: int
                  ymin: int
                  xmax: int
                  ymax: int
                  character: str
            faces:
              - face:
                  id: str
                  xmin: int
                  ymin: int
                  xmax: int
                  ymax: int
                  character: str
            frames:
              - frame:
                  id: str
                  xmin: int
                  ymin: int
                  xmax: int
                  ymax: int
            texts:
              - text:
                  id: str
                  xmin: int
                  ymin: int
                  xmax: int
                  ymax: int
                  text: str
            image_path: str
```

</details>

## Usage

### Basic Usage

#### Make instance

```python
from manga109 import Manga109

client = Manga109("path/to/manga109")

# You can use specific titles.
client = Manga109("path/to/manga109", titles=["ARMS", "GakuenNoise", "PrayerHaNemurenai"])
```

#### Access any information

```python
print(client.books[0].title)  # ARMS
print(client.books[0].characters[14].name)  # タイロン
print(client.books[0].pages[80].texts[5].text)  # 返事して
```

#### Get the path to the image

```python
print(client.books[0].pages[17].image_path)  # path/to/manga109/images/ARMS/017.jpg
```

### Advanced Usage

#### Get the number of characters per title

```python
print([{b.title: len(b.characters)} for b in client.books])
# [{'ARMS': 23}, {'AisazuNihaIrarenai': 17}, {'AkkeraKanjinchou': 16}, ...]
```

#### Get a list of texts per page with one or more texts

```python
print([[t.text for t in p.texts] for p in client.books[0].pages if p.texts])
# [['あ'], ['キャーッ', 'はやく逃げないとまきぞえくっちゃう', ...], ...]
```

## Installation

- `Python 3.7+`

```sh
pip install git+https://github.com/skmatz/manga109.git
```
