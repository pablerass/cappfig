# -*- coding: utf-8 -*-
"""Manage application configuration files."""
import configparser
import glob
import os


class __Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(__Singleton, cls).__call__(*args,
                                                                   **kwargs)
        return cls._instances[cls]


class Cappfig(metaclass=__Singleton):
    """Application configuration class."""

    def __init__(self, name, pattern="*.conf"):
        """Create application config."""
        self.__name = name
        self.__pattern = name

        self.__conf = configparser.ConfigParser()
        self.__conf.read(Cappfig.config_files())

    def config_files(self):
        """Get config files list."""
        return glob.glob(os.path.join(self.__config_dir(), self.__pattern))

    def __config_dir(self):
        if os.sys.platform == "linux" or os.sys.platform == "linux2":
            user_dir = os.path.join(os.path.join(os.getenv("HOME"),
                                                 ".{name}".format(name=self.__name), "etc"))
            opt_dir = "/opt/{name}/etc".format(name=self.__name)
            system_dir = "/etc/{name}".format(name=self.__name)
        elif os.sys.platform == "darwin":
            pass
        elif os.sys.platform == "win32":
            pass

        if os.path.exists(user_dir):
            return user_dir
        elif os.path.exists(opt_dir):
            return opt_dir
        elif os.path.exists(system_dir):
            return system_dir

    def get(self, section, option):
        """Get string option."""
        return self.__conf.get(section, option)

    def get_boolean(self, section, option):
        """Get boolean option."""
        return self.__conf.getboolean(section, option)

    def get_float(self, section, option):
        """Get float option."""
        return self.__conf.getfloat(section, option)

    def get_int(self, section, option):
        """Get integer option."""
        return self.__conf.getint(section, option)

    def has_option(self, section, option):
        """Return if the specified confi section has an determined option."""
        return self.__conf.has_option(section, option)

    def has_section(self, section):
        """Return if the configuration has a specified section."""
        return self.__conf.has_section(section)

    def options(self, section):
        """Return all section options."""
        return self.__conf.items(section)

    def sections(self):
        """Return all sections."""
        return self.__conf.sections
