#!/usr/bin/python3
"""
This module defines a function that generates Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    # Üçbucağı ən təpədəki ilk sətirlə (1) başladırıq
    triangle = [[1]]

    # 1-ci sətirdən başlayaraq n-ci sətirə qədər dövr edirik
    for i in range(1, n):
        row = [1]  # Hər yeni sətir 1 ilə başlayır
        prev_row = triangle[-1]  # Bir əvvəlki sətri götürürük
        
        # Əvvəlki sətrin elementlərini cüt-cüt toplayıb yeni sətirə əlavə edirik
        for j in range(len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])
            
        row.append(1)  # Hər yeni sətir 1 ilə bitir
        triangle.append(row)  # Hazır olan sətri əsas üçbucağa əlavə edirik

    return triangle
