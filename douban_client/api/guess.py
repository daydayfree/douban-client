# -*- coding: utf-8 -*-

from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Guess(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Guess>'

    def notes(self, user_id):
        return self._get('/v2/note/people_notes/%s/guesses'%user_id)

    def albums(self, user_id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/album/people_albums/%s/guesses'%user_id, start=start, count=count)
