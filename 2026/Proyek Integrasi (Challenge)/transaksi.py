def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total = 0
    nomor = 1

    for item, jumlah in daftar_barang:
        print(f"{nomor}. ", end="")
        item.tampilkan_detail(jumlah)
        total += item.hitung_harga_total(jumlah)
        nomor += 1

    print("----------------------------------------")
    print(f"TOTAL TAGIHAN: Rp {int(total):,}")
    print("----------------------------------------")
