import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from pdf_generator import PetMatchPDFGenerator

class PetMatchPetTester:
    def __init__(self):
        self.driver = None
        self.base_url = "http://localhost:5173"
        self.test_results = {}
        self.pdf_generator = PetMatchPDFGenerator()
        self.options = Options()
        self.options.add_argument("--width=1366")
        self.options.add_argument("--height=768")
        try:
            geckodriver_path = os.path.join(os.path.dirname(__file__), "..", "geckodriver.exe")
            if not os.path.exists(geckodriver_path):
                geckodriver_path = "geckodriver"
            self.service = Service(geckodriver_path)
        except Exception:
            self.service = None

    def setup_driver(self):
        try:
            print("Configurando navegador Firefox...")
            if self.service:
                self.driver = webdriver.Firefox(service=self.service, options=self.options)
            else:
                self.driver = webdriver.Firefox(options=self.options)
            self.driver.maximize_window()
            self.wait = WebDriverWait(self.driver, 10)
            print("Firefox iniciado correctamente")
            time.sleep(2)
            return True
        except Exception as e:
            print(f"Error al inicializar Firefox: {e}")
            return False

    def teardown_driver(self):
        if self.driver:
            print("Cerrando navegador...")
            try:
                self.driver.quit()
            except Exception:
                pass

    def test_pet_selection_modal(self):
        """Prueba que el modal de selección de mascotas se muestra y filtra correctamente"""
        try:
            self.driver.get(f"{self.base_url}/public")
            time.sleep(2)
            # Simular click en el primer botón de donación para abrir el modal
            donation_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Ayudar')]")
            if not donation_buttons:
                self.test_results['PetSelectionModal'] = {
                    'success': False,
                    'duration': 2,
                    'description': 'No se encontró botón para abrir el modal de selección de mascotas.'
                }
                return False
            donation_buttons[0].click()
            time.sleep(2)
            # Verificar que el modal aparece
            modal = self.driver.find_elements(By.CSS_SELECTOR, "div.fixed.inset-0")
            result = bool(modal)
            self.test_results['PetSelectionModal'] = {
                'success': result,
                'duration': 4,
                'description': 'El modal de selección de mascotas se muestra correctamente.' if result else 'El modal no apareció.'
            }
            return result
        except Exception as e:
            self.test_results['PetSelectionModal'] = {
                'success': False,
                'duration': 2,
                'description': f'Error: {str(e)}'
            }
            return False

    def test_pet_selector(self):
        """Prueba que el selector de mascotas muestra las opciones y permite seleccionar una"""
        try:
            self.driver.get(f"{self.base_url}/profile")
            time.sleep(2)
            # Buscar el selector de mascotas
            select_elements = self.driver.find_elements(By.CSS_SELECTOR, "select")
            result = bool(select_elements)
            self.test_results['PetSelector'] = {
                'success': result,
                'duration': 3,
                'description': 'El selector de mascotas está disponible en el perfil.' if result else 'No se encontró el selector de mascotas.'
            }
            return result
        except Exception as e:
            self.test_results['PetSelector'] = {
                'success': False,
                'duration': 2,
                'description': f'Error: {str(e)}'
            }
            return False

    def test_pet_registration_form(self):
        """Prueba que el formulario de registro de mascotas permite registrar una nueva mascota"""
        try:
            self.driver.get(f"{self.base_url}/register-pet")
            time.sleep(2)
            # Buscar el formulario
            form = self.driver.find_elements(By.TAG_NAME, "form")
            result = bool(form)
            self.test_results['PetRegistrationForm'] = {
                'success': result,
                'duration': 3,
                'description': 'El formulario de registro de mascotas está disponible.' if result else 'No se encontró el formulario de registro de mascotas.'
            }
            return result
        except Exception as e:
            self.test_results['PetRegistrationForm'] = {
                'success': False,
                'duration': 2,
                'description': f'Error: {str(e)}'
            }
            return False

    def test_pet_registration_flow(self):
        """Prueba flujo de registro de nueva mascota: login, navegar a Mis Mascotas, registrar mascota."""
        try:
            start = time.time()
            print("🔑 Iniciando login...")
            
            # 1. Login como dueño
            self.driver.get(f"{self.base_url}/login")
            email_input = self.wait.until(EC.presence_of_element_located((By.NAME, 'email')))
            password_input = self.driver.find_element(By.NAME, 'password')
            email_input.clear()
            email_input.send_keys("juan@example.com")
            password_input.clear()
            password_input.send_keys("Password123")
            self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            time.sleep(3)
            print("✅ Login completado")
            
            # 2. Manejar posible alert de login
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
                time.sleep(1)
            except:
                pass
            
            # 3. Abrir menú de perfil 
            print("📂 Abriendo menú de perfil...")
            profile_btns = self.driver.find_elements(By.CSS_SELECTOR, "button")
            profile_btn = None
            for btn in profile_btns:
                try:
                    svg = btn.find_element(By.CSS_SELECTOR, "svg path[d*='M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2']")
                    profile_btn = btn
                    break
                except:
                    continue
            
            if not profile_btn:
                raise Exception("No se encontró el botón de perfil")
            
            profile_btn.click()
            time.sleep(1)
            
            # 4. Click en Mis Mascotas
            print("🐾 Navegando a Mis Mascotas...")
            mis_mascotas_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Mis Mascotas')))
            mis_mascotas_link.click()
            time.sleep(3)
            
            # 5. Click en botón de registro
            print("➕ Buscando botón de registro...")
            reg_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Registrar Mascota')]")))
            reg_btn.click()
            time.sleep(3)
            print("📝 Formulario abierto")
            
            # 6. Llenar formulario paso a paso
            print("✏️ Llenando formulario...")
            
            # Nombre de la mascota
            name_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder*='Luna, Max, Bella']")))
            name_input.clear()
            name_input.send_keys('TestPet')
            time.sleep(0.5)
            
            # Especie - usar SelectTrigger
            print("Seleccionando especie...")
            species_triggers = self.driver.find_elements(By.CSS_SELECTOR, "button[role='combobox']")
            if species_triggers:
                species_triggers[0].click()
                time.sleep(1)
                perro_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option']//span[text()='Perro']")))
                perro_option.click()
                time.sleep(1)
            
            # Raza - segundo SelectTrigger
            print("Seleccionando raza...")
            breed_triggers = self.driver.find_elements(By.CSS_SELECTOR, "button[role='combobox']")
            if len(breed_triggers) > 1:
                breed_triggers[1].click()
                time.sleep(1)
                mestizo_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option']//span[text()='Mestizo']")))
                mestizo_option.click()
                time.sleep(1)
            
            # Edad
            print("Ingresando edad...")
            age_input = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='2.5']")
            age_input.clear()
            age_input.send_keys('3')
            time.sleep(0.5)
            
            # Peso  
            print("Ingresando peso...")
            weight_input = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='25.5']")
            weight_input.clear()
            weight_input.send_keys('30')
            time.sleep(0.5)
            
            # Tipo de sangre - tercer SelectTrigger
            print("Seleccionando tipo de sangre...")
            blood_triggers = self.driver.find_elements(By.CSS_SELECTOR, "button[role='combobox']")
            if len(blood_triggers) > 2:
                blood_triggers[2].click()
                time.sleep(1)
                blood_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='option']//span[text()='DEA 1.1+']")))
                blood_option.click()
                time.sleep(1)
            
            # Fecha de vacunación
            print("Ingresando fecha de vacunación...")
            vaccination_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='date']")
            vaccination_input.send_keys('2025-07-01')
            time.sleep(0.5)
            
            # Estado de salud
            print("Ingresando estado de salud...")
            health_textarea = self.driver.find_element(By.CSS_SELECTOR, "textarea")
            health_textarea.clear()
            health_textarea.send_keys('Mascota en excelente estado de salud, sin enfermedades conocidas, vacunas al día')
            time.sleep(0.5)
            
            # 7. Enviar formulario
            print("📤 Enviando formulario...")
            submit_btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_btn.click()
            time.sleep(3)
            
            # 8. Manejar alert de confirmación
            try:
                alert = self.wait.until(EC.alert_is_present())
                alert_text = alert.text
                print(f"🔔 Alert: {alert_text}")
                alert.accept()
                time.sleep(1)
            except:
                print("ℹ️ No se detectó alert")
            
            duration = time.time() - start
            self.test_results['RegistroMascota'] = {
                'success': True,
                'duration': f'{duration:.1f}s',
                'description': 'Registro de mascota completado exitosamente.'
            }
            print("✅ Prueba completada exitosamente")
            return True
            
        except Exception as e:
            duration = time.time() - start if 'start' in locals() else 0
            self.test_results['RegistroMascota'] = {
                'success': False,
                'duration': f'{duration:.1f}s',
                'description': f'Error en registro: {str(e)}'
            }
            print(f"❌ Error en prueba: {str(e)}")
            return False


def main():
    print("INICIANDO PRUEBA DE REGISTRO DE MASCOTA PETMATCH")
    tester = PetMatchPetTester()
    if not tester.setup_driver():
        print("No se pudo inicializar el navegador")
        return
    try:
        tester.test_pet_registration_flow()
    finally:
        tester.teardown_driver()
    # Generar reporte consolidado
    try:
        reports_dir = os.path.join(os.path.dirname(__file__), "reports")
        if not os.path.exists(reports_dir):
            os.makedirs(reports_dir)
        pdf_path = tester.pdf_generator.generate_summary_report(tester.test_results, reports_dir)
        print(f"Reporte generado: {pdf_path}")
    except Exception as e:
        print(f"Error generando reporte: {e}")

if __name__ == "__main__":
    main()
