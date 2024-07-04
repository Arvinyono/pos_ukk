from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
#from flaskext.mysql import MySQL
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
#koneksi
app.secret_key = 'bebasapasaja'
app.config['MYSQL_HOST'] ='127.0.0.1'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='skafa1'
mysql = MySQL(app)

#index
@app.route('/')
def index():
    if 'loggedin' in session:
        return render_template('index.html')
    flash('Harap Login dulu','danger')
    return redirect(url_for('login'))

#registrasi
@app.route('/registrasi', methods=('GET','POST'))
def registrasi():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        level = request.form['level']

        #cek username atau email
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_users WHERE username=%s OR email=%s',(username, email, ))
        akun = cursor.fetchone()
        if akun is None:
            cursor.execute('INSERT INTO tb_users VALUES (NULL, %s, %s, %s, %s)', (username, email, generate_password_hash(password), level))
            mysql.connection.commit()
            flash('Registrasi Berhasil','success')
        else :
            flash('Username atau email sudah ada','danger')
    return render_template('registrasi.html')




#login
@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        #cek data username
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM tb_users WHERE email=%s',(email, ))
        akun = cursor.fetchone()
        if akun is None:
            flash('Login Gagal, Cek Username Anda','danger')
        elif not check_password_hash(akun[3], password):
            flash('Login gagal, Cek Password Anda', 'danger')
        else:
            session['loggedin'] = True
            session['username'] = akun[1]
            session['level'] = akun[4]
            return redirect(url_for('index'))
    return render_template('login.html')


# UNTUK KONEKSI KE SETIAP MENU
@app.route('/penjualana')
def penjualana():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM tb_barang")
    data = cur.fetchall()
    cur.close()


    return render_template('penjualana.html', tb_barang=data )

@app.route('/penjualan')
def penjualan():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM tb_barang")
    data = cur.fetchall()
    cur.close()


    return render_template('penjualan.html', tb_barang=data )

@app.route('/pelanggan')
def pelanggan():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tb_pelanggan")
    data = cur.fetchall()
    cur.close()
    
    return render_template('pelanggan.html', tb_pelanggan=data)

@app.route('/suplier')
def suplier():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tb_suplier")
    data = cur.fetchall()
    cur.close()
    
    return render_template('suplier.html', tb_suplier=data)

@app.route('/pengeluaran')
def pengeluaran():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tb_pengeluaran")
    data = cur.fetchall()
    cur.close()
    
    return render_template('pengeluaran.html', tb_pengeluaran=data)

@app.route('/laporan')
def laporan():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tb_laporan")
    data = cur.fetchall()
    cur.close()
    
    return render_template('laporan.html', tb_laporan=data)



# CODINGAN BAGIAN INSERTS
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        namaBarang = request.form['namaBarang']
        kategori = request.form['kategori']
        hargaBeli = request.form['hargaBeli']
        hargaJual = request.form['hargaJual']
        stok = request.form['stok']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tb_barang (namaBarang, kategori, hargaBeli, hargaJual, stok) VALUES (%s, %s, %s, %s, %s)", (namaBarang, kategori, hargaBeli, hargaJual, stok))
        mysql.connection.commit()
        return redirect(url_for('penjualana'))
    
@app.route('/inserte', methods = ['POST'])
def inserte():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        noPelanggan = request.form['noPelanggan']
        name = request.form['name']
        alamat = request.form['alamat']
        telp = request.form['telp']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tb_pelanggan (noPelanggan, name, alamat, telp) VALUES (%s, %s, %s, %s)", (noPelanggan, name, alamat, telp))
        mysql.connection.commit()
        return redirect(url_for('inserte'))

@app.route('/insertes', methods = ['POST'])
def insertes():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        idSuplier = request.form['idSuplier']
        namaSuplier = request.form['namaSuplier']
        alamat = request.form['alamat']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tb_suplier (idSuplier, namaSuplier, alamat, phone) VALUES (%s, %s, %s, %s)", (idSuplier, namaSuplier, alamat, phone))
        mysql.connection.commit()
        return redirect(url_for('insertes'))
    

@app.route('/pengeluaran1', methods = ['POST'])
def pengeluaran1():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        idPengeluaran = request.form['idPengeluaran']
        pengeluaran = request.form['pengeluaran']
        nominal = request.form['nominal']
        status = request.form['status']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tb_pengeluaran (idPengeluaran, pengeluaran, nominal, status) VALUES (%s, %s, %s, %s)", (idPengeluaran, pengeluaran, nominal, status))
        mysql.connection.commit()
        return redirect(url_for('pengeluaran'))



# CODINGAN BAGIAN DELETE
@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tb_barang WHERE idBarang=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('penjualana'))


@app.route('/delete_pelanggan/<string:id_data_pelanggan>', methods = ['GET'])
def delete_pelanggan(id_data_pelanggan):
    flash("Record Has Been Deleted Successfully")
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM tb_pelanggan WHERE idPelanggan=%s", (id_data_pelanggan,))
    mysql.connection.commit()
    return redirect(url_for('pelanggan'))

