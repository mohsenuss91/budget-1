#-*- coding: utf-8 -*-

class DbConnectionFile():

	def __init__(self, path):
		self.host = ""
		self.user = ""
		self.password = ""
		self.database = ""
		self.__OpenAndParseFile(path)
		
	def __OpenAndParseFile(self, path):
		file = open(path)

		while 1:
			line = file.readline()
			if not line:
				break
			self.__ParseLine(line)

	def __ParseLine(self, line):
		if self.__IsKeyword(line, "host"):
			self.host = self.__GetValue(line,"host")
		elif self.__IsKeyword(line, "user"):
			self.user = self.__GetValue(line,"user")
		elif self.__IsKeyword(line, "password"):
			self.password = self.__GetValue(line,"password")
		elif self.__IsKeyword(line, "database"):
			self.database = self.__GetValue(line,"database")

	def __IsKeyword(self,line,keyword):
		keyword += '='
		if line.find(keyword) > -1:
			return True
		else:
			return False

	def __GetValue(self,line,keyword):
		keyword += '='
		return (line[line.find(keyword)+len(keyword):]).strip()
