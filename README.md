# Pokémon Anime Episode Generator 

In-depth explanation can be found on this blog post https://towardsdatascience.com/using-gpt-2-to-generate-pok%C3%A9mon-anime-episodes-113c0f15859c


To get all the data from Bulbapedia run:

```bash
python crawler_bulbapedia.py
```

And prepare the corpus for training:

```bash
python prepare_corpus.py
```

Then train the model:

```bash
python train_gpt2.py
```
