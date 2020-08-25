from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

login_screen = 'https://zeusr.sii.cl//AUT2000/InicioAutenticacion/IngresoRutClave.html'
carpeta_tributaria = 'https://zeus.sii.cl/dii_cgi/carpeta_tributaria/cte_acreditar_renta_00.cgi'
archivo_guardar = './carpeta_tributaria.html'

username = 'aqui_va_el_rut'
password = 'aqui_va_el_password'

driver = webdriver.Firefox()
driver.get(login_screen)
wait = ui.WebDriverWait(driver, 10)

elem = driver.find_element_by_id('rutcntr')
elem.clear()
elem.send_keys(username)

elem = driver.find_element_by_id('clave')
elem.clear()
elem.send_keys(password)

elem = driver.find_element_by_id('bt_ingresar')
elem.submit()

wait.until(lambda driver: driver.find_elements_by_class_name('nuevas_medidas_clasemedia'))

driver.get(carpeta_tributaria)

wait.until(EC.frame_to_be_available_and_switch_to_it((By.NAME,'cte')))

driver.save_screenshot("carpeta_tributaria.png")

with open(archivo_guardar, "w") as f:
    f.write(driver.page_source)

driver.close()
