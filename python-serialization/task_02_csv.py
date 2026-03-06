#!/usr/bin/env python3
"""
Module for converting CSV data to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads data from a CSV file and converts it into a JSON file.
    
    Args:
        csv_filename (str): The name of the source CSV file.
        
    Returns:
        bool: True if conversion was successful, False otherwise.
    """
    try:
        # 1. CSV faylını oxuyuruq
        with open(csv_filename, mode='r', encoding='utf-8') as csv_f:
            # DictReader hər sətri avtomatik lüğətə (dict) çevirir
            reader = csv.DictReader(csv_f)
            data_list = [row for row in reader]

        # 2. Məlumatı data.json faylına yazırıq
        with open('data.json', mode='w', encoding='utf-8') as json_f:
            json.dump(data_list, json_f)

        return True

    except FileNotFoundError:
        # Fayl tapılmadıqda False qaytarırıq
        return False
    except Exception:
        # Digər gözlənilməz xətalar zamanı False qaytarırıq
        return False