@app.route('/delete_suplier/<string:id_data_suplier>', methods = ['GET'])
def delete_suplier(id_data_suplier):
    flash("Record Has Been Deleted Successfully")
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM tb_suplier WHERE idSuplier=%s", (id_data_suplier,))
    mysql.connection.commit()
    return redirect(url_for('suplier'))


@app.route('/delete_pengeluaran/<string:id_data_pengeluaran>', methods = ['GET'])
def delete_pengeluaran(id_data_pengeluaran):
    flash("Record Has Been Deleted Successfully")
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM tb_pengeluaran WHERE idPengeluaran=%s", (id_data_pengeluaran,))
    mysql.connection.commit()
    return redirect(url_for('pengeluaran'))



# CODINGAN BAGIAN UPDATE
@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['idBarang']
        namaBarang = request.form['namaBarang']
        kategori = request.form['kategori']
        hargaBeli = request.form['hargaBeli']
        hargaJual = request.form['hargaJual']
        stok = request.form['stok']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE tb_barang
               SET namaBarang=%s, kategori=%s, hargaBeli=%s, hargaJual=%s, stok=%s
               WHERE idBarang=%s
            """, (namaBarang, kategori, hargaBeli, hargaJual, stok, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('penjualana'))


@app.route('/update_pelanggan',methods=['POST','GET'])
def update_pelanggan():

    if request.method == 'POST':
        id_data_update_pelanggan = request.form['idPelanggan']
        noPelanggan = request.form['noPelanggan']
        name = request.form['name']
        alamat = request.form['alamat']
        telp = request.form['telp']

        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE tb_pelanggan
               SET noPelanggan=%s, name=%s, alamat=%s, telp=%s
               WHERE idPelanggan=%s
            """, (noPelanggan, name, alamat, telp, id_data_update_pelanggan))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('pelanggan'))

@app.route('/update_suplier',methods=['POST','GET'])
def update_suplier():

    if request.method == 'POST':
        id_data_update_suplier = request.form['idSuplier']
        idSuplier = request.form['idSuplier']
        namaSuplier = request.form['namaSuplier']
        alamat = request.form['alamat']
        phone = request.form['phone']

        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE tb_suplier
               SET idSuplier=%s, namaSuplier=%s, alamat=%s, phone=%s
               WHERE idSuplier=%s
            """, (idSuplier, namaSuplier, alamat, phone, id_data_update_suplier))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('suplier'))


@app.route('/update_pengeluaran',methods=['POST','GET'])
def update_pengeluaran():

    if request.method == 'POST':
        id_data_update_pengeluaran = request.form['idPengeluaran']
        idPengeluaran = request.form['idPengeluaran']
        pengeluaran = request.form['pengeluaran']
        nominal = request.form['nominal']
        status = request.form['status']

        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE tb_pengeluaran
               SET idPengeluaran=%s, pengeluaran=%s, nominal=%s, status=%s
               WHERE idPengeluaran=%s
            """, (idPengeluaran, pengeluaran, nominal, status))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('pengeluaran'))
    
@app.route('/search')
def search():
    cur = mysql.connection.cursor()
    search_query = request.args.get('search', '')  # mendapatkan query pencarian dari form
    if search_query:
        cur.execute("SELECT * FROM tb_barang WHERE namaBarang LIKE %s", ('%' + search_query + '%',))
    else:
        cur.execute("SELECT * FROM tb_barang")
    data = cur.fetchall()
    cur.close()
    return render_template('penjualana.html', tb_barang=data)


@app.route('/tambah_ke_list/<int:id_barang>')
def tambah_ke_list(id_barang):
    # Logika untuk menambahkan barang ke list, misalnya menyimpannya di session atau database
    flash("Barang ditambahkan ke list")
    return redirect(url_for('penjualan'))

@app.route('/search_barang', methods=['GET'])
def search_barang():
    query = request.args.get('q', '')  # mendapatkan query dari parameter URL
    cur = mysql.connection.cursor()
    cur.execute("SELECT idBarang, namaBarang FROM tb_barang WHERE namaBarang LIKE %s", ('%' + query + '%',))
    barang_list = cur.fetchall()
    cur.close()
    return jsonify(barang_list)



@app.route('/search_pelanggan', methods=['GET'])
def search_pelanggan():
    search_query = request.args.get('search', '')  # mendapatkan query pencarian dari form
    cur = mysql.connection.cursor()
    if search_query:
        cur.execute("SELECT * FROM tb_pelanggan WHERE name LIKE %s", ('%' + search_query + '%',))
    else:
        cur.execute("SELECT * FROM tb_pelanggan")
    data = cur.fetchall()
    cur.close()
    return render_template('pelanggan.html', tb_pelanggan=data)


#logout
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('level', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=5005)
    
