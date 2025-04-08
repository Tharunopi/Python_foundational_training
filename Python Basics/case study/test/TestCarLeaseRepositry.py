import unittest, sys

sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\case study")

from entity.customer import Customer
from entity.lease import Lease
from entity.payment import Payment
from entity.vechicle import Vechicle

from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl

class TestCarLeaseRepositry(unittest.TestCase):
    