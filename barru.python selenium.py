import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):  # TEST SCENARIO

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Welcome', text_atas)
        self.assertEqual(text_bawah, 'Anda Berhasil Login')

    def test_b_failed_login_by_wrong_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("tester@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#password").send_keys("hahahoho") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', text_atas)
        self.assertEqual(text_bawah, 'Email atau Password Anda Salah')

    def test_c_failed_login_with_invalid_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("sahdasdg") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[2]").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").get_attribute("validationMessage")

        self.assertIn('Please include', text_atas)

    def test_d_failed_login_empty_email_pass(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[2]/form/input[1]").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input#password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signin_login").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('not found', text_atas)
        self.assertEqual(text_bawah, 'Email atau Password Anda Salah')

    def test_e_failed_register_min_characters(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") #buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("a") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("a@gmail.com") #isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("a") #isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() #klik tombol login
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("Karakter kurang dari 5", text_atas)
        self.assertEqual(text_bawah, "Gagal Register!")

    def test_f_failed_register_max_characters(self):
        #steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") #buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("qwertyuiopasdfghjklzxcvbnm1234567890") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("qwertyuiopasdfghjklzxcvbnm1234567890@gmail.com") #isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("qwertyuiopasdfghjklzxcvbnm1234567890") #isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() #klik tombol login
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("Melebihi batas karakter", text_atas)
        self.assertEqual(text_bawah, "Gagal Register!")
    
    def test_g_register_success(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("auliailma") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("auliailma109@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', text_atas)
        self.assertEqual(text_bawah, 'created user!')

    def test_h_register_failed_already_registered(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("auliailma") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("auliailma109@jagoqa.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("Sudah terdaftar", text_atas)
        self.assertEqual(text_bawah, "Gagal Register!")

    def test_h_register_failed_username_empty(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("auliailma109@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("Username kosong", text_atas)
        self.assertEqual(text_bawah, "Gagal Register!")
    
    def test_i_register_failed_email_empty(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("auliailma") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("testerjago") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("Username kosong", text_atas)
        self.assertEqual(text_bawah, "Gagal Register!")
    
    def test_j_register_failed_password_empty(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/daftar") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"signUp").click() # klik tombol sign up
        time.sleep(1)
        browser.find_element(By.ID,"name_register").send_keys("auliailma") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"email_register").send_keys("auliailma109@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"password_register").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign up
        time.sleep(1)

        # validasi
        text_atas = browser.find_element(By.ID,"swal2-title").text
        text_bawah = browser.find_element(By.ID,"swal2-content").text

        self.assertIn("Username kosong", text_atas)
        self.assertEqual(text_bawah, "Gagal Register!")

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
