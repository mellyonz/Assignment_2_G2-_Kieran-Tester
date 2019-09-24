from abc import ABC, abstractmethod

"""
    Tiny Interpreted Graphic = TIGr
    Keep the interfaces defined below in your work.
"""


class AbstractDrawer(ABC):
    """ Responsible for defining an interface for drawing """

    @abstractmethod
    def select_pen(self, pen_num):
        pass

    @abstractmethod
    def pen_down(self):
        pass

    @abstractmethod
    def pen_up(self):
        pass

    @abstractmethod
    def go_along(self, along):
        pass

    @abstractmethod
    def go_down(self, down):
        pass

    @abstractmethod
    def draw_line(self, direction, distance):
        pass


class AbstractParser(ABC):
    def __init__(self, drawer):
        self.drawer = drawer
        self.source = []
        self.command = ''
        self.data = 0

    @abstractmethod
    def parse(self, raw_source):
        pass


class AbstractInterface(ABC):
    """
        Responsible for providing source text for parsing and drawing
        Initiates the Draw use-case.
        Links to a parser and passes the source text onwards
    """

    def __init__(self, parser, optional_file_name=None):
        self.parser = parser
        self.interface = None
        self.config = None

    @abstractmethod
    def create_interface(self):
        pass

    @abstractmethod
    def open_config(self):
        pass

    @abstractmethod
    def go(self):
        pass
