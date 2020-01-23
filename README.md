# Hindi Transliterator
This assignment implements an English to Hindi transliterator and a
Hindi to Romanized Hindi transliterator
## Mappings
All the mappings are in `data/`. Files `data/roman*.json` are the mappings
for Hindi to Romanized Hindi and the rest are the mappings from English to Hindi.
## Run
- To transliterate from English to Hindi
  `python3 transliterate.py Hindi <word>`
  where, `<word>` is the string in English
- To transliterate from Hindi to Romanized Hindi
  `python3 transliterate.py Roman <word>`
  where, `<word>` is the string in Hindi
