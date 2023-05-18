#!/usr/bin/python3
""" Bit validation """

def validUTF8(data):
    # Variable to keep track of the number of bytes in the current UTF-8 character
    num_bytes = 0

    # Iterate over each byte in the data
    for byte in data:
        # Check if the byte is a continuation byte
        if num_bytes > 0:
            # If the byte doesn't start with "10" as the two most significant bits,
            # it's an invalid continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
        else:
            # If the byte is a single byte character (starts with "0"),
            # no need to check further
            if (byte >> 7) == 0b0:
                continue

            # Determine the number of bytes in the current UTF-8 character
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                # Invalid UTF-8 character
                return False

    # If there are remaining bytes without continuation bytes,
    # it's an invalid UTF-8 encoding
    return num_bytes == 0
