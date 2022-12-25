import array


class BytesValidator:
    """
    Class task is to validate bytes.
    """
    def validate_checksum(self, bytes_to_check: array, crc_sum: array):
        """
        Check bytes sum and returns if bytes are valid.

        :param bytes_to_check: Array of bytes to check.
        :param crc_sum: Array of checksum bytes.
        :return: Is valid bytes.
        """
        bytes_sum = sum(bytes_to_check)
        crc_sum = sum(crc_sum)

        return crc_sum == bytes_sum
