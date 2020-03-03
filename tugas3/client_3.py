import logging
import requests
import os
import threading

def download_gambar(url=None):
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}")
        fp = open(f"{namafile}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False

if __name__=='__main__':
    listImages = [
        "https://www.its.ac.id/news/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-26-at-17.18.55-768x511.jpeg",
        "https://www.its.ac.id/news/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-25-at-17.28.56-768x512.jpeg",
        "https://www.its.ac.id/news/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-24-at-18.06.47-768x434.jpeg",
        "https://www.its.ac.id/news/wp-content/uploads/sites/2/2020/02/WhatsApp-Image-2020-02-24-at-17.02.48-1-768x512.jpeg"
    ]

    threads = []
    for image in listImages:
        t = threading.Thread(target=download_gambar,args=(image,))
        threads.append(t)

    for thr in threads:
        thr.start()
