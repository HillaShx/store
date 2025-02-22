from bottle import route, run, template, static_file, get, post, delete, request
from sys import argv
import json
import pymysql
from dal.mysql_db_adapter import MySqlAdapter

connection = pymysql.connect(host='localhost', user='root', password='root', db='bootcamp', charset='utf8', cursorclass=pymysql.cursors.DictCursor, autocommit=True)

_db_adapter = MySqlAdapter()

@get('/admin')
def admin_portal():
  return template("pages/admin.html")

@get('/')
def index():
  return template("index.html")

@post('/category')
def add_category():
  category_name = request.forms.get("name")
  category_details = _db_adapter.add_category(category_name)
  return json.dumps(category_details)

@delete('/category/<id:int>')
def delete_category(id):
  return json.dumps(_db_adapter.delete_category(id))

@get('/categories')
def list_categories():
  return json.dumps(_db_adapter.list_categories())
  
@post('/product')
def add_edit_product():
  # {'category': '1', 'title': 'jklj', 'desc': 'ghht', 'price': '90', 'img_url': 'jklj', 'id': ''}
  product_details = dict(request.forms)
  if 'favorite' in product_details.keys():
    product_details['favorite'] = True
  else:
    product_details['favorite'] = False
  if product_details['id']:
    return _db_adapter.update_product(product_details)
  return json.dumps(_db_adapter.add_product(product_details))

@get('/product/<product_id:int>')
def get_product(product_id):
  return json.dumps(_db_adapter.get_product(product_id))

@get('/products')
def get_all_products():
  return json.dumps(_db_adapter.list_all_products())

@get('/category/<category_id:int>/products')
def get_products_by_category(category_id):
  return json.dumps(_db_adapter.list_products_by_category(category_id))

@delete('/product/<product_id:int>')
def delete_product(product_id):
  return json.dumps(_db_adapter.delete_product(product_id))



@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


if __name__ == "__main__":
  run(host='localhost', port=7001)
