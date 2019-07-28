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
        if not cursor.fetchone():
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
    result = {}
    sql = "INSERT INTO `Products` (`title`, `desc`, `price`, `img_url`, `category`, `favorite`) VALUES ('%s', '%s', %d, '%s', %d, %s)" % (product['title'], product['desc'], int(product['price']), product['img_url'], int(product['category']), product['favorite'])
    if_exists_category = "SELECT id FROM Categories"
    with self._connection.cursor() as cursor:
        try:
          cursor.execute(if_exists_category)
          list_ids = [x['id'] for x in cursor.fetchall()]
          if not int(product['category']) in list_ids:
            result['STATUS'] = 'ERROR'
            result['CODE'] = 404
            result['MSG'] = 'Category not found'
          else:
            cursor.execute(sql)
            result['STATUS'] = 'SUCCESS'
            result['CODE'] = 201
            result['PRODUCT_ID'] = cursor.lastrowid
        except:
          result['STATUS'] = 'ERROR'
          result['CODE'] = 500
          result['MSG'] = 'Internal server error'
          
    return result

  def update_product(self, product):
    # product is a dictionary containing the keys: id (int), title (str), desc (str), price (int), img_url (str), category (str), favorite (bool)
    result = {}
    # diff =  { k : dict2[k] for k in dict2 if dict2[k] != dict1[k] }
    sql = "UPDATE Products SET title = '%s', description = '%s', price = %d, img_url = '%s', category = %d, favorite = %s WHERE id = %d" % (product['title'], product['desc'], int(product['price']), product['img_url'], int(product['category']), product['favorite'], int(product['id']))
    print(sql)
    with self._connection.cursor() as cursor:
      try:
        cursor.execute(sql)
        result['STATUS'] = 'SUCCESS'
        result['CODE'] = 201
        result['PRODUCT_ID'] = cursor.lastrowid
      except:
        result['STATUS'] = 'ERROR'
        result['CODE'] = 500
        result['MSG'] = 'Internal server error'
    return result

  def get_product(self, product_id):
    result = {}
    sql = "SELECT * FROM Products WHERE id = %d" % product_id
    with self._connection.cursor() as cursor:
      try:
        cursor.execute(sql)
        findings = cursor.fetchone()
        if not findings:
          result['STATUS'] = 'ERROR'
          result['CODE'] = 404
          result['MSG'] = 'Product not found'
        else:
          result['STATUS'] = 'SUCCESS'
          result['CODE'] = 200
          result['PRODUCT'] = findings
      except:
        result['STATUS'] = 'ERROR'
        result['CODE'] = 500
        result['MSG'] = 'Internal server error'
      return result

  def list_all_products(self):
    result = {}
    sql = "SELECT * FROM Products"
    with self._connection.cursor() as cursor:
      try:
        cursor.execute(sql)
        result['PRODUCTS'] = cursor.fetchall()
        result['STATUS'] = 'SUCCESS'
        result['CODE'] = 200
      except:
        result['STATUS'] = 'ERROR'
        result['CODE'] = 500
        result['MSG'] = "Internal server error"
    return result

  def list_products_by_category(self, category_id):
    result = {}
    sql = "SELECT * FROM Products WHERE category = %d" % int(category_id)
    if_exists = "SELECT * FROM Categories WHERE id = %d" % int(category_id)
    with self._connection.cursor() as cursor:
      cursor.execute(if_exists)
      if not cursor.fetchone():
        result['STATUS'] = 'ERROR'
        result['CODE'] = 404
        result['MSG'] = 'Category not found'
      else:
        try:
          cursor.execute(sql)
          result['STATUS'] = 'SUCCESS'
          result['CODE'] = 200
          result['PRODUCTS'] = cursor.fetchall()
        except:
          result['STATUS'] = 'ERROR'
          result['CODE'] = 500
          result['MSG'] = 'Internal server error'
    return result


  def delete_product(self, product_id):
    result = {}
    sql = "DELETE FROM Products WHERE id = %d" % int(product_id)
    if_exists = "SELECT * FROM Products WHERE id = %d" % int(product_id)
    with self._connection.cursor() as cursor:
      cursor.execute(if_exists)
      if not cursor.fetchone():
        result['STATUS'] = 'ERROR'
        result['CODE'] = 404
        result['MSG'] = 'Product not found'
      else:
        try:
          cursor.execute(sql)
          result['STATUS'] = 'SUCCESS'
          result['CODE'] = 201
        except:
          result['STATUS'] = 'ERROR'
          result['CODE'] = 500
          result['MSG'] = 'Internal server error'
    return result