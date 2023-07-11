#!/usr/bin/python3
"""8. Class to JSON"""


def class_to_json(obj):
	"""
	Returns the dict of an object

	Args:
		obj (object): the object

	Returns:
		dict
	"""
	return obj.__dict__
