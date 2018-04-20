"""
KMP Text Search - O(m + n)
m = haystack
n = needle
"""

def kmp(strings, find_string):
    n = len(strings)
    m = len(find_string)
    j = 0
    k = 0
    fail = kmp_fail(find_string)
    while j < n:
        if strings[j].lower() == find_string[k].lower():
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return 'tidak ada kecocokkan'
        
        
def kmp_fail(find_string):
    n = len(find_string)
    fail = [0] * n
    j = 1
    k = 0
    while j < n:
        if find_string[j].lower() == find_string[k].lower():
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return fail
	
find_string = input('Masukkan string uji: ')
print(kmp('Dalam KBBI kemahasiswaan adalah kata benda yang memiliki arti seluk-beluk mahasiswa; yang bersangkutan dengan mahasiswa. Hal-hal apa yang bisa ditentukan bila melihat definisi kemahasiswaan tersebut? Mahasiswa, jurusan, fakultas, perguruan tinggi, profesi, buku, jurnal, belajar, skripsi, dan sebagainya. Akan tetapi pengertian kemahasiswaan yang begitu luas tersebut mengalami penyempitan makna yang drastis. Arti kata kemahasiswaan saat ini hanya merujuk pada hal-hal yang berbau non-akademis. Seolah-olah kemahasiswaan hanya berhubungan dengan hal-hal yang seremonial belaka. Mahasiswa mendemo pemerintahan, membuat gerakan-gerakan yang sok mencerminkan populisme, suka mengikuti kegiatan di kampus sampai melupakan belajar, dan masih banyak lagi. Pada akhirnya kemahasiswaan hanya dipakai sebagai ajang kesombongan dan pamer di media sosial, atau yang beberapa orang katakan “panjat sosial”. Padahal belum tentu orang-orang tersebut memahami esensi dari apa yang mereka sebut-sebut sebagai kemahasiswaan. Pertama, mahasiswa bukanlah siswa pendidikan dasar. Mahasiswa sudah bukan anak SMA lagi. Perbedaan mendasar antara mahasiswa dengan siswa SMA adalah bidang studi yang dipelajari. Mahasiswa sesungguhnya sudah menentukan bidang apa yang ia minati dan tekuni, yang diharapkan bisa dimanfaatkan untuk kehidupannya di masa depan.',find_string))