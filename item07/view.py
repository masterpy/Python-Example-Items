#!/usr/bin/python

print 'Content-type:text/html\n'

import cgitb;cgitb.enable()

import MySQLdb

conn = MySQLdb.connect(db='usernet',host='127.0.0.1',user='root',passwd='root')
curs = conn.cursor()

import cgi, sys
form = cgi.FieldStorage()
id = form.getvalue('id')

print '''
<html>
  <head>
    <title>View Message</title>
  </head>
  <body>
    <h1>View Message</h1>
    '''

try: id = int(id)
except:
        print 'Invalid message ID'
        sys.exit()

curs.execute('SELECT * FROM message WHERE id = %i' % id)
rows = curs.fetchall()

if not rows:
        print 'Unknown message ID'
        sys.exit()

row = rows[0]

print '''
<p><b>Subject:</b> %s<br/>
<b>Sender:</b>%s<br/>
<pre>%s</pre>
</p>
<hr/>
<a href='main.cgi'>Back to the main page</a>
|<a href="edit.cgi?reply_to=%s">Reply</a>
</body>
</html>
''' % (row[1],row[2],row[4],row[0])