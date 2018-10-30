"""Setup module for tests"""
# pylint: disable = useless-super-delegation
import os
import hashids
from unittest import TestCase

class BaseTestCase(TestCase):
    """Setup class for unittests"""
    def setUp(self):
        HASHID_FIELD_SALT = os.environ.get('HASHID_FIELD_SALT')
        self.HASH_IDS = hashids.Hashids(salt=HASHID_FIELD_SALT)
        super().setUp()

    def tearDown(self):
        super().tearDown()
