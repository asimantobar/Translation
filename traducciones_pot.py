# -*- coding: utf-8 -*-

import os
import pandas as pd
from mtranslate import translate

path = 'C:/Users/usuario/Downloads/translations'


def process_txt(folder_path):
    data_frames = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, 'r') as file:
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

    return data_frames

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

def write_translations(filepath, translations):
    filename = os.path.basename(filepath)
    filename_parts = os.path.splitext(filename)
    new_filename = filename_parts[0] + '_language' + filename_parts[1]
    new_filepath = os.path.join(os.path.dirname(filepath), new_filename)

    with open(filepath, 'r') as file:
        lines = file.readlines()

    with open(new_filepath, 'w') as new_file:
        for line in lines:
            if line.startswith('msgid'):
                msgstr = translations.get(line.split('msgid')[1].strip()[1:-1])
                if msgstr:
                    new_line = 'msgstr "{}"\n'.format(msgstr)
                    new_file.write(new_line)
                else:
                    new_file.write(line)
            else:
                new_file.write(line)

results = process_txt(path)

for df in results:
    translation(df)

for df in results:
    translations = df.set_index('msgid')['Translation_ZH'].to_dict()
    write_translations(path, translations)
