from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash, generate_password_hash

class Config:
    SECRET_KEY = 'bebasapasaja'
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'skafa1'

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config.from_object(Config)
        self.mysql = MySQL(self.app)
        self.register_routes()

    def register_routes(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/registrasi', 'registrasi', self.registrasi, methods=['GET', 'POST'])
        self.app.add_url_rule('/login', 'login', self.login, methods=['GET', 'POST'])
        self.app.add_url_rule('/penjualana', 'penjualana', self.penjualana)
        self.app.add_url_rule('/penjualan', 'penjualan', self.penjualan)
        self.app.add_url_rule('/pelanggan', 'pelanggan', self.pelanggan)
        self.app.add_url_rule('/suplier', 'suplier', self.suplier)
        self.app.add_url_rule('/pengeluaran', 'pengeluaran', self.pengeluaran)
        self.app.add_url_rule('/laporan', 'laporan', self.laporan)
        self.app.add_url_rule('/insert', 'insert', self.insert, methods=['POST'])
        self.app.add_url_rule('/inserte', 'inserte', self.inserte, methods=['POST'])
        self.app.add_url_rule('/insertes', 'insertes', self.insertes, methods=['POST'])
        self.app.add_url_rule('/pengeluaran1', 'pengeluaran1', self.pengeluaran1, methods=['POST'])
        self.app.add_url_rule('/delete/<string:id_data>', 'delete', self.delete, methods=['GET'])
        self.app.add_url_rule('/delete_pelanggan/<string:id_data_pelanggan>', 'delete_pelanggan', self.delete_pelanggan, methods=['GET'])
        self.app.add_url_rule('/delete_suplier/<string:id_data_suplier>', 'delete_suplier', self.delete_suplier, methods=['GET'])
        self.app.add_url_rule('/delete_pengeluaran/<string:id_data_pengeluaran>', 'delete_pengeluaran', self.delete_pengeluaran, methods=['GET'])
        self.app.add_url_rule('/update', 'update', self.update, methods=['POST', 'GET'])
        self.app.add_url_rule('/update_pelanggan', 'update_pelanggan', self.update_pelanggan, methods=['POST', 'GET'])
        self.app.add_url_rule('/update_suplier', 'update_suplier', self.update_suplier, methods=['POST', 'GET'])
        self.app.add_url_rule('/update_pengeluaran', 'update_pengeluaran', self.update_pengeluaran, methods=['POST', 'GET'])
        self.app.add_url_rule('/search', 'search', self.search)
        self.app.add_url_rule('/tambah_ke_list/<int:id_barang>', 'tambah_ke_list', self.tambah_ke_list)
        self.app.add_url_rule('/search_barang', 'search_barang', self.search_barang, methods=['GET'])
        self.app.add_url_rule('/search_pelanggan', 'search_pelanggan', self.search_pelanggan, methods=['GET'])
        self.app.add_url_rule('/logout', 'logout', self.logout)

    def index(self):
        if 'loggedin' in session:
            return render_template('index.html')
        flash('Harap Login dulu', 'danger')
        return redirect(url_for('login'))

    def registrasi(self):
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            level = request.form['level']

            cursor = self.mysql.connection.cursor()
            cursor.execute('SELECT * FROM tb_users WHERE username=%s OR email=%s', (username, email,))
            akun = cursor.fetchone()
            if akun is None:
                cursor.execute('INSERT INTO tb_users VALUES (NULL, %s, %s, %s, %s)', (username, email, generate_password_hash(password), level))
                self.mysql.connection.commit()
                flash('Registrasi Berhasil', 'success')
            else:
                flash('Username atau email sudah ada', 'danger')
        return render_template('registrasi.html')

    def login(self):
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            cursor = self.mysql.connection.cursor()
            cursor.execute('SELECT * FROM tb_users WHERE email=%s', (email,))
            akun = cursor.fetchone()
            if akun is None:
                flash('Login Gagal, Cek Username Anda', 'danger')
            elif not check_password_hash(akun[3], password):
                flash('Login gagal, Cek Password Anda', 'danger')
            else:
                session['loggedin'] = True
                session['username'] = akun[1]
                session['level'] = akun[4]
                return redirect(url_for('index'))
        return render_template('login.html')

    def penjualana(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT  * FROM tb_barang")
        data = cur.fetchall()
        cur.close()
        return render_template('penjualana.html', tb_barang=data)

    def penjualan(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT  * FROM tb_barang")
        data = cur.fetchall()
        cur.close()
        return render_template('penjualan.html', tb_barang=data)

    def pelanggan(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM tb_pelanggan")
        data = cur.fetchall()
        cur.close()
        return render_template('pelanggan.html', tb_pelanggan=data)

    def suplier(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM tb_suplier")
        data = cur.fetchall()
        cur.close()
        return render_template('suplier.html', tb_suplier=data)

    def pengeluaran(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM tb_pengeluaran")
        data = cur.fetchall()
        cur.close()
        return render_template('pengeluaran.html', tb_pengeluaran=data)

    def laporan(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM tb_laporan")
        data = cur.fetchall()
        cur.close()
        return render_template('laporan.html', tb_laporan=data)

    def insert(self):
        if request.method == "POST":
            flash("Data Inserted Successfully")
            namaBarang = request.form['namaBarang']
            kategori = request.form['kategori']
            hargaBeli = request.form['hargaBeli']
            hargaJual = request.form['hargaJual']
            stok = request.form['stok']
            cur = self.mysql.connection.cursor()
            cur.execute("INSERT INTO tb_barang (namaBarang, kategori, hargaBeli, hargaJual, stok) VALUES (%s, %s, %s, %s, %s)", (namaBarang, kategori, hargaBeli, hargaJual, stok))
            self.mysql.connection.commit()
            return redirect(url_for('penjualan'))

    def inserte(self):
        if request.method == "POST":
            flash("Data Inserted Successfully")
            namaPelanggan = request.form['namaPelanggan']
            alamat = request.form['alamat']
            noTelp = request.form['noTelp']
            cur = self.mysql.connection.cursor()
            cur.execute("INSERT INTO tb_pelanggan (namaPelanggan, alamat, noTelp) VALUES (%s, %s, %s)", (namaPelanggan, alamat, noTelp))
            self.mysql.connection.commit()
            return redirect(url_for('pelanggan'))

    def insertes(self):
        if request.method == "POST":
            flash("Data Inserted Successfully")
            namaSuplier = request.form['namaSuplier']
            alamat = request.form['alamat']
            noTelp = request.form['noTelp']
            cur = self.mysql.connection.cursor()
            cur.execute("INSERT INTO tb_suplier (namaSuplier, alamat, noTelp) VALUES (%s, %s, %s)", (namaSuplier, alamat, noTelp))
            self.mysql.connection.commit()
            return redirect(url_for('suplier'))

    def pengeluaran1(self):
        if request.method == "POST":
            flash("Data Inserted Successfully")
            namaPengeluaran = request.form['namaPengeluaran']
            jumlah = request.form['jumlah']
            cur = self.mysql.connection.cursor()
            cur.execute("INSERT INTO tb_pengeluaran (namaPengeluaran, jumlah) VALUES (%s, %s)", (namaPengeluaran, jumlah))
            self.mysql.connection.commit()
            return redirect(url_for('pengeluaran'))

    def delete(self, id_data):
        flash("Record Has Been Deleted Successfully")
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM tb_barang WHERE id=%s", (id_data,))
        self.mysql.connection.commit()
        return redirect(url_for('penjualan'))

    def delete_pelanggan(self, id_data_pelanggan):
        flash("Record Has Been Deleted Successfully")
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM tb_pelanggan WHERE id=%s", (id_data_pelanggan,))
        self.mysql.connection.commit()
        return redirect(url_for('pelanggan'))

    def delete_suplier(self, id_data_suplier):
        flash("Record Has Been Deleted Successfully")
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM tb_suplier WHERE id=%s", (id_data_suplier,))
        self.mysql.connection.commit()
        return redirect(url_for('suplier'))

    def delete_pengeluaran(self, id_data_pengeluaran):
        flash("Record Has Been Deleted Successfully")
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM tb_pengeluaran WHERE id=%s", (id_data_pengeluaran,))
        self.mysql.connection.commit()
        return redirect(url_for('pengeluaran'))

    def update(self):
        if request.method == 'POST':
            id_data = request.form['id']
            namaBarang = request.form['namaBarang']
            kategori = request.form['kategori']
            hargaBeli = request.form['hargaBeli']
            hargaJual = request.form['hargaJual']
            stok = request.form['stok']
            cur = self.mysql.connection.cursor()
            cur.execute("""
                UPDATE tb_barang
                SET namaBarang=%s, kategori=%s, hargaBeli=%s, hargaJual=%s, stok=%s
                WHERE id=%s
            """, (namaBarang, kategori, hargaBeli, hargaJual, stok, id_data))
            self.mysql.connection.commit()
            flash("Data Updated Successfully")
            return redirect(url_for('penjualan'))

    def update_pelanggan(self):
        if request.method == 'POST':
            id_data_pelanggan = request.form['id']
            namaPelanggan = request.form['namaPelanggan']
            alamat = request.form['alamat']
            noTelp = request.form['noTelp']
            cur = self.mysql.connection.cursor()
            cur.execute("""
                UPDATE tb_pelanggan
                SET namaPelanggan=%s, alamat=%s, noTelp=%s
                WHERE id=%s
            """, (namaPelanggan, alamat, noTelp, id_data_pelanggan))
            self.mysql.connection.commit()
            flash("Data Updated Successfully")
            return redirect(url_for('pelanggan'))

    def update_suplier(self):
        if request.method == 'POST':
            id_data_suplier = request.form['id']
            namaSuplier = request.form['namaSuplier']
            alamat = request.form['alamat']
            noTelp = request.form['noTelp']
            cur = self.mysql.connection.cursor()
            cur.execute("""
                UPDATE tb_suplier
                SET namaSuplier=%s, alamat=%s, noTelp=%s
                WHERE id=%s
            """, (namaSuplier, alamat, noTelp, id_data_suplier))
            self.mysql.connection.commit()
            flash("Data Updated Successfully")
            return redirect(url_for('suplier'))

    def update_pengeluaran(self):
        if request.method == 'POST':
            id_data_pengeluaran = request.form['id']
            namaPengeluaran = request.form['namaPengeluaran']
            jumlah = request.form['jumlah']
            cur = self.mysql.connection.cursor()
            cur.execute("""
                UPDATE tb_pengeluaran
                SET namaPengeluaran=%s, jumlah=%s
                WHERE id=%s
            """, (namaPengeluaran, jumlah, id_data_pengeluaran))
            self.mysql.connection.commit()
            flash("Data Updated Successfully")
            return redirect(url_for('pengeluaran'))

    def search(self):
        # Implement search functionality
        pass

    def tambah_ke_list(self, id_barang):
        # Implement add to list functionality
        pass

    def search_barang(self):
        # Implement search barang functionality
        pass

    def search_pelanggan(self):
        # Implement search pelanggan functionality
        pass

    def logout(self):
        session.pop('loggedin', None)
        session.pop('username', None)
        session.pop('level', None)
        flash('You have been logged out', 'success')
        return redirect(url_for('login'))

if __name__ == "__main__":
    app_instance = App()
    app_instance.app.run(debug=True)
