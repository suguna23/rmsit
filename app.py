from flask import Flask
from flask_mysqldb import MySQL
from flask import Flask, flash, redirect, render_template, request, session, abort
from flask_mail import Mail, Message
import os
from datetime import datetime
import datetime

app = Flask(__name__,static_url_path='/static')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'vendor'
mysql = MySQL(app)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME='sugunaprabu23@gmail.com',
	MAIL_PASSWORD='saattvik@23'
	)
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('indexmain.html')

@app.route('/homemain', methods=['GET', 'POST'])
def homemain():
    return render_template('indexmain.html')

@app.route('/product', methods=['GET', 'POST'])
def product():
    return render_template('addproduct.html')

@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    return render_template('addproduct.html')

@app.route('/newproduct', methods=['GET', 'POST'])
def newproduct():
  try:
        if request.method == "POST":
            details = request.form
            vname=details['vname']
            catg=details['catg']
            prname  = details['pname']

            comp=details['cname']
            qty=details['qty']
            
            unit=details['unit']
            price=details['price'] 
            purdate = details['ppurdate']
            pex=details['pexdate']
            c = mysql.connection.cursor()
            c.execute("""INSERT INTO product(vname,cat,prname,comp,qty,unit,price,purdate,expirydate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,         
             %s)""",(vname,catg,prname,comp,qty,unit,price,purdate,pex))
            mysql.connection.commit()
            print("Thanks for registering!")
            c.close()

            session['pname'] = prname
            return addproduct()
              
        return addproduct()

  except Exception as e:
        return(str(e))

@app.route('/updateproduct')
def updateproduct():
 try:
  c=mysql.connection.cursor()
  c.execute("SELECT pid from product")
  data = c.fetchall()
  c.close()
  return render_template("updateproduct.html", data=data)

 except Exception as e:
    return (str(e))

@app.route('/upproduct', methods=['GET', 'POST'])
def upproduct():
 try:
     if request.method == "POST":
        details = request.form
        pid  = details['pid']
        pno=int(pid)
        c = mysql.connection.cursor()
        x = c.execute("SELECT * FROM product WHERE pid = (%s)",(pid,))
        data = c.fetchall()
        c.close()
        return render_template("upproduct.html", data=data)
 except Exception as e:
   return (str(e))

@app.route('/productup', methods=['GET', 'POST'])
def productup():
  try:
        if request.method == "POST":
            details = request.form
            pid=details['pid']
            vname=details['vname']
            catg=details['catg']
            prname  = details['pname']

            comp=details['cname']
            qty=details['qty']
            
            unit=details['unit']
            price=details['price'] 
            purdate = details['ppurdate']
            pex=details['pexdate']
            c = mysql.connection.cursor()
            sql_update_query = """Update product set vname = %s,cat = %s,prname = %s,comp = %s,qty = %s,unit= %s,price= %s,purdate= 
            %s,expirydate= %s where pid = %s"""
            inputData = (vname,catg,prname,comp,qty,unit,price,purdate,pex,pid)
            c.execute(sql_update_query, inputData)
        
            mysql.connection.commit()
            print("Thanks for registering!")
            c.close()
            session['logged_in'] = True
            session['pname'] = prname
            return updateproduct()
              
        return updateproduct()

  except Exception as e:
        return(str(e))

@app.route('/viewproduct')
def viewproduct():
 try:
  c=mysql.connection.cursor()
  c.execute("SELECT * from product")
  data = c.fetchall()
  c.close()
  return render_template("productde.html", data=data)

 except Exception as e:
    return (str(e))

@app.route('/delete')
def delete():
  return render_template("Delete.html")

@app.route('/deletep')
def deletep():
  return render_template("Deletep.html")

@app.route('/deleteproduct', methods=['GET', 'POST'])
def deleteproduct():
 try:
     if request.method == "POST":
        details = request.form
        pid  = details['id']
        pno=int(pid)
        c = mysql.connection.cursor()
        x = c.execute("SELECT * FROM product WHERE pid = (%s)",(pid,))
        data = c.fetchall()
        mysql.connection.commit()
        c.close()
        return render_template("deleteproduct.html", data=data)
 except Exception as e:
   return (str(e))

