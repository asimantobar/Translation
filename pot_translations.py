# -*- coding: utf-8 -*-

import os
import pandas as pd
from mtranslate import translate

path = 'C:/Users/usuario/Desktop/Traducciones'

def process_pot(folder_path):
    data_frames = []
    names = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".pot"):
            filepath = os.path.join(folder_path, filename)
            names.append(filename) 
            with open(filepath, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            df_data = []
            msgid = None
            for line in lines:
                if line.startswith('msgid'):
                    msgid = line.split('msgid')[1].strip()[1:-1]
                    df_data.append((msgid))

            df = pd.DataFrame(df_data, columns=['msgid'])
            df = df[df['msgid'] != '']
            data_frames.append(df)

    return data_frames, names



def translation(df):
    target_lang = {'Translation_ZH': 'zh-CN'}
    for column, language in target_lang.items():
        translations = []
        for content in df['msgid']:
            try:
                translation = translate(content, language, 'en')
                translations.append(translation)
            except Exception as e:
                print(f"Error occurred during translation: {str(e)}")
                translations.append(None)

        df[column] = translations
        df.rename(columns={column: 'msgstr'}, inplace=True)

def write_translations(filepath, translations):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if line.startswith('msgid'):
            msgid = line.split('msgid')[1].strip()[1:-1]
            msgstr = translations.get(msgid)
            if msgstr is not None:
                new_lines.append(line)
                new_lines.append('msgstr "{}"\n'.format(msgstr))
                idx += 1
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
        idx += 1

    with open(filepath, 'w', encoding='utf-8') as new_file:
        new_file.writelines(new_lines)



results, filenames = process_pot(path)

for df in results:
    translation(df)

cont = 0
for df in results:
    translations = df.set_index('msgid')['msgstr'].to_dict()
    filepath = 'C:/Users/usuario/Desktop/Traducciones/' + filenames[cont]
    write_translations(filepath, translations)
    cont += 1
    
