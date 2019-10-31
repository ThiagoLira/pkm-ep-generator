# Pokémon Anime Episode Generator 

In-depth explanation can be found on this blog post 


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
