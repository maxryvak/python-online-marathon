import unittest
from unittest.mock import patch, Mock, mock_open, MagicMock

def file_parser(file, *args):
    with open(file) as file:
        text = file.read()
        if len(args) == 1:
            return f'Found {text.count(args[0])} strings'
        else:
            count = text.count(args[0])
            text = text.replace(args[0], args[1])
            return f'Replaced {count} strings'


class ParserTest(unittest.TestCase):
    def test_file_read(self):
        with patch('builtins.open', mock_open(read_data='123456789098765432')):
            with open('/dev/null') as f:
                self.assertEqual(file_parser('/dev/null', '2'), 'Found 2 strings')

    def test_file_write(self):
        with patch('builtins.open', mock_open(read_data='123456789098765432')):
            with open('/dev/null') as f:
                self.assertEqual(file_parser('/dev/null', '2', '_'), 'Replaced 2 strings')
