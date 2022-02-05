from logging import Handler, _Level, LogRecord
from warnings import warn
from os import getpid
from sys import argv
from datetime import datetime
from threading import current_thread, Semaphore
from queue import Queue
from ..formatters import AwsFormatter
from typing import List, Optional, Union, Mapping


_defaultFormatter = AwsFormatter("")

class AwsLogHandler(Handler):

    creating_log_stream: Semaphore
    shutting_down: Semaphore
    queues: Mapping[str, Queue]
    

    def __init__(self, level: _Level = ...) -> None:
        super().__init__(level)
        
    
    def emit(self, record: LogRecord) -> None:
        pass

    def acquire(self):
        """
        Acquire the I/O thread lock.
        """
        if self.lock:
            self.lock.acquire()

    def release(self):
        """
        Release the I/O thread lock.
        """
        if self.lock:
            self.lock.release()

    def format(self, record):
        """
        Format the specified record.

        If a formatter is set, use it. Otherwise, use the default formatter
        for the module.
        """
        if self.formatter:
            fmt = self.formatter
        else:
            fmt = _defaultFormatter
        return fmt.format(record)

    def flush(self):
        """
        Ensure all logging output has been flushed.

        This version does nothing and is intended to be implemented by
        subclasses.
        """
        self.shutting_down

    def close(self):
        """
        Tidy up any resources used by the handler.

        This version removes the handler from an internal map of handlers,
        _handlers, which is used for handler lookup by name. Subclasses
        should ensure that this gets called from overridden close()
        methods.
        """
        super().close()
