# -*- coding: utf-8 -*-

from gooey import Gooey, GooeyParser
from gooey.gui.lang import i18n
from gooey.gui.lang.i18n import _
from Translation_def import translate_files
import json
import os

def config_file():
    config_file_path = "config.json"
    default_config = {"language": "english"}

    if os.path.exists(config_file_path):
        with open(config_file_path, "r") as file:
            config_data = json.load(file)
        idioma = config_data.get("language")

    else:
        with open(config_file_path, "w") as file:
            json.dump(default_config, file)
        idioma = default_config["language"]
    return idioma


idioma = config_file()
version ='1.0.0'
date='04/07/2023'

i18n.load("C:/Users/usuario/Documents/automatic_translation/languages", idioma, "utf-8")


@Gooey(program_name="File Translation",
    program_description=_("Translate documents in the same directory"),
    default_size=(600, 650), image_dir='C:/Users/usuario/Documents/automatic_translation/images',
    language= idioma , language_dir='C:/Users/usuario/Documents/automatic_translation/languages',
    menu=[{
        'name': _('File'),
        'items': [{
                'type': 'AboutDialog',
                'menuTitle': _('About'),
                'name': _('Translation Demo'),
                'description': _('Common directory document translation'),
                'version': f'{version}',
                'copyright': f'{date}'
            }, {
                'type': 'MessageDialog',
                'menuTitle': _('Information'),
                'caption': '',
                'message': _('No current messages!')
            }, {
                'type': 'Link',
                'menuTitle': _('Visit Site'),
                'url': 'http://devserver:3000/asiman/automatic_translation.git'
            }]
        },{
        'name': _('Help'),
        'items': [{
            'type': 'Link',
            'menuTitle': _('Documentation'),
            'url': 'http://devserver:3000/asiman/automatic_translation.git'
        }]
    }],
    timing_options = {'show_time_remaining':True,
        'hide_time_remaining_on_complete':False,}, clear_before_run=True
)
    
def main():
    parser = GooeyParser(description=_("File Translation"))
    
    info = parser.add_argument_group(_('Directory Information'),                                
                                       gooey_options={'show_border': True, 'columns': 1 })
    info.add_argument(
        "-a",
        "--folder_path",
        metavar=_("Folder"),
        help=_("Select the directory with documents to translate"),
        widget="DirChooser",
    )

    info.add_argument(
        "-b",
        "--name",
        metavar=_("ID"),
        default="",
        help=_("Choose name to identify the translated documents (optional)")
    )

    lang = parser.add_argument_group(_('Select language(s) to translate documents'),                                
                                       gooey_options={'show_border': True, 'columns': 3 })
    
    lang.add_argument('--ES',
                        metavar=_('Spanish'),
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--ZH',
                        metavar=_('Chinese (Simplified)'),
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--DE',
                        metavar=_('German'),
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--FR',
                        metavar=_('French'),
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--PT',
                        metavar=_('Portuguese'),
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--IT',
                        metavar=_('Italian'),
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--EU',
                        metavar=_('Basque'),
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--JA',
                        metavar=_('Japanese'),
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--AR',
                        metavar=_('Arabic'),
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )

    args = parser.parse_args()
    translate_files(args)


if __name__ == "__main__":
    main()