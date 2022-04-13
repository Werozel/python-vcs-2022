import ast
import dataclasses
import importlib
import inspect
import itertools
import sys
import textwrap
from difflib import SequenceMatcher
from dataclasses import dataclass


@dataclass
class Method:
    full_name: str
    code: str

    def __eq__(self, other):
        if not isinstance(other, Method):
            return False
        if self.full_name == other.full_name:
            return True
        if SequenceMatcher(a=self.code, b=other.code).ratio() >= 0.95:
            return True

    def __repr__(self):
        return self.full_name


def parse_methods(module_name: str, module) -> list[Method]:
    methods = []

    members = inspect.getmembers(module)
    for name, value in members:
        full_name = f"{module_name}.{name}"
        if inspect.isclass(value) and not name.startswith("__"):
            methods += parse_methods(full_name, value)
        elif inspect.isfunction(value):
            code = textwrap.dedent(inspect.getsource(value))
            code_ast = ast.parse(code)
            for node in ast.walk(code_ast):
                for attr in ['name', 'id', 'arg', 'attr']:
                    if hasattr(node, attr):
                        setattr(node, attr, '_')
            methods.append(Method(full_name, ast.unparse(code_ast)))

    return methods


def print_similar_methods(methods: list[Method]):
    for method1, method2 in itertools.combinations(methods, 2):
        if method1.full_name == method2.full_name:
            continue
        if method1 == method2:
            print(method1, method2, sep=' ')


def main():
    module_name_1 = sys.argv[1]
    module_name_2 = sys.argv[2] if len(sys.argv) > 2 else None
    methods1 = parse_methods(module_name_1, importlib.import_module(module_name_1))
    methods2 = parse_methods(module_name_2, importlib.import_module(module_name_2)) if module_name_2 else []
    print_similar_methods(methods1 + methods2)


if __name__ == "__main__":
    main()
