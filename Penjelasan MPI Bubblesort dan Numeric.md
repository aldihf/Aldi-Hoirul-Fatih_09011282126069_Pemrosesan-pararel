# Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel
# Tugas MPI

## • Sebelum Pengerjaan
1.	Memastikan bahwa setiap PC/Laptop dalam satu jaringan yang sama 
2.	Menentukan Server dan Slave/worker
3.	Melakukan penginstallan net-tools untuk mengecek IP dan vim untuk teks editor

## •	Konfigurasi IP Server dan Slave didalam file /etc/hosts
1.	Untuk server, buka file /etc/hosts menggunakan perintah sudo nano /etc/hosts
2.	Di dalam file /etc/hosts tambahkan IP master dan Slave/worker,kemudian save file dan keluar dari file dengan ctrl+x

  	![WhatsApp Image 2023-11-16 at 19 14 04_698f3594](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/f2d4fde2-a0c4-443d-9989-2b0bbbb7203f)
  	
4.	Untuk worker/slave, sama seperti master buka file /etc/hosts kemudian masukkan cukup masukkan IP dari master dan worker pemegang file
   
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/6b064ee5-544a-45bd-be02-5ac763903bb9)

## •	Membuat user baru
1.	Untuk Server dan Worker/slave,Nama user harus sama. Untuk menambahkan User dapat digunakkan perintah sudo adduser(nama user baru)

    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/a89a6f01-5162-4d53-bd63-63167b2f577e)

2.	Kemudian berikan akses root kepada user yang telah dibuat dengan perintah sudo usermod -aG sudo (nama user baru)
3.	Terakhir kita masuk sebagai user baru yang telah dibuat dengan perintah su – (nama user baru)
   
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/33874e39-0006-4b8b-90f0-456ecc6f967f)
   
## •	Konfigurasi SSH
1.	Pertama lakukan penginstalan ssh diserver dan slave dengan perintah sudo apt install openssh-server
   
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/768213ea-9042-4e68-8d42-084f07b2b2e1)
   
    Kemudian lakukan pengecekan ssh dengan perintah ssh (nama user)@(host)
  	
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/fb532888-464d-40e8-82c3-579f88384a93)
  	
3.	Setelahnya lakukan generate keygen diserver dengan perintah ssh-keygen -t rsa
   
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/6e72e6c5-2ac3-49b3-a8a6-172058a4d2f6)
  	
5.	Kemudian lakukan copy key publik ke client dengan perintah cd .ssh
    cat id_rsa.pub | ssh <nama user>@<host> "mkdir .ssh; cat >> .ssh/authorized_keys". Lakukan berkali-kali sesuai dengan jumlah dan host dari setiap slave.
  	
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/2df8f4a5-9e89-487f-a237-563110f629a4)

## •	Pengkonfigurasian NFS
1.	Di dalam server dan slave buat sebuah folder dengan nama bebas,gunakan perintah mkdir.Folder setiap pc harus memiliki nama yang sama (nama folder yang ingin dibuat)
   
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/ec0a5878-a317-4ced-a667-218bed1dbd31)
  	
2.	Lakukan penginstalan NFS server perintahnnya ialah sudo apt install nfs-kernel-server
   
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/940d6da3-65a5-488b-bafb-1ca1c3e8024a)
  	
3.	Lakukan konfigurasi file /etc/exports server, dengan perintah sudo vim /etc/exports
    Kemudian masukkan kalimat berikut:
    <lokasi shared folder> *(rw,sync,no_root_squash,no_subtree_check)
    Sesuaikan lokasi shared folder dengan folder yang telah dibuat sebelumnya.
  	
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/3733a4d8-7a74-4592-a9a7-b7cceedf8e63)
  	
    Kemudian masukkan perintah sudo exportfs -a dan sudo systemctl restart nfs-kernel-server
  	
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/e233015f-2f08-4eb9-bec1-8e2bc2655349)
  	
4.	Kemudian install nfs pada client dengan perintah sudo apt install nfs-common
   
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/c15f94ed-c341-435c-97e3-41cb908577cd)
  	
5.	Kemudian Mounting dengan perintah sudo mount <server host>:<lokasi shared folder di server> <lokasi shared folder di client> pada slave
   
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/d1c2449e-c544-410c-a882-667a1e03ce95)

## •	MPI
   Install MPI dengan perintah sudo apt install openmpi-bin libopenmpi-dev pada server dan slave

   ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/68f9e749-458a-4706-ab43-0f8d71a9b0a0)

## •	Menjalankan program bubblesort dan numerik
1.	Lakukan penginstallan python dan mpi4py dengan perintah sudo apt install python3-pip dan pip install mpi4py
   
    ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/a0b95cfc-a498-4920-85f0-69d00a0e615e)
  	
2.	Pertama buat 2 buah file python yaitu touch bubblesort.py untuk file bubblesort dan touch numeric.py untuk file numeric    
3.	Kemudian masuk kemasing-masing file dengan cara sudo nano bubblesort.py/numeric.py dan didalam file tersebut masukkan program sesuai dengan jenis nama file.
- Program bubblesort

  ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/02485c97-8c11-409a-8ad5-e414ef7a8740)
  
- Program numeric

  ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/bdb0286c-2b62-4f21-bdbc-206a72de18f2)
  
4.	Jalankan file menggunakan MPI dengan perintah mpirun -np <jumlah prosesor> -host <daftar host> python3 test.py.
- Hasil program bubblesort

  ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/cc6c8b01-3390-45a9-b565-fa1288689bc6)
  
- Hasil program numeric

  ![image](https://github.com/aldihf/Aldi-Hoirul-Fatih_09011282126069_Pemrosesan-pararel/assets/151024026/15f14fb3-215b-4336-9142-378d91ff5286)