@app.route('/deletepr', methods=['GET', 'POST'])
def deletepr():
 try:
     if request.method == "POST":
        details = request.form
        pid  = details['pid']
        c = mysql.connection.cursor()
        x = c.execute("DELETE FROM product WHERE pid = (%s)",(pid,))
        mysql.connection.commit()
        c.close()
        return viewproduct()


 except Exception as e:
   return (str(e))

@app.route('/Deleten')
def Deleten():
  return render_template("Deleten.html")

@app.route('/deletebyname', methods=['GET', 'POST'])
def deletebyname():
 try:
  if request.method == "POST":
     details = request.form
     pname  = details['pname']
     c=mysql.connection.cursor()
     c.execute("SELECT * FROM product WHERE prname LIKE %s", ("%" + pname + "%",) )
     data = c.fetchall()
     c.close()
     return render_template("deletebyname.html", data=data)

 except Exception as e:
    return (str(e))

@app.route('/vendorreg')
def vendorreg():
  return render_template("vendorreg.html")

@app.route('/updatevendor')
def updatevendor():
 try:
  c=mysql.connection.cursor()
  c.execute("SELECT vid from vendor")
  data = c.fetchall()
  c.close()
  return render_template("updatevendor.html", data=data)

 except Exception as e:
    return (str(e))


@app.route('/allvendordetails')
def allvendordetails():
 try:
  c=mysql.connection.cursor()
  c.execute("SELECT * from vendor")
  data = c.fetchall()
  c.close()
  return render_template("allvendordetails.html", data=data)

 except Exception as e:
    return (str(e))



@app.route('/vendorre', methods=['GET', 'POST'])
def vendorre():
  try:
        if request.method == "POST":
            details = request.form
            vname=details['vname']
            comp=details['comp']
            address  = details['address']

            email=details['email']
            cno=details['cno']
            
            accno=details['accno']
            dop=details['dop'] 
            c = mysql.connection.cursor()
            c.execute("""INSERT INTO vendor(vname,comp,address,email,cno,accno,dop) VALUES (%s,%s,%s,%s,%s,%s,   
             %s)""",(vname,comp,address,email,cno,accno,dop))
            mysql.connection.commit()
            print("Thanks for registering!")
            c.close()
            session['logged_in'] = True
            session['vname'] = vname
            return vendorreg()
              
        return vendorreg()

  except Exception as e:
        return(str(e))

@app.route('/vendorup', methods=['GET', 'POST'])
def vendorup():
 try:
     if request.method == "POST":
        details = request.form
        vidn  = details['vid']
        vno=int(vidn)
        c = mysql.connection.cursor()
        x = c.execute("SELECT * FROM vendor WHERE vid = (%s)",(vidn,))
        data = c.fetchall()
        c.close()
        return render_template("vendorup.html", data=data)
 except Exception as e:
   return (str(e))

@app.route('/vendoru', methods=['GET', 'POST'])
def vendoru():
  try:
        if request.method == "POST":
            details = request.form
            vid=details['vid']
            vname=details['vname']
            comp=details['comp']
            addr=details['addr']
            email=details['email']
            cno=details['cno']     
            accno=details['accno']
            dop=details['date'] 
            c = mysql.connection.cursor()
            sql_update_query = """Update vendor set vname = %s,comp = %s,address = %s,email = %s,cno = %s,accno= %s,dop = %s where vid = %s"""
            inputData = (vname,comp,addr,email,cno,accno,dop,vid)
            c.execute(sql_update_query, inputData)
            mysql.connection.commit()
            print("Thanks for registering!")
            c.close()
            session['logged_in'] = True
            session['vname'] = vname
            return updatevendor()
           
        return updatevendor()

  except Exception as e:
        return(str(e))
@app.route('/customerreg')
def customerreg():
  return render_template("customerreg.html")

