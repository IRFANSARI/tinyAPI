# ----- Info ------------------------------------------------------------------

__author__ = 'Michael Montero <mcmontero@gmail.com>'

# ----- Imports ---------------------------------------------------------------

from tinyAPI.base.exception import tinyAPIException

__all__ = [
    'DataStoreDuplicateKeyException',
    'DataStoreException',
    'DataStoreForeignKeyException',
    'IllegalMixOfCollationsException'
]

# ----- Public Classes --------------------------------------------------------

class DataStoreException(tinyAPIException):
    '''Named exception identifying an issue specifically with an underlying
       data store.'''
    pass


class ColumnCannotBeNullException(DataStoreException):

    def __init__(self, column_name):
        super(ColumnCannotBeNullException, self) \
            .__init__(
                "Column '{}' cannot be null.".format(column_name)
            )

        self.column_name = column_name


class DataStoreDuplicateKeyException(DataStoreException):
    '''Named exception identifying when a duplicate key is being added to a
       RDBMS.'''
    pass


class DataStoreForeignKeyException(DataStoreException):
    '''A foreign key constraint failed to match a parent record.'''
    pass


class IllegalMixOfCollationsException(DataStoreException):
    '''An illegal mix of collations error was generated.'''

    def __init__(self, sql, binds):
        super(IllegalMixOfCollationsException, self) \
            .__init__(
                'sql:\n\n"{}"\n-----\nbinds:\n\n{}'.format(sql, binds)
            )
