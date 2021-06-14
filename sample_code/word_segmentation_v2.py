#!/usr/bin/python
# -*- coding: utf-8 -*-

import trie
from codecs import open, decode

class WordSegmentation:
  # init Trie class
  def __init__(self, text):
    self.text = text
    self.model = trie.Trie()
    self.model.load_from_pickle("train_data")
    # self.result = []
    self.result_all = []
    # self.leftover = []
    self.startIndex = 0

  def isNumber(self, ch):
    # number letter
    return ch in "0123456789០១២៣៤៥៦៧៨៩"

  def parseNumber(self, index):
    result = ""
    while (index < len(self.text)):
      ch = self.text[index]
      ch = ch
      if self.isNumber(ch):
        result += self.text[index]
        index += 1
      else:
        return result

    return result
  def isEnglish(self, ch):
    return ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

  def parseEnglish(self, index):
    result = ""
    while (index < len(self.text)):
      ch = self.text[index]
      ch = ch
      if (self.isEnglish(ch) or self.isNumber(ch)):
        result += ch;
        index += 1
      else:
        return result
    return result

  def parseTrie(self, index):
    word = ''
    foundWord = ''

    while (index < len(self.text)):
      ch = self.text[index]
      ch = ch
      word += ch
      if self.model.searchWordPrefix(word):
        if self.model.searchWord(word):
          foundWord = word
      elif self.model.searchWord(word):
        return word
      else:
        return foundWord;

      index += 1

    return ""

  def check_words(self):
    while(self.startIndex < len(self.text)):
      ch = self.text[self.startIndex]
      ch = ch
      word = ''

      if self.isNumber(ch):
        word = self.parseNumber(self.startIndex)
      elif self.isEnglish(ch):
        word = self.parseEnglish(self.startIndex)
      else:
        word = self.parseTrie(self.startIndex)

      length = len(word)
      if length == 0:
        self.result_all.append(ch)
        self.startIndex += 1
        continue

      result = {}
      if self.model.searchWord(word) or self.isNumber(ch) or self.isEnglish(ch):
        self.result_all.append(word)
        result = word
      else:
        result = word

      # self.result_all.append(result)
      self.startIndex += length

  def tokenizer(self):
    return self.result_all