@app.route('/customer', methods=['GET', 'POST'])
def customer():
  try:
        if request.method == "POST":
            details = request.form
            fname=details['firstname']
            lname=details['lastname']
            email  = details['email']

            zipc=details['zip']
            
            comp=details['compname']
            cno=details['cno']
            buy=details['buyser'] 
            fave=details['fave']
            notify=details['notify']
            c = mysql.connection.cursor()
            c.execute("""INSERT INTO customer(fname,lname,email,zip,uname,cno,buy,tech,notify) VALUES (%s,%s,%s,%s,%s,%s,   
             %s,%s,%s)""",(fname,lname,email,zipc,comp,cno,buy,fave,notify))
            mysql.connection.commit()
            print("Thanks for registering!")
            c.close()
            session['logged_in'] = True
            session['fname'] = fname
            return customerreg()
              
        return customerreg()

  except Exception as e:
        return(str(e))

@app.route('/updatecustomer')
def updatecustomer():
 try:
  c=mysql.connection.cursor()
  c.execute("SELECT * from customer")
  data = c.fetchall()
  c.close()
  return render_template("updatecustomer.html", data=data)
 except Exception as e:
    return (str(e))

@app.route('/customerup', methods=['GET', 'POST'])
def customerup():
 try:
     if request.method == "POST":
        details = request.form
        cname  = details['cname']
        s=cname.split(",")
        cn=s[0]
        cna=s[1]
        c = mysql.connection.cursor()
        x = c.execute("SELECT * from customer where fname = (%s) and uname = (%s) ",(cn,cna,))
        data = c.fetchall()
        c.close()
        return render_template("customerup.html", data=data)
 except Exception as e:
   return (str(e))

@app.route('/customeru', methods=['GET', 'POST'])
def customeru():
  try:
        if request.method == "POST":
            details = request.form
            cid=details['cid']
            fname=details['fname']
            lname=details['lname']
            email  = details['email']

            zipc=details['zip']
            
            comp=details['uname']
            cno=details['cno']
            buy=details['buy'] 
            fave=details['tech']
            notify=details['notify']
            c = mysql.connection.cursor()
            sql_update_query = """Update customer set fname = %s,lname = %s,email = %s,zip = %s,uname = %s,cno = %s,buy = %s,tech = %s,notify 
                                = %s where cid = %s"""
            inputData = (fname,lname,email,zipc,comp,cno,buy,fave,notify,cid)
            c.execute(sql_update_query, inputData)
            mysql.connection.commit()
            print("Thanks for registering!")
            c.close()
            session['logged_in'] = True
            session['fname'] = fname
            return updatecustomer()

  except Exception as e:
        return(str(e))

@app.route('/custdetails')
def custdetails():
 try:
  c=mysql.connection.cursor()
  c.execute("SELECT * from customer")
  data = c.fetchall()
  c.close()
  return render_template("custdetails.html", data=data)

 except Exception as e:
    return (str(e))

@app.route('/deletecustomer', methods=['GET', 'POST'])
def deletecustomer():
 try:
  c=mysql.connection.cursor()
  c.execute("SELECT * from customer")
  data = c.fetchall()
  c.close()
  return render_template("deletecustomer.html", data=data)

 except Exception as e:
    return (str(e))

@app.route('/deletecus', methods=['GET', 'POST'])
def deletecus():
 try:
     if request.method == "POST":
        details = request.form
        cid  = details['id']
        c = mysql.connection.cursor()
        x = c.execute("DELETE FROM customer WHERE cid = (%s)",(cid,))
        mysql.connection.commit()
        c.close()
        return deletecustomer()
 except Exception as e:
   return (str(e))

@app.route('/custbuy')
def custbuy():
 try:
  c=mysql.connection.cursor()
  c.execute("SELECT * from product")
  data = c.fetchall()
  c.close()
  return render_template("buyproduct.html", data=data)

 except Exception as e:
    return (str(e))

@app.route('/custprlist')
def custprlist():
 try:
  c=mysql.connection.cursor()
  c.execute("SELECT * from customer")
  data = c.fetchall()
  c.close()
  return render_template("cuproduct.html", data=data)

 except Exception as e:
    return (str(e))

@app.route('/customerproduct')
def customerproduct():
  return render_template("customerproduct.html")

