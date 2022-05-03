from typing import Type
from .widget import Widget
from .text_widget import TextWidget
from .array_widget import ArrayWidget
from .checkbox_widget import CheckBoxWidget
from .select_widget import SelectWidget

__widgets__: list[Type['Widget']] = [
    TextWidget,
    ArrayWidget,
    CheckBoxWidget,
    SelectWidget
]
