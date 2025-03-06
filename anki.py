import genanki
import json
from hanziconv import HanziConv

_filename = 'complete.json'
with open(_filename, 'r') as file:
    data = json.load(file)

my_model = genanki.Model(
  1607392319,
  'Chinese Vocab',
  fields=[
    {'name': 'Vocab'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Vocab}}',
      'afmt': '{{FrontSide}}<hr id="Answer">{{Answer}}',
    },
  ])

decks = []
deck_id = 2059400110
for i in range (1, 8):
    decks.append(genanki.Deck(
      2059400110 + i,
      f'traditional_chinese::level{i}'))

for e in data:
    tradChar = HanziConv.toTraditional(e['simplified'])
    forms = []
    for form in e['forms']:
        meanings = '\n'.join(form['meanings'])
        forms.append(f'{form['transcriptions']['pinyin']}\n{meanings}')
    level = -1
    for l in e['level']:
        if 'new' in l:
            # example "new-1", map new-1 to 0
            level = int(l[4:5]) - 1
    if level == -1:
        continue
    answer = '\n\n'.join(forms)
    my_note = genanki.Note(
        model=my_model,
        fields=[tradChar, answer])
    decks[level].add_note(my_note)

for i in range(len(decks)):
  genanki.Package(decks[i]).write_to_file(f'chinese_{i+1}.apkg')