@app.route('/custproduct', methods=['GET', 'POST'])
def custproduct():
 try:
     if request.method == "POST":
        details = request.form
        pid  = details['pid']
        c = mysql.connection.cursor()
        ca = mysql.connection.cursor()
        x = c.execute("SELECT * from product where pid = (%s) ",(pid,))
        data = c.fetchall()
        c.close()
        y=ca.execute("select * from customer")
        da=ca.fetchall()
        ca.close()
        return render_template("custproduct.html", data=data,da=da)

 except Exception as e:
   return (str(e))

@app.route('/custpr', methods=['GET', 'POST'])
def custpr():
  try:
        if request.method == "POST":
            details = request.form
            pid=details['pid']
            cid=details['cid']
            catg = details['catg']

            pname=details['pname']
            cname=details['cname']
            qty=details['qty']
            
            unit=details['unit']
            price=details['price'] 
            purdate = details['ppurdate']
            pex=details['pexdate']
            c = mysql.connection.cursor()
            c.execute("""INSERT INTO custproduct(pid,cid,category,pname,cname,quantity,unitprice,totalprice,purchasedate,expirydate) VALUES  
                     (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(pid,cid,catg,pname,cname,qty,unit,price,purdate,pex))
            mysql.connection.commit()
            print("Thanks for registering!")
            c.close()
            session['logged_in'] = True
            session['pname'] = pname
            return addproduct()

  except Exception as e:
        return(str(e))

@app.route('/custproductdetails', methods=['GET', 'POST'])
def custproductdetails():
 try:
     if request.method == "POST":
        details = request.form
        cid  = details['id']

        c = mysql.connection.cursor()
        x = c.execute("SELECT * FROM custproduct WHERE cid = (%s)",(cid,))
        data = c.fetchall()
        c.close()
        return render_template("custproductdetails.html", data=data)
 except Exception as e:
   return (str(e))

@app.route('/rproductdetails', methods=['GET', 'POST'])
def rproductdetails():
 try:
     if request.method == "POST":
        details = request.form
        dur  = details['dur']
        c = mysql.connection.cursor()
        if dur=="one":
            x = c.execute("SELECT * from product where DATEDIFF(expirydate,NOW())<30")
        elif dur=="three":
            x = c.execute("SELECT * from product where DATEDIFF(expirydate,NOW())<90")
        elif dur=="six":
            x = c.execute("SELECT * from product where DATEDIFF(expirydate,NOW())<180")
        elif dur=="nine":
            x = c.execute("SELECT * from product where DATEDIFF(expirydate,NOW())<270")
        elif dur=="tweleve":
            x = c.execute("SELECT * from product where DATEDIFF(expirydate,NOW())<365")
      
        data = c.fetchall()
        c.close()
        session['logged_in'] = True
        session['dur'] = dur
        return render_template("rproductdetails.html",data=data)
 except Exception as e:
   return (str(e))

@app.route('/sendmail', methods=['GET', 'POST'])
def sendmail():
 try:
        
        c = mysql.connection.cursor()

        dura=session['dur']
     
        if dura=="one":
            x = c.execute("SELECT * from product where DATEDIFF(expirydate,NOW())<30")
        elif dura=="three":
            x = c.execute("SELECT * from product where DATEDIFF(expirydate,NOW())<90")
        elif dura=="six":
            x = c.execute("SELECT * from product where DATEDIFF(expirydate,NOW())<180")
        elif dura=="nine":
            x = c.execute("SELECT * from product where DATEDIFF(expirydate,NOW())<270")
        elif dura=="tweleve":
            x = c.execute("SELECT * from product where DATEDIFF(expirydate,NOW())<365")
      
        data = c.fetchall()

        for dx in data:
           msg = Message("Product Renewal",sender="sugunaprabu23@gmail.com",
                 recipients=["suguna777@gmail.com","suguna.p@theitman.in","sugunaprabu23@gmail.com"])
           pid=str(dx[0])
           da=str(dx[9])
           msg.body = dx[3] + " is expired please renewe it with product code as " + pid +" on before "+ da      
           mail.send(msg)        
        c.close()
        return render_template("renewal.html",data=data)
 except Exception as e:
   return (str(e))



@app.route('/renewal')
def renewal():
  return render_template("renewal.html")


if __name__ == "__main__":
  app.secret_key = os.urandom(12)
  app.run(debug=True,host='0.0.0.0', port=4000)

  
