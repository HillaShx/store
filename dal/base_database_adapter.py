from abc import ABC, abstractmethod


class BaseDatabaseAdapter(ABC):
  
  @abstractmethod
  def add_category(self):
    pass

  @abstractmethod
  def delete_category(self, category_id):
    pass

  @abstractmethod
  def list_categories(self):
    pass

  @abstractmethod
  def add_product(self, product):
    # product is a dictionary containing the keys: id (int), title (str), desc (str), price (int), img_url (str), category (str), favorite (bool)
    pass

  @abstractmethod
  def edit_product(self, product):
    # product is a dictionary containing the keys: id (int), title (str), desc (str), price (int), img_url (str), category (str), favorite (bool)
    pass

  @abstractmethod
  def get_product(self, product_id):
    pass

  @abstractmethod
  def delete_product(self, product_id):
    pass

  @abstractmethod
  def list_all_products(self):
    pass

  @abstractmethod
  def list_products_by_category(self, category):
    pass