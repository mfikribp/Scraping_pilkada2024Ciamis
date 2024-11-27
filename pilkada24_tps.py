import pandas as pd
import requests
import json
from libs import lib_pilkada as lp

headers = {
    'authority':'sirekappilkada-obj-data.kpu.go.id',
    'method':'GET',
    'path':'/pilkada/hhcw/pkwkk/32/3207/320701/3207012010/3207012010001.json',
    'scheme':'https',
    'accept':'application/json, text/plain, */*',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'id,id-ID;q=0.9,en;q=0.8,en-US;q=0.7',
    'origin':'https://pilkada2024.kpu.go.id',
    'priority':'u=1, i',
    'referer':'https://pilkada2024.kpu.go.id/',
    'sec-ch-ua':'"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'same-site',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36}'
}




url_kel = 'https://sirekappilkada-obj-data.kpu.go.id/wilayah/pilkada/pkwkk/32/3207/320701/3207012010.json'
res = lp.get_response(url_kel)
unique_tps = lp.get_unique_number(res)

data = []
for kel in range(0, len(unique_tps)):
    kode_tps = unique_tps[kel][0]
    nama_tps = unique_tps[kel][1]

    url = f'https://sirekappilkada-obj-data.kpu.go.id/pilkada/hhcw/pkwkk/32/3207/320701/3207012010/{kode_tps}.json'



    response = requests.get(url,headers=headers).json()
    req = response['tungsura']

    
    pemilih_dpt_j = req['administrasi']['pemilih_dpt_j']
    pengguna_dpt_j = req['administrasi']['pengguna_dpt_j']
    suara_total = req['administrasi']['suara_total'] 
    suara_sah = req['administrasi']['suara_sah'] 
    suara_t_sah = req['administrasi']['suara_tidak_sah']
    suara_herdiat = req['chart']['1000561']
    kotak_kosong = req['chart']['1000562']

    # print(f"Pemilih terdaftar: {pemilih_dpt_j}")
    # print(f"Pengguna pemilih: {pengguna_dpt_j}")
    # print(f"Jumlah Suara: {suara_total}")
    # print(f"Suara sah: {suara_sah}")
    # print(f"Suara tidak sah: {suara_t_sah}")
    # print(f"Pemilih Herdiat: {suara_herdiat}")
    # print(f"Pemilih Kotak kosong: {kotak_kosong}")
    data.append(
        pemilih_dpt_j, pengguna_dpt_j, suara_total, suara_sah, suara_t_sah, suara_herdiat, kotak_kosong
    )
print(data)


