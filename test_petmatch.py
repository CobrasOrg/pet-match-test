from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
import time
import sys
import os

class PetMatchTester:
    def __init__(self):
        self.base_url = "http://localhost:5173"
        self.driver = None
        
    def setup_driver(self):
        """Configura e inicializa el driver de Firefox (sin webdriver-manager)"""
        print("Configurando el navegador Firefox...")
        
        firefox_options = Options()
        # Configuraciones para mejor estabilidad
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        firefox_options.set_preference("dom.webnotifications.enabled", False)
        firefox_options.set_preference("media.volume_scale", "0.0")
        
        try:
            # Usar Firefox directamente sin webdriver-manager
            self.driver = webdriver.Firefox(options=firefox_options)
            self.driver.maximize_window()
            print("Firefox iniciado correctamente")
        except Exception as e:
            print(f"Error al iniciar Firefox: {e}")
            print("Asegúrate de tener Firefox instalado y geckodriver en el PATH")
            print("Descarga geckodriver desde: https://github.com/mozilla/geckodriver/releases")
            raise
        
    def close_driver(self):
        """Cierra el navegador"""
        if self.driver:
            print("Cerrando navegador...")
            try:
                self.driver.quit()
            except:
                pass
            self.driver = None
            time.sleep(2)
    
    def wait_and_click(self, by, value, timeout=10):
        """Espera a que un elemento sea clickeable y lo hace click"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()
        return element
    
    def wait_and_type(self, by, value, text, timeout=10):
        """Espera a que un elemento esté presente y escribe texto en él"""
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        element.clear()
        element.send_keys(text)
        return element
    
    def wait_for_element(self, by, value, timeout=10):
        """Espera a que un elemento esté presente"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    
    def logout_if_logged_in(self):
        """Cierra sesión si hay una sesión activa"""
        try:
            # Buscar el botón de perfil
            profile_button = None
            buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
            for button in buttons:
                try:
                    svg_path = button.find_element(By.CSS_SELECTOR, "svg path[d*='M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2']")
                    profile_button = button
                    break
                except:
                    continue
            
            if profile_button:
                print("🔓 Cerrando sesión...")
                profile_button.click()
                time.sleep(1)
                
                # Buscar y hacer click en "Cerrar sesión" 
                logout_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Cerrar sesión')]")
                if logout_buttons:
                    # Hacer scroll al elemento si es necesario
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", logout_buttons[0])
                    time.sleep(0.5)
                    logout_buttons[0].click()
                    time.sleep(1)
                    print("✅ Sesión cerrada")
                else:
                    print("❌ No se encontró botón de logout")
            else:
                print("No hay sesión activa")
                
        except Exception:
            print("❌ Error al cerrar sesión")
    
    def visit_profile_and_show_data(self):
        """Visita el perfil del usuario y muestra sus datos"""
        try:
            # Buscar el botón de perfil
            profile_button = None
            buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
            for button in buttons:
                try:
                    svg_path = button.find_element(By.CSS_SELECTOR, "svg path[d*='M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2']")
                    profile_button = button
                    break
                except:
                    continue
            
            if profile_button:
                print("📋 Visitando perfil del usuario...")
                profile_button.click()
                time.sleep(1)
                
                # Buscar y hacer click en "Mi Perfil"
                profile_links = self.driver.find_elements(By.XPATH, "//a[contains(text(), 'Mi Perfil')] | //div[contains(text(), 'Mi Perfil')]")
                if profile_links:
                    profile_links[0].click()
                    time.sleep(2)
                    
                    # Intentar obtener datos específicos del perfil
                    try:
                        # Buscar información específica: nombre, email, teléfono
                        user_data = {}
                        
                        # Buscar email
                        try:
                            email_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), '@')]")
                            for elem in email_elements:
                                text = elem.text.strip()
                                if '@' in text and '.' in text and len(text) < 50:
                                    user_data['Email'] = text
                                    break
                        except:
                            pass
                        
                        # Buscar teléfono (números de 10 dígitos)
                        try:
                            phone_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), '3') or contains(text(), '2') or contains(text(), '1')]")
                            for elem in phone_elements:
                                text = elem.text.strip()
                                if text.isdigit() and len(text) == 10 and text.startswith(('3', '2', '1')):
                                    user_data['Teléfono'] = text
                                    break
                        except:
                            pass
                        
                        # Buscar nombre/título principal
                        try:
                            name_elements = self.driver.find_elements(By.CSS_SELECTOR, "h1, h2, .text-xl, .font-bold")
                            for elem in name_elements:
                                text = elem.text.strip()
                                if text and len(text) > 3 and len(text) < 50 and not any(x in text.lower() for x in ['perfil', 'configuración', 'información']):
                                    user_data['Nombre'] = text
                                    break
                        except:
                            pass
                        
                        # Mostrar datos encontrados
                        print("👤 Datos del perfil:")
                        if user_data:
                            for key, value in user_data.items():
                                print(f"   • {key}: {value}")
                        else:
                            print("   • Perfil visitado correctamente")
                        
                    except Exception:
                        print("   • Perfil visitado correctamente")
                    
                else:
                    print("❌ No se pudo acceder al perfil")
            else:
                print("❌ No se encontró el botón de perfil")
                
        except Exception as e:
            print(f"❌ Error al visitar perfil")
    
    def test_login_usuario(self):
        """Prueba 1: Login como usuario dueño de mascota"""
        print("\n=== PRUEBA 1: Login como Usuario (Dueño de Mascota) ===")
        
        try:
            self.setup_driver()
            
            # Ir a la página de login
            print("🔑 Iniciando login de usuario...")
            self.driver.get(f"{self.base_url}/login")
            time.sleep(1.5)
            
            # Verificar que estamos en la página correcta
            self.wait_for_element(By.CSS_SELECTOR, "input[type='email']")
            
            # Llenar el formulario de login
            self.wait_and_type(By.CSS_SELECTOR, "input[type='email']", "juan@example.com")
            self.wait_and_type(By.CSS_SELECTOR, "input[type='password']", "Password123")
            
            # Hacer click en el botón de iniciar sesión
            self.wait_and_click(By.CSS_SELECTOR, "button[type='submit']")
            
            # Esperar a que aparezca el alert y aceptarlo
            time.sleep(2)
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
            except:
                pass
            
            # Verificar redirección exitosa
            time.sleep(1.5)
            current_url = self.driver.current_url
            
            if "/public" in current_url:
                print("✅ LOGIN USUARIO EXITOSO")
                
                # Visitar perfil y mostrar datos
                time.sleep(1)
                self.visit_profile_and_show_data()
                
            else:
                print("❌ LOGIN USUARIO FALLÓ")
            
            # Cerrar sesión
            time.sleep(1)
            self.logout_if_logged_in()
            
        except Exception as e:
            print(f"❌ ERROR en test_login_usuario: {str(e)}")
        finally:
            self.close_driver()
    
    def test_login_veterinaria(self):
        """Prueba 2: Login como clínica veterinaria"""
        print("\n=== PRUEBA 2: Login como Clínica Veterinaria ===")
        
        try:
            self.setup_driver()
            
            # Ir a la página de login
            print("🏥 Iniciando login de veterinaria...")
            self.driver.get(f"{self.base_url}/login")
            time.sleep(1.5)
            
            # Verificar que estamos en la página correcta
            self.wait_for_element(By.CSS_SELECTOR, "input[type='email']")
            
            # Llenar el formulario de login
            self.wait_and_type(By.CSS_SELECTOR, "input[type='email']", "veterinaria@sanpatricio.com")
            self.wait_and_type(By.CSS_SELECTOR, "input[type='password']", "Clinic123")
            
            # Hacer click en el botón de iniciar sesión
            self.wait_and_click(By.CSS_SELECTOR, "button[type='submit']")
            
            # Esperar a que aparezca el alert y aceptarlo
            time.sleep(2)
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
            except:
                pass
            
            # Verificar redirección exitosa
            time.sleep(1.5)
            current_url = self.driver.current_url
            
            if "/requests" in current_url:
                print("✅ LOGIN VETERINARIA EXITOSO")
                
                # Visitar perfil y mostrar datos
                time.sleep(1)
                self.visit_profile_and_show_data()
                
            else:
                print("❌ LOGIN VETERINARIA FALLÓ")
            
            # Cerrar sesión
            time.sleep(1)
            self.logout_if_logged_in()
            
        except Exception as e:
            print(f"❌ ERROR en test_login_veterinaria: {str(e)}")
        finally:
            self.close_driver()
    
    def test_register_and_login_owner(self):
        """Prueba 3: Registrar nuevo dueño de mascota"""
        print("\n=== PRUEBA 3: Registro de Nuevo Dueño de Mascota ===")
        
        # Datos del nuevo usuario con teléfono colombiano correcto
        user_data = {
            "name": "Carlos Rodríguez",
            "email": "carlos.rodriguez@email.com",
            "phone": "3118622827",  # Formato colombiano de 10 dígitos
            "address": "Carrera 15 #45-30, Bogotá",
            "password": "MiPassword123"
        }
        
        try:
            self.setup_driver()
            
            # Ir a la página de registro
            print("📝 Registrando nuevo dueño de mascota...")
            self.driver.get(f"{self.base_url}/register")
            time.sleep(2)
            
            # Verificar y hacer click en "Dueño de Mascota"
            owner_button = self.wait_and_click(By.XPATH, "//button[contains(text(), 'Dueño de Mascota')]")
            time.sleep(2)
            
            # Llenar el formulario de registro
            self.wait_and_type(By.CSS_SELECTOR, "input[placeholder='Juan Pérez']", user_data["name"])
            self.wait_and_type(By.CSS_SELECTOR, "input[placeholder='juan@example.com']", user_data["email"])
            self.wait_and_type(By.CSS_SELECTOR, "input[placeholder='+57 300 123 4567']", user_data["phone"])
            self.wait_and_type(By.CSS_SELECTOR, "input[placeholder='Calle 123 #45-67']", user_data["address"])
            
            # Buscar los campos de contraseña
            password_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='password']")
            if len(password_inputs) >= 2:
                password_inputs[0].clear()
                password_inputs[0].send_keys(user_data["password"])
                password_inputs[1].clear()
                password_inputs[1].send_keys(user_data["password"])
            
            # Hacer click en registrarse
            self.wait_and_click(By.CSS_SELECTOR, "button[type='submit']")
            
            # Esperar alert de confirmación
            time.sleep(2.5)
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
            except:
                pass
            
            # Verificar que el registro fue exitoso
            time.sleep(1.5)
            current_url = self.driver.current_url
            
            if "/public" in current_url:
                print("✅ REGISTRO DE DUEÑO EXITOSO")
                
                # Visitar perfil y mostrar datos del usuario registrado
                time.sleep(1)
                self.visit_profile_and_show_data()
                
                # Cerrar sesión después de ver el perfil
                time.sleep(1)
                self.logout_if_logged_in()
            else:
                print("❌ REGISTRO DE DUEÑO FALLÓ")
            
        except Exception as e:
            print(f"❌ ERROR en test_register_and_login_owner: {str(e)}")
        finally:
            self.close_driver()
    
    def test_register_and_login_clinic(self):
        """Prueba 4: Registrar nueva clínica veterinaria"""
        print("\n=== PRUEBA 4: Registro de Nueva Clínica Veterinaria ===")
        
        # Datos de la nueva clínica con teléfono colombiano correcto
        clinic_data = {
            "name": "Veterinaria Los Andes",
            "email": "info@veterinarialosandes.com",
            "phone": "3029876543",  # Formato colombiano de 10 dígitos
            "address": "Avenida 68 #125-40",
            "password": "ClinicPassword123"
        }
        
        try:
            self.setup_driver()
            
            # Ir a la página de registro
            print("🏥 Registrando nueva clínica veterinaria...")
            self.driver.get(f"{self.base_url}/register")
            time.sleep(2)
            
            # Verificar y hacer click en "Clínica Veterinaria"
            clinic_button = self.wait_and_click(By.XPATH, "//button[contains(text(), 'Clínica Veterinaria')]")
            time.sleep(2)
            
            # Llenar el formulario de registro
            self.wait_and_type(By.CSS_SELECTOR, "input[placeholder='Veterinaria San Patricio']", clinic_data["name"])
            self.wait_and_type(By.CSS_SELECTOR, "input[placeholder='info@veterinaria.com']", clinic_data["email"])
            self.wait_and_type(By.CSS_SELECTOR, "input[placeholder='+57 300 123 4567']", clinic_data["phone"])
            self.wait_and_type(By.CSS_SELECTOR, "input[placeholder='Av. Principal 123']", clinic_data["address"])
            
            # Seleccionar localidad
            select_trigger = self.wait_and_click(By.CSS_SELECTOR, "[role='combobox']")
            time.sleep(1)
            
            # Intentar seleccionar localidades disponibles
            localidades = ["Engativá", "Suba", "Usaquén", "Chapinero", "Kennedy"]
            for localidad in localidades:
                try:
                    localidad_option = self.driver.find_element(By.XPATH, f"//div[@role='option'][contains(text(), '{localidad}')]")
                    localidad_option.click()
                    break
                except:
                    continue
            else:
                # Si no se encuentra ninguna, usar la primera disponible
                try:
                    first_option = self.wait_and_click(By.CSS_SELECTOR, "div[role='option']:first-child")
                except:
                    pass
            
            time.sleep(1)
            
            # Buscar los campos de contraseña
            password_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='password']")
            if len(password_inputs) >= 2:
                password_inputs[0].clear()
                password_inputs[0].send_keys(clinic_data["password"])
                password_inputs[1].clear()
                password_inputs[1].send_keys(clinic_data["password"])
            
            # Hacer click en registrar clínica
            self.wait_and_click(By.CSS_SELECTOR, "button[type='submit']")
            
            # Esperar alert de confirmación
            time.sleep(2.5)
            try:
                alert = self.driver.switch_to.alert
                alert.accept()
            except:
                pass
            
            # Verificar que el registro fue exitoso
            time.sleep(1.5)
            current_url = self.driver.current_url
            
            if "/requests" in current_url:
                print("✅ REGISTRO DE CLÍNICA EXITOSO")
                
                # Visitar perfil y mostrar datos de la clínica registrada
                time.sleep(1)
                self.visit_profile_and_show_data()
                
                # Cerrar sesión después de ver el perfil
                time.sleep(1)
                self.logout_if_logged_in()
            else:
                print("❌ REGISTRO DE CLÍNICA FALLÓ")
            
        except Exception as e:
            print(f"❌ ERROR en test_register_and_login_clinic: {str(e)}")
        finally:
            self.close_driver()
    
    def run_all_tests(self):
        """Ejecuta todas las pruebas secuencialmente"""
        print("🚀 INICIANDO PRUEBAS DE PETMATCH")
        print("=" * 40)
        
        # Ejecutar todas las pruebas
        self.test_login_usuario()
        self.test_login_veterinaria()
        self.test_register_and_login_owner()
        self.test_register_and_login_clinic()
        
        print("\n" + "=" * 40)
        print("🏁 PRUEBAS COMPLETADAS")

def main():
    tester = PetMatchTester()
    
    if len(sys.argv) > 1:
        test_name = sys.argv[1]
        if hasattr(tester, test_name):
            getattr(tester, test_name)()
        else:
            print(f"Prueba '{test_name}' no encontrada")
            print("Pruebas disponibles:")
            print("- test_login_usuario")
            print("- test_login_veterinaria")
            print("- test_register_and_login_owner")
            print("- test_register_and_login_clinic")
    else:
        tester.run_all_tests()

if __name__ == "__main__":
    main()
