#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Overxfl0w13 #
# Sequential search, boyer moore algorithm #

def generate_d_vector(text,pattern):
	d = {}
	for char in text: 
		founded = pattern.lower().rfind(char.lower())
		if char.lower() not in d:
			d[char] = len(pattern)-1-pattern.lower().rfind(char.lower()) if founded != -1 else len(pattern)
	return d

def boyer_moore(text,pattern,d):
	j = len(pattern)-1
	while j<len(text):
		i = len(pattern)-1
		while i>0 and pattern[i].lower()==text[j].lower(): 
			i,j = i-1,j-1		
		if i==0: return j
		else:
			if len(pattern)-1-i>d[text[j]]: j = j + len(pattern)-1- i + 1
			else: j = j + d[text[j]]
	return -1
	
if __name__ == "__main__":
	text,pattern = "Dalam KBBI kemahasiswaan adalah kata benda yang memiliki arti seluk-beluk mahasiswa; yang bersangkutan dengan mahasiswa. Hal-hal apa yang bisa ditentukan bila melihat definisi kemahasiswaan tersebut? Mahasiswa, jurusan, fakultas, perguruan tinggi, profesi, buku, jurnal, belajar, skripsi, dan sebagainya. Akan tetapi pengertian kemahasiswaan yang begitu luas tersebut mengalami penyempitan makna yang drastis. Arti kata kemahasiswaan saat ini hanya merujuk pada hal-hal yang berbau non-akademis. Seolah-olah kemahasiswaan hanya berhubungan dengan hal-hal yang seremonial belaka. Mahasiswa mendemo pemerintahan, membuat gerakan-gerakan yang sok mencerminkan populisme, suka mengikuti kegiatan di kampus sampai melupakan belajar, dan masih banyak lagi. Pada akhirnya kemahasiswaan hanya dipakai sebagai ajang kesombongan dan pamer di media sosial, atau yang beberapa orang katakan “panjat sosial”. Padahal belum tentu orang-orang tersebut memahami esensi dari apa yang mereka sebut-sebut sebagai kemahasiswaan. Pertama, mahasiswa bukanlah siswa pendidikan dasar. Mahasiswa sudah bukan anak SMA lagi. Perbedaan mendasar antara mahasiswa dengan siswa SMA adalah bidang studi yang dipelajari. Mahasiswa sesungguhnya sudah menentukan bidang apa yang ia minati dan tekuni, yang diharapkan bisa dimanfaatkan untuk kehidupannya di masa depan.", input("Masukkan string uji: ")
	print(boyer_moore(text,pattern,generate_d_vector(text,pattern)))