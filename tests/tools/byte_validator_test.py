import unittest

from src.tools.bytes_validator import BytesValidator


class ByteValidatorTest(unittest.TestCase):
    def test_checksum(self):
        self.global_test([1, 2, 3, 4], [10], True)
        self.global_test([79, 0, 22, 5], [106], True)
        self.global_test([12, 232, 23], [234], False)

    def global_test(self, bytes, crc, ans):
        self.assertEqual(BytesValidator().validate_checksum(bytes, crc), ans, f"Should be {ans}.")