import cmd
from typing import Optional

import pynames
from pynames.generators.elven import *
from pynames.generators.iron_kingdoms import *
from pynames.generators.orc import *
from pynames.generators.goblin import *
from pynames.generators.mongolian import *
from pynames.generators.korean import *
from pynames.generators.russian import *
from pynames.generators.scandinavian import *


class GeneratorWrapper:

    def __init__(self, race: str, generator):
        self.race = race
        self.name = generator.__name__
        self.generator = generator()


def get_wrapped_generators() -> list[GeneratorWrapper]:
    return [GeneratorWrapper('elven', WarhammerNamesGenerator),
            GeneratorWrapper('elven', DnDNamesGenerator),
            GeneratorWrapper('goblin', GoblinGenerator),
            GeneratorWrapper('iron_kingdoms', GobberFullnameGenerator),
            GeneratorWrapper('iron_kingdoms', ThurianMorridaneFullnameGenerator),
            GeneratorWrapper('iron_kingdoms', TordoranFullnameGenerator),
            GeneratorWrapper('iron_kingdoms', RynFullnameGenerator),
            GeneratorWrapper('iron_kingdoms', DwarfFullnameGenerator),
            GeneratorWrapper('iron_kingdoms', IossanNyssFullnameGenerator),
            GeneratorWrapper('iron_kingdoms', CaspianMidlunderSuleseFullnameGenerator),
            GeneratorWrapper('iron_kingdoms', KhadoranFullnameGenerator),
            GeneratorWrapper('iron_kingdoms', OgrunFullnameGenerator),
            GeneratorWrapper('iron_kingdoms', TrollkinFullnameGenerator),
            GeneratorWrapper('korean', KoreanNamesGenerator),
            GeneratorWrapper('mongolian', MongolianNamesGenerator),
            GeneratorWrapper('orc', OrcNamesGenerator),
            GeneratorWrapper('russian', PaganNamesGenerator),
            GeneratorWrapper('scandinavian', ScandinavianNamesGenerator)]


def filter_wrapped_generators(race: str = "", name: str = "") -> Optional[GeneratorWrapper]:
    generators = list(
        filter(
            lambda x: x.name.lower().startswith(name.lower()),
            filter(
                lambda x: x.race.lower().startswith(race.lower()),
                get_wrapped_generators()
            )
        )
    )
    return None if not generators else generators[0]


GENDERS = {'male': pynames.GENDER.MALE, 'female': pynames.GENDER.FEMALE}


class NameGenerator(cmd.Cmd):
    intro = 'Welcome to name generator! Don\'t forget to change the language'
    file = None

    def __init__(self):
        super().__init__()
        self.language = pynames.LANGUAGE.NATIVE

    def do_language(self, new_language: str):
        if new_language.lower() in pynames.LANGUAGE.ALL:
            self.language = new_language.lower()

    @staticmethod
    def do_info(str_args):
        args = str_args.split(' ')
        if len(args) == 0:
            print("Nothing to show")
            return

        race = args[0]
        if len(args) == 1:
            wrapped_generator = filter_wrapped_generators(race)
            if not wrapped_generator:
                print("No such generators")
                return
            print(wrapped_generator.generator.get_names_number(pynames.GENDER.MALE))
            return

        arg2 = args[1]
        if arg2 == 'language':
            wrapped_generator = filter_wrapped_generators(race)
            if not wrapped_generator:
                print('No such generators')
                return
            print(','.join(wrapped_generator.generator.languages))
            return

        if arg2.lower() in GENDERS.keys():
            wrapped_generator = filter_wrapped_generators(race)
            if not wrapped_generator:
                print('No such generators')
                return
            gender = GENDERS.get(arg2)
            print(wrapped_generator.generator.get_names_number(gender))
            return

        wrapped_generator = filter_wrapped_generators(race, arg2)
        if not wrapped_generator:
            print('No such generators')
            return

        if len(args) > 2:
            arg3 = args[2]
            if arg3.lower() not in GENDERS.keys():
                print("Unknown arg:", arg3)
                return
            gender = GENDERS.get(arg3)
            print(wrapped_generator.generator.get_names_number(gender))
        else:
            print(wrapped_generator.generator.get_names_number(pynames.GENDER.MALE))

    def do_generate(self, str_args):
        args = str_args.split(' ')
        if len(args) == 0:
            wrapped_generator = filter_wrapped_generators()
            if not wrapped_generator:
                print("Nothing to generate")
                return
            print(wrapped_generator.generator.get_name_simple(language=self.language))
            return

        race = args[0]
        if len(args) == 1:
            wrapped_generator = filter_wrapped_generators(race)
            if not wrapped_generator:
                print("No such generator")
                return
            print(wrapped_generator.generator.get_name_simple(language=self.language))
            return

        arg2 = args[1]
        if arg2.lower() in GENDERS.keys():
            wrapped_generator = filter_wrapped_generators(race)
            if not wrapped_generator:
                print('No such generators')
                return
            gender = GENDERS.get(arg2)
            print(wrapped_generator.generator.get_name_simple(gender=gender, language=self.language))
            return

        wrapped_generator = filter_wrapped_generators(race, arg2)
        if not wrapped_generator:
            print('No such generators')
            return

        if len(args) > 2:
            arg3 = args[2]
            if arg3.lower() not in GENDERS.keys():
                print("Unknown arg:", arg3)
                return
            gender = GENDERS.get(arg3)
            print(wrapped_generator.generator.get_name_simple(gender=gender, language=self.language))
        else:
            print(wrapped_generator.generator.get_name_simple(language=self.language))

    @staticmethod
    def do_bye(*_):
        return True


if __name__ == "__main__":
    NameGenerator().cmdloop()
