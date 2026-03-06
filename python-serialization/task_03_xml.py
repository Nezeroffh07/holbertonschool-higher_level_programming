#!/usr/bin/env python3
"""
Module for serializing and deserializing dictionaries using XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into XML and saves it to a file.
    """
    # Kök element yaradırıq (<data>)
    root = ET.Element("data")

    # Lüğətdəki hər bir açar-dəyər cütünü uşaq (child) element kimi əlavə edirik
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # XML ağacını yaradırıq və fayla yazırıq
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Reads XML data from a file and returns a deserialized Python dictionary.
    """
    try:
        # XML faylını analiz edirik (parse)
        tree = ET.parse(filename)
        root = tree.getroot()

        # Elementləri yenidən lüğətə (dict) yığırıq
        deserialized_dict = {}
        for child in root:
            deserialized_dict[child.tag] = child.text

        return deserialized_dict
    except FileNotFoundError:
        return None
