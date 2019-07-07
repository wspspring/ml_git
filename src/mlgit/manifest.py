"""
© Copyright 2020 HP Development Company, L.P.
SPDX-License-Identifier: GPL-2.0-only
"""

from mlgit.utils import yaml_load, yaml_save
from pprint import pformat


class Manifest(object):
	def __init__(self, manifest):
		self._mfpath = manifest
		self._manifest = yaml_load(manifest)

	def add(self, key, file, stats=None):
		mf = self._manifest
		try:
			mf[key].add(file)
		except:
			mf[key] = {file}

	def rm(self, key, file):
		mf = self._manifest
		try:
			files = mf[key]
			if len(files) == 1:
				del(mf[key])
			else:
				files.remove(file)
				mf[key] = files
		except Exception as e:
			print(e)
			return False
		return True

	def rm_file(self, file):
		mf = self._manifest
		for key in mf:
			files = mf[key]
			if file not in files: continue

			if len(files) == 1:
				del(mf[key])
			else:
				files.remove(file)
				mf[key] = files
			return True
		return False


	def exists(self, key):
		return key in self._manifest

	def search(self, file):
		mf = self._manifest
		for key in mf:
			if file in mf[key]: return key
		return None

	def get(self, key):
		try:
			return self._manifest[key]
		except:
			return None

	def exists_keyfile(self, key, file):
		mf = self._manifest
		try:
			files = mf[key]
			return file in files
		except:
			pass
		return False

	def __repr__(self):
		return pformat(self._manifest, indent=4)

	def save(self):
		yaml_save(self._manifest, self._mfpath)