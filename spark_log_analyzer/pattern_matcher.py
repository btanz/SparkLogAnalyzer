import re



class PatternMatcher:

    def __init__(self, pattern, raise_read_errors=True):
        self._pattern = pattern
        self._raise_read_errors = raise_read_errors


    def match(self, input_line):
        match = re.search(self._pattern, input_line)
        if (match is None):
            if self._raise_read_errors:
                raise ValueError("Invalid input line: %s" % input_line)
            else:
                return {
                    'remote_host': None,
                    'client_id': None,
                    'user_id': None,
                    'time_received': None,
                    'request_method': None,
                    'request_first_line': None,
                    'request_protocol': None,
                    'status_code': None,
                    'response_bytes': 0
                }

        match_dict = {
            'remote_host': match.group(1),
            'client_id': match.group(2),
            'user_id': match.group(3),
            'time_received': match.group(4),
            'request_method': match.group(5),
            'request_first_line': match.group(6),
            'request_protocol': match.group(7),
            'status_code': int(match.group(8)),
            'response_bytes': int(match.group(9))
        }
        return match_dict




