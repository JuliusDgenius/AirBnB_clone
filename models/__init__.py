#!/usr/bin'python3
"""Init file to import storage"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
