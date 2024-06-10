# chemicals.py
from utils import UtilityFunctions

class Chemicals():
    """Represents Chemicals"""

    def __init__(self, name, cas_number, product_number, vendor_name, quantity, location, hazard_info):
        # initialize attributes
        pass
    
    @property
    def name(self):
        pass

    @name.setter
    def name(self, name):
        pass
    
    @property
    def cas_number(self):
        pass

    @cas_number.setter
    def cas_number(self, cas_number):
        pass

    @property
    def unique_id(self):
        pass

    @unique_id.setter
    def unique_id(self):
        UtilityFunctions._generate_unique_id
        pass

    @property
    def product_number(self):
        pass

    @product_number.setter
    def product_number(self, product_number):
        pass

    @property
    def vendor_name(self):
        pass

    @vendor_name.setter
    def vendor_name(self, vendor_name):
        pass

    @property
    def quantity(self):
        pass
        
    @staticmethod
    def _parse_quantity(quantity):
        pass

    @quantity.setter
    def quantity(self, quantity):
        pass

    @property
    def hazard_info(self):
        pass

    @hazard_info.setter
    def hazard_info(self, hazard_info):
        pass