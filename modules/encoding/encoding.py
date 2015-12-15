#!/usr/bin/env python3
import base64

def encode(s):
    """ This function encodes a message with base64 standard encode """
    encoded_text = base64.standard_b64encode(s)
    encoded_string = bytes.decode(encoded_text)
    print(encoded_string)

def decode(s):
    """ This function decodes a message with base64 standard decode """
    decoded_text = base64.standard_b64decode(s)
    decoded_string = bytes.decode(decoded_text)
    print(decoded_string)