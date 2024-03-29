# Copyright (c) 2012 Adam Karpierz
# Licensed under the zlib/libpng License
# https://opensource.org/license/zlib

__all__ = ('StreamEmitter',)

from .__config__ import origin
origin = __import__(origin, globals(), locals(), ["QtCore"], 0)


class StreamEmitter(origin.QtCore.QObject):

    message = origin.QtCore.Signal(object)

    def write(self, data):
        self.message.emit(data)

    def flush(self):
        pass
