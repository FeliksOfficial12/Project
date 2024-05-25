from numpy import array
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu # Untuk membuat SIDE BAR
import pandas as pd
import PIL.Image as img
import time
import pickle

from time_predict import run_ml

#Tampilan halaman utama
st.title('Porter Delivery Time Estimation')


image = img.open('porterimg2.jpg')
st.image(image)
image1 = img.open('Visualization1.png')
image2 = img.open('Visualization2.png')
image3 = img.open('Visualization3.png')
image4 = img.open('Visualization4.png')

desc_1 = """
        Porter is a tech-enabled logistics company offering a variety of intracity 
        and intercity delivery services. From a pin to an entire house, Porter will 
        deliver anything, anywhere, anytime. However, Porter does not deliver item(s) 
        which are illegal, dangerous or hazardous in nature or which are prohibited by 
        any statue or law. 
        """

desc_2 = """
        This app is made, as a Final Project from Digital Skola, by Team Honeycomb. 
        This app will do Delivery Time Estimation on Porter delivery services. 
        The whole process upon making this app started from thorough data preprocessing, 
        model selection & training, model evaluation until model tuning. We believe the 
        prediction the app generates is accurate as we made it from the best of our knowledge.
        """
df = pd.DataFrame({'Team Member': 
                   ['Jessica Manna Febriani Nadeak',
                    'Ignatius Evans Erlangga',
                    'Hapsari Warih Utami',
                    'Feri Aditya Ridwan Mas',
                    'Feliks Wijaya Santoso',
                    'Fela Suvah'
                    ]})

desc_3 = """
         Pada total items: pengiriman dengan jumlah di bawah 10 cukup mendominasi. 
         Subtotal: Harga akhir pesanan dengan jumlah di bawah 5000, cukup besar, sekitar 70ribu pesanan. 
         Num_distinc items: jumlah barang dengan varian berbeda masih didominasi dibawah angka lima. Artinya pelanggan yang memesan dengan variasi berbeda, umumnya di bawah 5 items. 
         Min_items_price= untuk items dengan harga di bawah 2500 masih menjadi paling banyak dipesan.  Umumnya harganya berkisar di angka 1000an.
         Max_items_price: paling mahal items yang dipesan seharga 1500, dengan jumlah pesanan di atas 100ribuan items.
         Total onshift partner= jumlah mitra porter yang standby sekitar 20 pertener umumnya menangani 25ribu pesanan. Semakin tinggai yang standby, semakin rendah pula jumlah pesanan yang ditangani per partner. 
         Total_busy_ partners: sekitar 20 mitra porter menyelesaikan 30ribu pesanan lain.  Dan semakin  banyak partner driver jumlah pesanan yang ditangani mereka semakin menurun.
         Total_outstanding_order: sekitar 45 orderan diselesaikan pada saat itu juga oleh 38 ribu mitra porter.
         """

desc_4 = """
         Variabel yang berkorelasi:
         total_items ↔ sub_total
         semakin banyak jumlah barang, semakin tinggi harga pesanan.
         subtotal ↔ num_distinct_item
         semakin banyak variasi barang, semakin tinggi pesanan.
         variabel yang memiliki korelasi tertinggi dengan delivery_duration adalah subtotal.
         """

desc_5 = """
         Perbandingan lokasi restoran
         """

desc_6 = """
         Perbandingan metode pemesanan makanan
         """


page = option_menu('MENU' , ['About Porter', 'About Us'])
if page == 'About Porter':
   st.caption(desc_1)
   st.image(image1)
   st.caption(desc_3)
   st.image(image2)
   st.caption(desc_4)
   st.image(image3)
   st.caption(desc_5)
   st.image(image4)
   st.caption(desc_6)
elif page == 'About Us':
   st.caption (desc_2)
   st.subheader('Team Honeycomb consists of :')
   st.dataframe(df.style.hide())
   

def main():
   menu = ['Home', 'Delivery Time Prediction']
   choice = st.sidebar.selectbox('Menu', menu)
    
   if choice == 'Home':
      print('')
   elif choice == 'Delivery Time Prediction':
      run_ml()
    
if __name__== '__main__':
   main()

    

