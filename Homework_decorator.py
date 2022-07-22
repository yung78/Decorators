import datetime


def logger(path: str):
    def _logger(some_function):

        def inside_func(*args, **kwargs):
            dt = datetime.datetime.now()
            dt_log = dt.strftime('%d.%m.%Y  %H:%M:%S')
            result = some_function(*args, **kwargs)
            with open(f'{path}\log.txt', 'a', encoding='utf8') as log:
                log.write(f'\n[{dt_log}] Name - {some_function.__name__}, '
                          f'arguments - {args} {kwargs}, result - {result}')
            return some_function(*args, **kwargs)

        return inside_func
    return _logger
