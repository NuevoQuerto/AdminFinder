import socket
import argparse
import re

print """
\t\t\t|----------------------------|
\t\t\t|       devilzc0de.org       |
\t\t\t| We Are Coder And Exploiter |
\t\t\t|                            |
\t\t\t|      Admin Finder          |
\t\t\t|Created By Nuevo Querto     |
\t\t\t|----------------------------|
"""

Parser = argparse.ArgumentParser(prog='AdminFinder.py', description="Tools Ini Untuk Mencari Halaman Admin :D")

Parser.add_argument("-u", "--url", help="Target URL, Example: -u www.kpu.go.id", action="store", default=False, dest="URL")

Args = Parser.parse_args()

Admin_Page = [
				"admin.php", "admin", "admin/index.php", "admin/admin.php", "admin/login.php",
				"login.php", "login", "login/index.php", "login/admin.php", "login/login.php",
				"wp-login.php", "wp-admin.php", "wp-admin"
			] # Halaman Login Admin
			
HTTP_Code = "200 OK|301 Moved Permanently|302 Found|302 Moved Temporarily" # HTTP Response Code

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
			if Checking_Code:
				print Args.URL + "/" + Admin_Page[i] + " [ Ketemu ]\n"
			else:
				print Args.URL + "/" + Admin_Page[i] + " [ Tidak Ketemu ]\n"
	else:
		print "Usage: -h For Help"
except KeyboardInterrupt:
	print "Canceling"
