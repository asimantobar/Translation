# -*- coding: utf-8 -*-

from gooey import Gooey, GooeyParser
<<<<<<< HEAD
<<<<<<< HEAD
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
version ='0.1.0'
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
                'url': 'https://github.com/asimantobar/Variable-Excluding-Translation'
            }]
        },{
        'name': _('Help'),
        'items': [{
            'type': 'Link',
            'menuTitle': _('Documentation'),
            'url': 'https://github.com/asimantobar/Variable-Excluding-Translation'
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
=======
=======
from gooey.gui.lang import i18n
from gooey.gui.lang.i18n import _
>>>>>>> a8fdd56 (updates:)
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
version ='0.1.0'
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
                'url': 'https://github.com/asimantobar/Variable-Excluding-Translation'
            }]
        },{
        'name': _('Help'),
        'items': [{
            'type': 'Link',
            'menuTitle': _('Documentation'),
            'url': 'https://github.com/asimantobar/Variable-Excluding-Translation'
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
<<<<<<< HEAD
        metavar="Folder",
        help="Select the directory with documents to translate:",
>>>>>>> 284fde0 (separar def & GUI)
=======
        metavar=_("Folder"),
        help=_("Select the directory with documents to translate"),
>>>>>>> a8fdd56 (updates:)
        widget="DirChooser",
    )

    info.add_argument(
        "-b",
        "--name",
<<<<<<< HEAD
<<<<<<< HEAD
        metavar=_("ID"),
        default="",
        help=_("Choose name to identify the translated documents (optional)")
    )

    lang = parser.add_argument_group(_('Select language(s) to translate documents'),                                
                                       gooey_options={'show_border': True, 'columns': 3 })
    
    lang.add_argument('--ES',
                        metavar=_('Spanish'),
=======
        metavar="ID:",
=======
        metavar=_("ID"),
>>>>>>> a8fdd56 (updates:)
        default="",
        help=_("Choose name to identify the translated documents (optional)")
    )

    lang = parser.add_argument_group(_('Select language(s) to translate documents'),                                
                                       gooey_options={'show_border': True, 'columns': 3 })
    
    lang.add_argument('--ES',
<<<<<<< HEAD
<<<<<<< HEAD
                        metavar='Español',
>>>>>>> 284fde0 (separar def & GUI)
=======
                        metavar='Spanish',
>>>>>>> ddafc94 (change icons. try to translate (failed))
=======
                        metavar=_('Spanish'),
>>>>>>> a8fdd56 (updates:)
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--ZH',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        metavar=_('Chinese (Simplified)'),
=======
                        metavar='Chino',
>>>>>>> 284fde0 (separar def & GUI)
=======
                        metavar='Chinese (Simplified)',
>>>>>>> ddafc94 (change icons. try to translate (failed))
=======
                        metavar=_('Chinese (Simplified)'),
>>>>>>> a8fdd56 (updates:)
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--DE',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        metavar=_('German'),
=======
                        metavar='Alemán',
>>>>>>> 284fde0 (separar def & GUI)
=======
                        metavar='German',
>>>>>>> ddafc94 (change icons. try to translate (failed))
=======
                        metavar=_('German'),
>>>>>>> a8fdd56 (updates:)
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--FR',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        metavar=_('French'),
=======
                        metavar='Francés',
>>>>>>> 284fde0 (separar def & GUI)
=======
                        metavar='French',
>>>>>>> ddafc94 (change icons. try to translate (failed))
=======
                        metavar=_('French'),
>>>>>>> a8fdd56 (updates:)
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--PT',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        metavar=_('Portuguese'),
=======
                        metavar='Portugués',
>>>>>>> 284fde0 (separar def & GUI)
=======
                        metavar='Portuguese',
>>>>>>> ddafc94 (change icons. try to translate (failed))
=======
                        metavar=_('Portuguese'),
>>>>>>> a8fdd56 (updates:)
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--IT',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        metavar=_('Italian'),
=======
                        metavar='Italiano',
>>>>>>> 284fde0 (separar def & GUI)
=======
                        metavar='Italian',
>>>>>>> ddafc94 (change icons. try to translate (failed))
=======
                        metavar=_('Italian'),
>>>>>>> a8fdd56 (updates:)
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--EU',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        metavar=_('Basque'),
=======
                        metavar='Euskera',
>>>>>>> 284fde0 (separar def & GUI)
=======
                        metavar='Basque',
>>>>>>> ddafc94 (change icons. try to translate (failed))
=======
                        metavar=_('Basque'),
>>>>>>> a8fdd56 (updates:)
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--JA',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        metavar=_('Japanese'),
=======
                        metavar='Japonés',
>>>>>>> 284fde0 (separar def & GUI)
=======
                        metavar='Japanese',
>>>>>>> ddafc94 (change icons. try to translate (failed))
=======
                        metavar=_('Japanese'),
>>>>>>> a8fdd56 (updates:)
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )
    lang.add_argument('--AR',
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                        metavar=_('Arabic'),
=======
                        metavar='Arabe',
>>>>>>> 284fde0 (separar def & GUI)
=======
                        metavar='Arabic',
>>>>>>> ddafc94 (change icons. try to translate (failed))
=======
                        metavar=_('Arabic'),
>>>>>>> a8fdd56 (updates:)
                        widget='CheckBox',
                        action='store_true',
                        default=False,
                        )

    args = parser.parse_args()
    translate_files(args)
<<<<<<< HEAD
<<<<<<< HEAD


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    

if __name__ == "__main__":
    main()
    
>>>>>>> 284fde0 (separar def & GUI)
=======


if __name__ == "__main__":
    main()
<<<<<<< HEAD

>>>>>>> ddafc94 (change icons. try to translate (failed))
=======
>>>>>>> 48bd011 (GUI Translation)
=======
    main()
>>>>>>> a8fdd56 (updates:)
