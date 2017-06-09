import socket
import argparse
import re

print """
\t\t\t|----------------------------|
\t\t\t|       devilzc0de.org       |
\t\t\t| We Are Coder And Exploiter |
\t\t\t|                            |
\t\t\t|       Admin Finder         |
\t\t\t|  Created By Nuevo Querto   |
\t\t\t|----------------------------|
"""

Parser = argparse.ArgumentParser(prog='AdminFinder.py', description="Tools Ini Untuk Mencari Halaman Admin :D")

Parser.add_argument("-u", "--url", help="Target URL, Example: -u www.kpu.go.id", action="store", default=False, dest="URL")
Parser.add_argument("--wordlist", help="Wordlist Target, Example: -w Desktop/wordlist.txt", action="store", default=False, dest="Wordlist")

Args = Parser.parse_args()

Admin_Page = []

DefaultAdminPage = [
		"admin.php", "admin", "admin/index.php", "admin/admin.php", "admin/login.php", "admin/administrator.php", "admin/home.php", "admin/dsp_login.php",
		"login.php", "login", "login/index.php", "login/admin.php", "login/login.php", "login/administrator.php", "login/home.php", "login/dsp_login.php",
		"administrator.php", "administrator", "administrator/index.php", "administrator/admin.php", "administrator/login.php", "administrator/administrator.php", "administrator/home.php", "administrator/dsp_login.php",
		"admin_mato.php", "admin_mato", "admin_mato/index.php", "admin_mato/admin.php", "admin_mato/login.php", "admin_mato/administrator.php", "admin_mato/home.php", "admin_mato/dsp_login.php",
		"dashboard.php", "dashboard", "dashboard/index.php", "dashboard/admin.php", "dashboard/login.php", "dashboard/administrator.php", "dashboard/home.php", "dashboard/dashboard.php", "dashboard/dashboard.php",
		"wp-login.php", "wp-admin.php", "wp-admin"
	] # Halaman Login Admin
		
HTTP_Code = "200|301|302" # HTTP Response Code

if Args.Wordlist:
	with open(Args.Wordlist, "r+") as file:
		Read = file.read()
		Pisahkan = Read.split("\n")
	for i in range(len(Pisahkan)):
		ImportAdminPage = Admin_Page.append(Pisahkan[i])
else:
	for i in range(len(DefaultAdminPage)):
		ImportAdminPage = Admin_Page.append(DefaultAdminPage[i])
		
try:
	if Args.URL:
		for i in range(len(Admin_Page)):
			Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Membuat Objek Socket
			
			Socket.connect((Args.URL, 80)) # Menghubungkan Socket
			
			Request = """
GET /%s HTTP/1.1
Host: %s
Connection: keep-alive\n
			""" %(Admin_Page[i], Args.URL)
			
			Socket.send(Request) # Mengirim Request
			
			Response = Socket.recv(1024) # Menerima Respon
			
			Socket.close()
			
			Checking_Code = re.search( r"%s" %(HTTP_Code), Response, re.M|re.I) # Reguler Expression
			print Args.URL + "/" + Admin_Page[i] + " [ %s ]\n" %("Ketemu" if Checking_Code else "Tidak Ketemu")
	else:
		print "Usage: -h For Help"
except KeyboardInterrupt:
	print "Canceling"
except socket.gaierror:
	print "Masukkan Target Dengan Benar, Example: -u www.kpu.go.id"
