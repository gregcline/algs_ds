from typing import List, Optional, Set
import pdb


class Node:
    def __init__(self, terminal=False):
        self.terminal = terminal
        self.children = dict()

    def __repr__(self):
        return f'<Node terminal={self.terminal}, children={[repr(child) for child in self.children]}>'

    def __str__(self):
        return repr(self)


class Dictionary:
    def __init__(self, words: List[str]):
        self.dictionary = Node()
        self.possible_matches: Set[str] = set()

        working_node = self.dictionary
        for word in words:
            for char in word:
                if char not in working_node.children:
                    working_node.children[char] = Node()
                working_node = working_node.children[char]
            working_node.terminal = True
            working_node = self.dictionary

    def is_member(self, query, working_node=None):
        if working_node is None:
            working_node = self.dictionary

        for i, char in enumerate(query):
            if char in working_node.children:
                working_node = working_node.children[char]
            elif char == '*':
                for (_key, child) in working_node.children.items():
                    if self.is_member(query[i+1:], child):
                        return True
                return False
            else:
                return False
        return working_node.terminal

    def __repr__(self):
        return f'<Dictionary dictionary={self.dictionary}>'

    def __str__(self):
        return repr(self)


word_set = ['foo', 'fot', 'fod', 'aodi', 'fodo']
print(word_set)
words = Dictionary(word_set) # foo
# print('foo', words.is_member('foo'))
# print('fot', words.is_member('fot'))
# print('fo', words.is_member('fo'))
# print('food', words.is_member('food'))
# print('fodo', words.is_member('fodo'))
# print('fod', words.is_member('fod'))
print('fo*', words.is_member('fo*'))
print('fo*o', words.is_member('fo*o'))
print('*o*o', words.is_member('*o*o'))
