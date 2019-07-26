from bottle import route, run, template, static_file, get, post, delete, request
from sys import argv
import json
import pymysql

connection = pymysql.connect(host='localhost', user='root', password='root', db='bootcamp', charset='utf8', cursorclass=pymysql.cursors.DictCursor, autocommit=True)

@get('/admin')
def admin_portal():
	return template("pages/admin.html")

@get('/')
def index():
    return template("index.html")

@post('/category')
def add_category():
  result = {}
  category_name = request.forms.get("name")
  if not category_name:
    result['STATUS'] = 'ERROR'
    result['CODE'] = 400
    result['MSG'] = 'Name parameter is missing'
  else:
    sql = "INSERT INTO Categories (name) VALUES ('%s')" % category_name
    if_exists = "SELECT * FROM Categories WHERE name = '%s'" % category_name
    with connection.cursor() as cursor:
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
      finally:
        return json.dumps(result)
    


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


run(host='localhost', port=7000)
