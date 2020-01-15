class NonPositiveError(Exception):
    pass


class PositiveList(list):

    def append(self, _T) -> None:
        self._T = _T
        if self._T > 0:
            super(PositiveList, self).append(self._T)
        else:
            raise NonPositiveError('You number is not positive')
