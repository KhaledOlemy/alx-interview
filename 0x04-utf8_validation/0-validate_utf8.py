#!/usr/bin/python3
"""Checks for UTF-8 validation"""

def validUTF8(data):
    """checks for UTF8 input is a list of integers."""
    return len(data) == len([i for i in data if i < 128])
