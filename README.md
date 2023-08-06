<p align="center">
  <img src="pyquote.png" alt="pyquote"/>
</p>
<p align="center">
<a href="https://mongodb.com" target="_blank">
<img src="https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"/>
</a>
<a href="https://fastapi.tiangolo.com/" target="_blank">
<img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI"/>
</a>
</p>

# Pyquote

REST API Pyquote adalah sebuah Rest API (Application Programming Interface) web yang menyediakan layanan untuk mengelola dan mengakses kumpulan quote. Rest API ini dibangun menggunakan Python [FastAPI](https://fastapi.tiangolo.com) dan terhubung dengan [MongoDB](https://www.mongodb.com) sebagai database.

## Endpoint yang Tersedia

- GET /quotes: Mengembalikan daftar quote dalam bentuk JSON.
- GET /quotes/{quote_id}: Mengembalikan quote dengan ID yang sesuai dalam bentuk JSON.
- POST /quotes: Membuat quote baru dan menyimpannya ke dalam koleksi quotes.
- PUT /quotes/{quote_id}: Memperbarui quote dengan ID tertentu dalam koleksi quotes.
- DELETE /quotes/{quote_id}: Menghapus quote dengan ID tertentu dari koleksi quotes.

## Format Data Quote

Setiap quote memiliki atribut berikut:

- id: ID unik untuk quote.
- text: Teks dari quote.
- author: Penulis atau sumber dari quote.

## Penggunaan

Anda dapat menggunakan aplikasi ini dengan mengirimkan permintaan HTTP ke endpoint yang sesuai menggunakan metode GET, POST, PUT, atau DELETE. Permintaan harus memiliki header Content-Type: application/json dan body permintaan harus berisi data quote dalam format JSON.

Pastikan Anda telah menjalankan server FastAPI dan MongoDB sebelum menggunakan REST API ini. Pastikan juga bahwa koleksi quotes telah dibuat di dalam database MongoDB yang terhubung.

Selamat menggunakan REST API Pyquote!
