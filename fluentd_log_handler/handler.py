from io import BytesIO

import msgpack
from fluent import handler


class NeilFluentdFormatter(handler.FluentRecordFormatter):
    def __init__(self, task_name=''):
        structure = {
            'hostname': '%(hostname)s',
            'module': '%(module)s',
            'funcName': '%(funcName)s',
            'type': '%(levelname)s',
            'created': '%(created)f',
            'process': '%(process)d',
            'thread': '%(thread)d',
            'processName': '%(processName)s',
            'pathName': '%(pathname)s',
            'levelno': '%(levelno)s'
        }
        structure['taskName'] = task_name
        super().__init__(structure)


def overflow_handler(pendings):
    unpacker = msgpack.Unpacker(BytesIO(pendings))
    for unpacked in unpacker:
        print(unpacked)


class NeilFluentdHandler(handler.FluentHandler):
    def __init__(self, tag, host='127.0.0.1', port=24224, task_name=''):
        super().__init__(tag=tag, host=host, port=port, buffer_overflow_handler=overflow_handler)
        formatter = NeilFluentdFormatter(task_name)
        self.setFormatter(formatter)