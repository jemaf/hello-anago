# %% [markdown]
# # Hello, anago
# Hello world of anago library

# %%
import anago
from anago.utils import download

# %%
url = 'https://s3-ap-northeast-1.amazonaws.com/dev.tech-sketch.jp/chakki/public/conll2003_en.zip'
weights, params, preprocessor = download(url)

# %%
model = anago.Sequence.load(weights, params, preprocessor)

# %%
text = 'President Obama is speaking at the White House.'
model.analyze(text)