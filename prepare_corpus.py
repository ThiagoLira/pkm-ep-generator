import os
import re

# ##### #
# Regex #
# ##### #
punctuations = re.escape('!"#%\'()*+,./:;<=>?@[\\]^_`{|}~')
re_remove_brackets = re.compile(r'\{.*\}')
re_remove_html = re.compile(r'<(\/|\\)?.+?>', re.UNICODE)
re_transform_numbers = re.compile(r'\d', re.UNICODE)
re_transform_emails = re.compile(r'[^\s]+@[^\s]+', re.UNICODE)
re_transform_url = re.compile(r'(http|https)://[^\s]+', re.UNICODE)
# Different quotes are used.
re_quotes_1 = re.compile(r"(?u)(^|\W)[‘’′`']", re.UNICODE)
re_quotes_2 = re.compile(r"(?u)[‘’`′'](\W|$)", re.UNICODE)
re_quotes_3 = re.compile(r'(?u)[‘’`′“”]', re.UNICODE)
re_dots = re.compile(r'(?<!\.)\.\.(?!\.)', re.UNICODE)
re_punctuation = re.compile(r'([,";:]){2},', re.UNICODE)
re_hiphen = re.compile(r' -(?=[^\W\d_])', re.UNICODE)
re_tree_dots = re.compile(u'…', re.UNICODE)
# Differents punctuation patterns are used.
re_punkts = re.compile(r'(\w+)([%s])([ %s])' %
                       (punctuations, punctuations), re.UNICODE)
re_punkts_b = re.compile(r'([ %s])([%s])(\w+)' %
                         (punctuations, punctuations), re.UNICODE)
re_punkts_c = re.compile(r'(\w+)([%s])$' % (punctuations), re.UNICODE)
re_changehyphen = re.compile(u'–')
re_doublequotes_1 = re.compile(r'(\"\")')
re_doublequotes_2 = re.compile(r'(\'\')')
re_trim = re.compile(r' +', re.UNICODE)


def clean_text(text):
    """Apply all regex above to a given string."""
    text = text.lower()
    text = re_tree_dots.sub('...', text)
    text = re.sub('\.\.\.', '', text)
    text = re_remove_brackets.sub('', text)
    text = re_changehyphen.sub('-', text)
    text = re_remove_html.sub(' ', text)
    text = re_transform_numbers.sub('0', text)
    text = re_transform_url.sub('URL', text)
    text = re_transform_emails.sub('EMAIL', text)
    text = re_quotes_1.sub(r'\1"', text)
    text = re_quotes_2.sub(r'"\1', text)
    text = re_quotes_3.sub('"', text)
    text = re.sub('"', '', text)
    text = re_dots.sub('.', text)
    text = re_punctuation.sub(r'\1', text)
    text = re_hiphen.sub(' - ', text)
    text = re_punkts.sub(r'\1 \2 \3', text)
    text = re_punkts_b.sub(r'\1 \2 \3', text)
    text = re_punkts_c.sub(r'\1 \2', text)
    text = re_doublequotes_1.sub('\"', text)
    text = re_doublequotes_2.sub('\'', text)
    text = re_trim.sub(' ', text)
    text = re.sub(r'(.,!?()])', r' \1 ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    return text.strip()

# remove annoying characters
chars = {
    '\x82' : ',',        # High code comma
    '\x84' : ',,',       # High code double comma
    '\x85' : '...',      # Tripple dot
    '\x88' : '^',        # High carat
    '\x91' : '',     # Forward single quote
    '\x92' : '',     # Reverse single quote
    '\x93' : '',     # Forward double quote
    '\x94' : '',     # Reverse double quote
    '\x95' : ' ',
    '\x96' : '-',        # High hyphen
    '\x97' : '--',       # Double hyphen
    '\x99' : ' ',
    '\xa0' : ' ',
    '\xa6' : '|',        # Split vertical bar
    '\xab' : '<<',       # Double less than
    '\xbb' : '>>',       # Double greater than
    '\xbc' : '1/4',      # one quarter
    '\xbd' : '1/2',      # one half
    '\xbe' : '3/4',      # three quarters
    '\xbf' : '\x27',     # c-single quote
    '\xa8' : '',         # modifier - under curve
    '\xb1' : ''          # modifier - under line
}

def replace_chars_ (text):
    def replace_chars(match):
        char = match.group(0)
        return chars[char]
    return re.sub('(' + '|'.join(chars.keys()) + ')', replace_chars, text)





corpus = ""


for filename in os.listdir('data/pokeCorpusBulba'):
    if (filename in [ ".DS_Store", "train.txt", "val.txt"]):
        pass
    else:
        with open('data/pokeCorpusBulba/' + filename, "r",encoding='utf-8') as text_file:

            clean_string =  (clean_text(replace_chars_(text_file.read())))

            corpus+= clean_string

with open('data/pokeCorpusBulba/' + 'train.txt', 'w') as text_file:
        text_file.write(corpus)
