from .base_database_adapter import BaseDatabaseAdapter
import pymysql
import json
from bottle import request

class MySqlAdapter(BaseDatabaseAdapter):
  def __init__(self):
    self._connection = pymysql.connect(host='localhost', user='root', password='root', db='bootcamp', charset='utf8', cursorclass=pymysql.cursors.DictCursor, autocommit=True)

  def run(self):
    run(host='localhost', port=7000)

  def add_category(self, category_name):
    result = {}
    if not category_name:
      result['STATUS'] = 'ERROR'
      result['CODE'] = 400
      result['MSG'] = 'Name parameter is missing'
    else:
      sql = "INSERT INTO Categories (name) VALUES ('%s')" % category_name
      if_exists = "SELECT * FROM Categories WHERE name = '%s'" % category_name
      with self._connection.cursor() as cursor:
        try:
          cursor.execute(if_exists)
          if cursor.fetchone():
            result['STATUS'] = 'ERROR'
            result['CODE'] = 200
            result['MSG'] = 'Category already exists'
          else:
            cursor.execute(sql)
            result['CAT_ID'] = cursor.lastrowid
            result['STATUS'] = 'SUCCESS'
            result['CODE'] = 201
        except:
          result['STATUS'] = 'ERROR'
          result['CODE'] = 500
          result['MSG'] = 'Internal server error'
    return result

  def delete_category(self, category_id):
    result = {}
    sql = "DELETE FROM Categories WHERE id = %d" % category_id
    if_exists = "SELECT * FROM Categories WHERE id = %d" % category_id
    with self._connection.cursor() as cursor:
      try:
        cursor.execute(if_exists)
        if cursor.fetchone():
          result['STATUS'] = 'ERROR'
          result['CODE'] = 404
          result['MSG'] = 'Category not found'
        else:
          cursor.execute(sql)
          result['STATUS'] = 'SUCCESS'
          result['CODE'] = 201
      except:
        result['STATUS'] = 'ERROR'
        result['CODE'] = 500
        result['MSG'] = 'Internal server error'
    return result

  def list_categories(self):
    result = {}
    sql = "SELECT * FROM Categories"
    with self._connection.cursor() as cursor:
      try:
        cursor.execute(sql)
        result['STATUS'] = 'SUCCESS'
        result['CODE'] = 200
        result['CATEGORIES'] = cursor.fetchall()
      except:
        result['STATUS'] = 'ERROR'
        result['CODE'] = 500
        result['MSG'] = 'Internal server error'
    return result

  def add_product(self, product):
    # product is a dictionary containing the keys: id (int), title (str), desc (str), price (int), img_url (str), category (str), favorite (bool)
    
    pass

  def edit_product(self, product):
    # product is a dictionary containing the keys: id (int), title (str), desc (str), price (int), img_url (str), category (str), favorite (bool)
    pass

  def get_product(self, product_id):
    pass

  def delete_product(self, product_id):
    pass

  def list_all_products(self):
    pass

  def list_products_by_category(self, category):
    pass