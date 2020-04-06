import sys
import os
import json
import uuid
import logging
from queue import  Queue

class Chat:
	def __init__(self):
		self.sessions={}
		self.users = {}
		self.users['messi']={ 'nama': 'Lionel Messi', 'negara': 'Argentina', 'password': 'surabaya', 'incoming' : {}, 'outgoing': {}}
		self.users['henderson']={ 'nama': 'Jordan Henderson', 'negara': 'Inggris', 'password': 'surabaya', 'incoming': {}, 'outgoing': {}}
		self.users['lineker']={ 'nama': 'Gary Lineker', 'negara': 'Inggris', 'password': 'surabaya','incoming': {}, 'outgoing':{}}

	def proses(self,data):
		j = data.split(" ")
		try:
			command = j[0].strip()
			if (command == 'auth'):
				username = j[1].strip()
				password = j[2].strip()
				logging.warning("AUTH: auth {} {}" . format(username,password))
				return self.autentikasi_user(username,password)
			elif (command == 'logout'):
				sessionid = j[1].strip()
				logging.warning("LOGOUT: logout {}" . format(sessionid))
				return self.logout(sessionid)
			elif (command == 'send'):
				sessionid = j[1].strip()
				usernameto = j[2].strip()
				message=""
				for w in j[3:]:
					message = "{} {}" . format(message,w)
				usernamefrom = self.sessions[sessionid]['username']
				logging.warning("SEND: session {} send message from {} to {}" . format(sessionid, usernamefrom,usernameto))
				return self.send_message(sessionid, usernamefrom, usernameto, message)
			elif (command == 'inbox'):
				sessionid = j[1].strip()
				username = self.sessions[sessionid]['username']
				logging.warning("INBOX: {}" . format(sessionid))
				return self.get_inbox(username)
			elif (command == 'outbox'):
				sessionid = j[1].strip()
				username = self.sessions[sessionid]['username']
				logging.warning("OUTBOX: {}" . format(sessionid))
				return self.get_outbox(username)
			elif (command == 'active'):
				sessionid = j[1].strip()
				logging.warning("ACTIVE USER REQ by: {}" . format(sessionid))
				return self.get_active()
			else:
				return {'status': 'ERROR', 'message': '**Protocol Tidak Benar'}
		except KeyError:
			return { 'status': 'ERROR', 'message' : 'Informasi tidak ditemukan'}
		except IndexError:
			return {'status': 'ERROR', 'message': '--Protocol Tidak Benar'}

	def autentikasi_user(self,username,password):
		if (username not in self.users):
			return { 'status': 'ERROR', 'message': 'User Tidak Ditemukan' }
		if (self.users[username]['password']!= password):
			return { 'status': 'ERROR', 'message': 'Password Salah' }

		tokenid = str(uuid.uuid4())
		self.sessions[tokenid] = {
			'username': username,
			'userdetail': self.users[username]
		}
		return { 'status': 'OK', 'tokenid': tokenid }

	def get_user(self,username):
		if (username not in self.users):
			return False
		return self.users[username]

	def send_message(self,sessionid,username_from,username_dest,message):
		if (sessionid not in self.sessions):
			return {'status': 'ERROR', 'message': 'Session Tidak Ditemukan'}

		s_fr = self.get_user(username_from)
		s_to = self.get_user(username_dest)

		if (s_fr==False or s_to==False):
			return {'status': 'ERROR', 'message': 'User Tidak Ditemukan'}

		message = { 'msg_from': s_fr['nama'], 'msg_to': s_to['nama'], 'msg': message }

		outqueue_sender = s_fr['outgoing']
		inqueue_receiver = s_to['incoming']

		try:
			outqueue_sender[username_from].put(message)
		except KeyError:
			outqueue_sender[username_from]=Queue()
			outqueue_sender[username_from].put(message)

		try:
			inqueue_receiver[username_from].put(message)
		except KeyError:
			inqueue_receiver[username_from]=Queue()
			inqueue_receiver[username_from].put(message)

		return {'status': 'OK', 'message': 'Message Sent'}

	def get_inbox(self,username):
		s_fr = self.get_user(username)
		incoming = s_fr['incoming']
		msgs={}
		for users in incoming:
			msgs[users]=[]
			while not incoming[users].empty():
				msgs[users].append(s_fr['incoming'][users].get_nowait())

		return {'status': 'OK', 'messages': msgs}

	def get_outbox(self,username):
		s_fr = self.get_user(username)
		outgoing = s_fr['outgoing']
		msgs={}
		for users in outgoing:
			msgs[users]=[]
			while not outgoing[users].empty():
				msgs[users].append(s_fr['outgoing'][users].get_nowait())

		return {'status': 'OK', 'messages': msgs}

	def get_active(self):
		s_ac = []
		for active in self.sessions:
			s_ac.append({
				'username': self.sessions[active]['username'],
				'nama': self.sessions[active]['userdetail']['nama'],
				'negara': self.sessions[active]['userdetail']['negara'],
			})
		return {'status': 'OK', 'messages': s_ac}
	
	def logout(self,sessionid):
		username = self.sessions[sessionid]['username']
		if (sessionid not in self.sessions):
			return {'status': 'ERROR', 'message': 'Session Tidak Ditemukan'}

		del self.sessions[sessionid]
		return { 'status': 'OK', 'username': username }




if __name__=="__main__":
	j = Chat()
	mes = j.proses("auth messi surabaya")
	hen = j.proses("auth henderson surabaya")
	lin = j.proses("auth lineker surabaya")

	print(mes)

	mesid = mes['tokenid']
	henid = hen['tokenid']
	linid = lin['tokenid']

	# print(j.logout(mesid))

	print(json.dumps(j.get_active(), indent=1))

	# print(j.proses("send {} henderson xxx gimana kabarnya son " . format(mesid)))
	# print(j.proses("send {} henderson yyy gimana kabarnya son " . format(mesid)))

	print(j.proses("send {} messi aaa gimana kabarnya mes " . format(linid)))
	print(j.proses("send {} messi xxx gimana kabarnya mes " . format(henid)))
	print(j.proses("send {} messi bbb gimana kabarnya mes " . format(linid)))
	print(j.proses("send {} messi yyy gimana kabarnya mes " . format(henid)))


	# print("isi mailbox dari henderson")
	# print(json.dumps(j.get_inbox('henderson')))
	print("isi inbox dari messi")
	print(json.dumps(j.get_inbox('messi'), indent=1))
	# print("isi outbox dari messi")
	# print(json.dumps(j.get_outbox('messi'), indent=1))
















