# -*- coding: utf-8 -*-

import os
import pandas as pd
from mtranslate import translate

<<<<<<< HEAD
<<<<<<< HEAD
path = 'C:/Users/usuario/Desktop/Traducciones'

def process_pot(folder_path):
    data_frames = []
    names = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".pot"):
            filepath = os.path.join(folder_path, filename)
            names.append(filename) 
            with open(filepath, 'r', encoding='utf-8') as file:
=======
path = 'C:/Users/usuario/Downloads/translations'
=======
path = 'C:/Users/usuario/Desktop/Traducciones'
>>>>>>> 5b14780 (fix bugs in pot document translations)

def process_pot(folder_path):
    data_frames = []
    names = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".pot"):
            filepath = os.path.join(folder_path, filename)
<<<<<<< HEAD
            with open(filepath, 'r') as file:
>>>>>>> 6f5a66c (translate to pot files)
=======
            names.append(filename) 
            with open(filepath, 'r', encoding='utf-8') as file:
>>>>>>> 5b14780 (fix bugs in pot document translations)
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

<<<<<<< HEAD
<<<<<<< HEAD
    return data_frames, names


=======
    return data_frames
>>>>>>> 6f5a66c (translate to pot files)
=======
    return data_frames, names


>>>>>>> 5b14780 (fix bugs in pot document translations)

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
<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
        df.rename(columns={column: 'msgstr'}, inplace=True)
>>>>>>> 5b14780 (fix bugs in pot document translations)

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

<<<<<<< HEAD
results = process_txt(path)
>>>>>>> 6f5a66c (translate to pot files)
=======
    with open(filepath, 'w', encoding='utf-8') as new_file:
        new_file.writelines(new_lines)



results, filenames = process_pot(path)
>>>>>>> 5b14780 (fix bugs in pot document translations)

for df in results:
    translation(df)

<<<<<<< HEAD
<<<<<<< HEAD
cont = 0
for df in results:
    translations = df.set_index('msgid')['msgstr'].to_dict()
    filepath = 'C:/Users/usuario/Desktop/Traducciones/' + filenames[cont]
    write_translations(filepath, translations)
    cont += 1
    
=======
for df in results:
    translations = df.set_index('msgid')['Translation_ZH'].to_dict()
    write_translations(path, translations)
>>>>>>> 6f5a66c (translate to pot files)
=======
cont = 0
for df in results:
    translations = df.set_index('msgid')['msgstr'].to_dict()
    filepath = 'C:/Users/usuario/Desktop/Traducciones/' + filenames[cont]
    write_translations(filepath, translations)
    cont += 1
    
>>>>>>> 5b14780 (fix bugs in pot document translations)
