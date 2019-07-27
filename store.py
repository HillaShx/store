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
  product_details = {'title': request.forms.get('title'), 'desc': request.forms.get('desc'), 'favorite': request.forms.get('favorite'), 'price': request.forms.get('price'), 'img_url': request.forms.get('img_url'), 'category': request.forms.get('category')}
  if request.forms.get('id'):
    product_details['id'] = request.forms.get('id')
    sql = "INSERT INTO Products (title, description, price, image_url,"

# update_product
# @post
# finding the different value
# { k : dict2[k] for k in dict2 if dict2[k] != dict1[k] }

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
