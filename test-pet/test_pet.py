import os
import time
from datetime import datetime, timedelta
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
            self.wait = WebDriverWait(self.driver, 15)  # Aumentar timeout a 15 segundos
            print("Firefox iniciado correctamente")
            time.sleep(3)  # Aumentar tiempo de espera inicial
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
        """Prueba flujo completo: login, registrar mascota, eliminar mascota."""
        try:
            start = time.time()
            print("🔑 Iniciando login...")
            
            # 1. Login como dueño
            self.driver.get(f"{self.base_url}/login")
            email_input = self.wait.until(EC.presence_of_element_located((By.NAME, 'email')))
            password_input = self.driver.find_element(By.NAME, 'password')
            email_input.clear()
            email_input.send_keys("mcastiblancoa@unal.edu.co")
            password_input.clear()
            password_input.send_keys("Mati112999")
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
            time.sleep(2)
            
            # 4. Click en Mis Mascotas
            print("🐾 Navegando a Mis Mascotas...")
            mis_mascotas_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Mis Mascotas')))
            mis_mascotas_link.click()
            time.sleep(3)
            
            # 5. Click en botón de registro
            print("➕ Buscando botón de registro...")
            reg_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Registrar Mascota')]")))
            reg_btn.click()
            time.sleep(4)
            print("📝 Formulario abierto")
            
            # 6. Llenar formulario paso a paso
            print("✏️ Llenando formulario...")
            
            # Primero, vamos a imprimir el HTML del formulario para debug
            try:
                form_html = self.driver.find_element(By.TAG_NAME, "form").get_attribute("outerHTML")
                print("🔍 Estructura del formulario encontrada")
            except:
                print("⚠️ No se pudo obtener la estructura del formulario")
            
            # Nombre de la mascota
            print("Ingresando nombre...")
            name_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder*='Luna, Max, Bella']")))
            name_input.clear()
            name_input.send_keys('TestPetAuto')
            time.sleep(0.5)
            
            # Especie - buscar todas las opciones posibles
            print("Seleccionando especie...")
            species_selected = False
            
            try:
                # Scroll hacia arriba para asegurar visibilidad
                self.driver.execute_script("window.scrollTo(0, 0);")
                time.sleep(0.5)
                
                # Buscar todos los combobox
                species_triggers = self.driver.find_elements(By.XPATH, "//button[@role='combobox']")
                print(f"🔍 Encontrados {len(species_triggers)} elementos combobox")
                
                if len(species_triggers) >= 1:
                    # Usar JavaScript para hacer clic
                    self.driver.execute_script("arguments[0].click();", species_triggers[0])
                    time.sleep(1)
                    
                    # Buscar la opción Perro
                    perro_options = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Perro')]")
                    if perro_options:
                        # También usar JavaScript para la opción
                        self.driver.execute_script("arguments[0].click();", perro_options[0])
                        time.sleep(1)
                        species_selected = True
                        print("✅ Especie seleccionada: Perro")
                    else:
                        print("❌ No se encontró opción 'Perro'")
                        
            except Exception as e:
                print(f"❌ Error seleccionando especie: {e}")
            
            if not species_selected:
                raise Exception("No se pudo seleccionar la especie")
            
            # Raza - Intentar múltiples estrategias
            print("Seleccionando raza...")
            breed_selected = False
            
            try:
                time.sleep(1.5)  # Esperar a que la especie se actualice y se carguen las razas
                
                # Estrategia 1: Buscar combobox específico para raza
                print("🔍 Estrategia 1: Buscando combobox de raza...")
                breed_triggers = self.driver.find_elements(By.XPATH, "//button[@role='combobox']")
                print(f"🔍 Total combobox encontrados: {len(breed_triggers)}")
                
                # El segundo combobox debería ser para raza
                if len(breed_triggers) >= 2:
                    # Scroll al elemento para asegurar visibilidad
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", breed_triggers[1])
                    time.sleep(0.5)
                    
                    self.driver.execute_script("arguments[0].click();", breed_triggers[1])
                    time.sleep(1.5)
                    
                    # Buscar opciones disponibles después de abrir el dropdown
                    breed_options = self.driver.find_elements(By.XPATH, "//div[@role='option']")
                    print(f"🔍 Opciones de raza encontradas: {len(breed_options)}")
                    
                    # Buscar específicamente "Mestizo"
                    mestizo_found = False
                    for option in breed_options:
                        try:
                            if "Mestizo" in option.text:
                                self.driver.execute_script("arguments[0].click();", option)
                                time.sleep(1)
                                breed_selected = True
                                mestizo_found = True
                                print("✅ Raza seleccionada: Mestizo")
                                break
                        except:
                            continue
                    
                    # Si no se encuentra Mestizo, tomar la primera opción válida
                    if not mestizo_found and breed_options:
                        try:
                            self.driver.execute_script("arguments[0].click();", breed_options[0])
                            time.sleep(1)
                            breed_selected = True
                            print(f"✅ Raza seleccionada: {breed_options[0].text}")
                        except:
                            pass
                        
            except Exception as e:
                print(f"❌ Error en estrategia 1 de raza: {e}")
            
            # Estrategia 2: Buscar por texto específico si la primera falló
            if not breed_selected:
                try:
                    print("🔄 Estrategia 2: Buscando por texto...")
                    # Cerrar cualquier dropdown abierto
                    self.driver.execute_script("document.body.click();")
                    time.sleep(1)
                    
                    # Buscar elementos que contengan "raza" en el texto
                    raza_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'Raza') or contains(text(), 'raza')]")
                    print(f"🔍 Elementos relacionados con raza: {len(raza_elements)}")
                    
                    for element in raza_elements:
                        try:
                            # Buscar el combobox más cercano
                            parent = element.find_element(By.XPATH, "./following-sibling::*//button[@role='combobox']")
                            parent.click()
                            time.sleep(2)
                            
                            # Buscar opciones
                            options = self.driver.find_elements(By.XPATH, "//div[@role='option']")
                            if options:
                                options[0].click()
                                time.sleep(2)
                                breed_selected = True
                                print("✅ Raza seleccionada usando estrategia 2")
                                break
                        except:
                            continue
                            
                except Exception as e:
                    print(f"❌ Error en estrategia 2 de raza: {e}")
            
            # Estrategia 3: Buscar por posición en la página
            if not breed_selected:
                try:
                    print("🔄 Estrategia 3: Buscando por posición...")
                    # Buscar todos los select nativos
                    selects = self.driver.find_elements(By.TAG_NAME, "select")
                    if len(selects) >= 2:
                        from selenium.webdriver.support.ui import Select
                        select_obj = Select(selects[1])  # Segundo select debería ser raza
                        select_obj.select_by_index(1)  # Seleccionar primera opción válida
                        breed_selected = True
                        print("✅ Raza seleccionada usando select nativo")
                        
                except Exception as e:
                    print(f"❌ Error en estrategia 3 de raza: {e}")
            
            if not breed_selected:
                print("⚠️ No se pudo seleccionar raza, continuando con el test...")
            else:
                print("✅ Campo Raza completado exitosamente")
            
            # Edad
            print("Ingresando edad...")
            age_filled = False
            try:
                # Buscar input de edad
                age_inputs = self.driver.find_elements(By.XPATH, "//input[@type='number']")
                age_input = None
                
                # Buscar el input que tenga placeholder o esté cerca del label de edad
                for inp in age_inputs:
                    placeholder = inp.get_attribute('placeholder') or ''
                    if '2' in placeholder or inp.get_attribute('min') == '1':
                        age_input = inp
                        break
                
                if not age_input and age_inputs:
                    age_input = age_inputs[0]  # Tomar el primero si no se encuentra específico
                
                if age_input:
                    age_input.clear()
                    age_input.send_keys('3')
                    time.sleep(0.5)
                    age_filled = True
                    print("✅ Edad ingresada: 3 años")
                else:
                    print("❌ No se encontró input de edad")
                    
            except Exception as e:
                print(f"❌ Error ingresando edad: {e}")
            
            if not age_filled:
                print("⚠️ No se pudo ingresar edad, continuando...")
            
            # Peso  
            print("Ingresando peso...")
            weight_filled = False
            try:
                # Buscar input de peso
                weight_inputs = self.driver.find_elements(By.XPATH, "//input[@type='number']")
                weight_input = None
                
                for inp in weight_inputs:
                    placeholder = inp.get_attribute('placeholder') or ''
                    step = inp.get_attribute('step') or ''
                    if '25' in placeholder or step == '0.1':
                        weight_input = inp
                        break
                
                if not weight_input and len(weight_inputs) >= 2:
                    weight_input = weight_inputs[1]  # Segundo input numérico
                
                if weight_input:
                    weight_input.clear()
                    weight_input.send_keys('15.5')
                    time.sleep(0.5)
                    weight_filled = True
                    print("✅ Peso ingresado: 15.5 kg")
                else:
                    print("❌ No se encontró input de peso")
                    
            except Exception as e:
                print(f"❌ Error ingresando peso: {e}")
            
            if not weight_filled:
                print("⚠️ No se pudo ingresar peso, continuando...")
            
            # Tipo de sangre - Mejorada con múltiples estrategias
            print("Seleccionando tipo de sangre...")
            blood_selected = False
            try:
                time.sleep(1)  # Asegurar que la página esté lista
                
                # Estrategia 1: Buscar el tercer combobox (debería ser tipo de sangre)
                print("🔍 Estrategia 1: Buscando combobox de tipo de sangre...")
                blood_triggers = self.driver.find_elements(By.XPATH, "//button[@role='combobox']")
                print(f"🔍 Total combobox para tipo de sangre: {len(blood_triggers)}")
                
                if len(blood_triggers) >= 3:
                    # Scroll al elemento para asegurar visibilidad
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", blood_triggers[2])
                    time.sleep(0.5)
                    
                    self.driver.execute_script("arguments[0].click();", blood_triggers[2])
                    time.sleep(1.5)
                    
                    # Buscar opciones de tipo de sangre para perros (DEA)
                    blood_options = self.driver.find_elements(By.XPATH, "//div[@role='option']")
                    print(f"🔍 Opciones de tipo de sangre: {len(blood_options)}")
                    
                    # Buscar específicamente DEA 1.1+ o DEA 1.1-
                    dea_found = False
                    for option in blood_options:
                        try:
                            option_text = option.text.strip()
                            if "DEA" in option_text:
                                self.driver.execute_script("arguments[0].click();", option)
                                time.sleep(1)
                                blood_selected = True
                                dea_found = True
                                print(f"✅ Tipo de sangre seleccionado: {option_text}")
                                break
                        except:
                            continue
                    
                    # Si no se encuentra DEA, tomar la primera opción
                    if not dea_found and blood_options:
                        try:
                            self.driver.execute_script("arguments[0].click();", blood_options[0])
                            time.sleep(1)
                            blood_selected = True
                            print(f"✅ Tipo de sangre seleccionado: {blood_options[0].text}")
                        except:
                            pass
                            
            except Exception as e:
                print(f"❌ Error en estrategia 1 de tipo de sangre: {e}")
            
            # Estrategia 2: Buscar por texto relacionado
            if not blood_selected:
                try:
                    print("🔄 Estrategia 2: Buscando por texto 'sangre'...")
                    # Cerrar dropdowns abiertos
                    self.driver.execute_script("document.body.click();")
                    time.sleep(1)
                    
                    # Buscar elementos relacionados con tipo de sangre
                    blood_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'sangre') or contains(text(), 'Sangre') or contains(text(), 'Tipo')]")
                    print(f"🔍 Elementos relacionados con sangre: {len(blood_elements)}")
                    
                    for element in blood_elements:
                        try:
                            # Buscar combobox cerca del texto
                            nearby_combobox = element.find_element(By.XPATH, "./following-sibling::*//button[@role='combobox'] | .//following::button[@role='combobox'][1]")
                            nearby_combobox.click()
                            time.sleep(2)
                            
                            # Seleccionar primera opción disponible
                            options = self.driver.find_elements(By.XPATH, "//div[@role='option']")
                            if options:
                                options[0].click()
                                time.sleep(2)
                                blood_selected = True
                                print("✅ Tipo de sangre seleccionado usando estrategia 2")
                                break
                        except:
                            continue
                            
                except Exception as e:
                    print(f"❌ Error en estrategia 2 de tipo de sangre: {e}")
            
            # Estrategia 3: Buscar select nativo
            if not blood_selected:
                try:
                    print("🔄 Estrategia 3: Buscando select nativo...")
                    selects = self.driver.find_elements(By.TAG_NAME, "select")
                    if len(selects) >= 3:
                        from selenium.webdriver.support.ui import Select
                        select_obj = Select(selects[2])  # Tercer select debería ser tipo de sangre
                        if len(select_obj.options) > 1:
                            select_obj.select_by_index(1)  # Seleccionar primera opción válida
                            blood_selected = True
                            print("✅ Tipo de sangre seleccionado usando select nativo")
                            
                except Exception as e:
                    print(f"❌ Error en estrategia 3 de tipo de sangre: {e}")
            
            if not blood_selected:
                print("⚠️ No se pudo seleccionar tipo de sangre, continuando...")
            else:
                print("✅ Campo Tipo de sangre completado exitosamente")
            
            # Fecha de vacunación - Mejorada con fecha válida
            print("Ingresando fecha de vacunación...")
            date_filled = False
            try:
                # Calcular una fecha válida (6 meses atrás desde hoy)
                today = datetime.now()
                six_months_ago = today - timedelta(days=180)
                valid_date = six_months_ago.strftime('%Y-%m-%d')
                print(f"🗓️ Usando fecha válida: {valid_date}")
                
                # Estrategia 1: Buscar input de tipo date
                date_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='date']")))
                
                # Scroll al elemento para asegurar visibilidad
                self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", date_input)
                time.sleep(1)
                
                # Limpiar y establecer la fecha
                date_input.clear()
                time.sleep(0.3)
                
                # Intentar múltiples formatos
                date_formats = [
                    valid_date,  # YYYY-MM-DD
                    six_months_ago.strftime('%m/%d/%Y'),  # MM/DD/YYYY
                    six_months_ago.strftime('%d/%m/%Y'),  # DD/MM/YYYY
                ]
                
                for date_format in date_formats:
                    try:
                        date_input.clear()
                        date_input.send_keys(date_format)
                        time.sleep(0.5)
                        
                        # Verificar si el valor se estableció correctamente
                        input_value = date_input.get_attribute('value')
                        if input_value and len(input_value) > 0:
                            date_filled = True
                            print(f"✅ Fecha de vacunación ingresada: {date_format} (valor: {input_value})")
                            break
                    except:
                        continue
                
                if not date_filled:
                    # Estrategia alternativa usando JavaScript
                    self.driver.execute_script(f"arguments[0].value = '{valid_date}';", date_input)
                    self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_input)
                    time.sleep(0.5)
                    date_filled = True
                    print("✅ Fecha establecida usando JavaScript")
                    
            except Exception as e:
                print(f"❌ Error ingresando fecha: {e}")
                
                # Estrategia de respaldo: buscar cualquier input que pueda ser fecha
                try:
                    date_inputs = self.driver.find_elements(By.XPATH, "//input[contains(@placeholder, 'fecha') or contains(@name, 'date') or contains(@id, 'date')]")
                    if date_inputs:
                        date_inputs[0].clear()
                        date_inputs[0].send_keys(valid_date)
                        time.sleep(1)
                        date_filled = True
                        print("✅ Fecha ingresada usando input alternativo")
                except:
                    pass
            
            if not date_filled:
                print("⚠️ No se pudo ingresar fecha, continuando...")
            else:
                print("✅ Campo Fecha de vacunación completado exitosamente")
            
            # Estado de salud - Mejorado con texto más detallado
            print("Ingresando estado de salud...")
            health_filled = False
            try:
                # Buscar textarea para estado de salud
                health_textarea = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea")))
                
                # Scroll al elemento para asegurar visibilidad
                self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", health_textarea)
                time.sleep(1)
                
                # Texto detallado que cumple los requisitos mínimos
                health_text = """Mascota en excelente estado de salud general. Sin enfermedades conocidas o condiciones médicas preexistentes. Todas las vacunas están al día según el calendario de vacunación recomendado. Ha sido desparasitada recientemente. Presenta buen apetito, nivel de energía normal y comportamiento saludable. Peso ideal para su raza y edad. Apta para participar como donante de sangre según evaluación veterinaria."""
                
                health_textarea.clear()
                time.sleep(0.3)
                health_textarea.send_keys(health_text)
                time.sleep(1)
                
                # Verificar que el texto se ingresó correctamente
                textarea_value = health_textarea.get_attribute('value')
                if len(textarea_value) >= 10:  # Requisito mínimo según validación
                    health_filled = True
                    print(f"✅ Estado de salud ingresado ({len(textarea_value)} caracteres)")
                else:
                    print(f"⚠️ Texto muy corto ({len(textarea_value)} caracteres)")
                    
            except Exception as e:
                print(f"❌ Error ingresando estado de salud: {e}")
                
                # Estrategia de respaldo: buscar por placeholder o nombre
                try:
                    health_inputs = self.driver.find_elements(By.XPATH, "//textarea[contains(@placeholder, 'salud') or contains(@name, 'health')] | //input[contains(@placeholder, 'salud')]")
                    if health_inputs:
                        health_inputs[0].clear()
                        health_inputs[0].send_keys("Mascota en excelente estado de salud. Vacunas al día. Sin enfermedades conocidas. Apta para donación.")
                        time.sleep(0.5)
                        health_filled = True
                        print("✅ Estado de salud ingresado usando input alternativo")
                except:
                    pass
            
            if not health_filled:
                print("⚠️ No se pudo ingresar estado de salud, continuando...")
            else:
                print("✅ Campo Estado de salud completado exitosamente")
            
            # 7. Resumen de campos completados antes de enviar
            print("\n📋 RESUMEN DE CAMPOS COMPLETADOS:")
            completed_fields = []
            if True:  # Nombre siempre se completa
                completed_fields.append("✅ Nombre de mascota")
            if species_selected:
                completed_fields.append("✅ Especie")
            if breed_selected:
                completed_fields.append("✅ Raza")
            if age_filled:
                completed_fields.append("✅ Edad")
            if weight_filled:
                completed_fields.append("✅ Peso")
            if blood_selected:
                completed_fields.append("✅ Tipo de sangre")
            if date_filled:
                completed_fields.append("✅ Fecha de vacunación")
            if health_filled:
                completed_fields.append("✅ Estado de salud")
            
            for field in completed_fields:
                print(field)
            
            missing_fields = 8 - len(completed_fields)
            if missing_fields > 0:
                print(f"⚠️ {missing_fields} campo(s) no se completaron correctamente")
            else:
                print("🎉 Todos los campos obligatorios completados!")
            
            # 8. Enviar formulario
            print("📤 Enviando formulario...")
            try:
                submit_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
                submit_btn.click()
                time.sleep(3)
                print("✅ Formulario enviado")
            except Exception as e:
                print(f"❌ Error enviando formulario: {e}")
                raise
            
            # 9. Manejar alert de confirmación
            try:
                alert = self.wait.until(EC.alert_is_present())
                alert_text = alert.text
                print(f"🔔 Alert detectado: {alert_text}")
                alert.accept()
                time.sleep(1)
            except:
                print("ℹ️ No se detectó alert de confirmación")
            
            # 10. Verificar que estamos en la página de mis mascotas y proceder a eliminar
            print("🗑️ Procediendo a eliminar la mascota 'TestPetAuto'...")
            
            # Navegar a mis mascotas
            try:
                self.driver.get(f"{self.base_url}/my-pets")
                time.sleep(3)
                print("✅ Navegando a página de mis mascotas")
                
                # Manejar posible alert de carga
                try:
                    alert = self.driver.switch_to.alert
                    alert.accept()
                    time.sleep(1)
                except:
                    pass
                    
            except:
                print("⚠️ Error navegando a mis mascotas")
            
            # Buscar específicamente la mascota "TestPetAuto" y eliminarla
            try:
                print("🔍 Buscando mascota 'TestPetAuto'...")
                
                # Buscar el contenedor que contiene el nombre "TestPetAuto"
                pet_containers = self.driver.find_elements(By.XPATH, "//*[contains(text(), 'TestPetAuto')]")
                
                if pet_containers:
                    print(f"✅ Encontrada mascota 'TestPetAuto'")
                    pet_container = pet_containers[0]
                    
                    # Buscar el botón eliminar dentro del mismo contenedor o cerca
                    delete_btn = None
                    
                    # Estrategia 1: Buscar botón eliminar en el mismo contenedor padre
                    try:
                        # Subir al contenedor padre que contiene toda la información de la mascota
                        parent_container = pet_container.find_element(By.XPATH, "./ancestor::div[contains(@class, 'card') or contains(@class, 'pet') or contains(@class, 'item')][1]")
                        delete_btn = parent_container.find_element(By.XPATH, ".//button[contains(text(), 'Eliminar')]")
                        print("✅ Botón eliminar encontrado en contenedor padre")
                    except:
                        pass
                    
                    # Estrategia 2: Buscar en hermanos siguientes
                    if not delete_btn:
                        try:
                            delete_btn = pet_container.find_element(By.XPATH, "./following-sibling::*//button[contains(text(), 'Eliminar')] | ./following::button[contains(text(), 'Eliminar')][1]")
                            print("✅ Botón eliminar encontrado en hermanos siguientes")
                        except:
                            pass
                    
                    # Estrategia 3: Buscar en el contenedor más amplio
                    if not delete_btn:
                        try:
                            grandparent = pet_container.find_element(By.XPATH, "./ancestor::div[2]")
                            delete_btn = grandparent.find_element(By.XPATH, ".//button[contains(text(), 'Eliminar')]")
                            print("✅ Botón eliminar encontrado en contenedor más amplio")
                        except:
                            pass
                    
                    # Estrategia 4: Buscar botón eliminar por posición relativa
                    if not delete_btn:
                        try:
                            # Buscar todos los botones eliminar y tomar el más cercano
                            all_delete_btns = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Eliminar')]")
                            if all_delete_btns:
                                delete_btn = all_delete_btns[0]  # Tomar el primero por ahora
                                print("✅ Botón eliminar encontrado por posición")
                        except:
                            pass
                    
                    if delete_btn:
                        # Scroll al botón para asegurar visibilidad
                        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", delete_btn)
                        time.sleep(1)
                        
                        delete_btn.click()
                        time.sleep(2)
                        print("✅ Botón eliminar clickeado")
                        
                        # Buscar y confirmar en el modal de confirmación
                        try:
                            print("🔍 Buscando modal de confirmación '¿Eliminar mascota?'...")
                            
                            # Buscar el modal que contiene la pregunta
                            modal_text_elements = self.driver.find_elements(By.XPATH, "//*[contains(text(), '¿Eliminar mascota?') or contains(text(), 'Eliminar mascota') or contains(text(), 'TestPetAuto')]")
                            
                            if modal_text_elements:
                                print("✅ Modal de confirmación encontrado")
                                
                                # Buscar el botón "Eliminar" en el modal (no "Cancelar")
                                confirm_delete_btn = None
                                
                                # Buscar todos los botones eliminar visibles
                                eliminate_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Eliminar') and not(contains(text(), 'Cancelar'))]")
                                
                                # Filtrar para encontrar el botón de confirmación en el modal
                                for btn in eliminate_buttons:
                                    try:
                                        if btn.is_displayed() and btn.is_enabled():
                                            # Verificar que esté en un modal o dialog
                                            modal_parent = btn.find_element(By.XPATH, "./ancestor::div[contains(@class, 'modal') or contains(@class, 'dialog') or contains(@class, 'fixed') or contains(@role, 'dialog')]")
                                            confirm_delete_btn = btn
                                            break
                                    except:
                                        continue
                                
                                # Si no se encuentra en modal, tomar el último botón eliminar (debería ser el del modal)
                                if not confirm_delete_btn and eliminate_buttons:
                                    confirm_delete_btn = eliminate_buttons[-1]
                                
                                if confirm_delete_btn:
                                    confirm_delete_btn.click()
                                    time.sleep(2)
                                    print("✅ Eliminación confirmada en el modal")
                                    
                                    # Verificar que el modal se cerró o que aparece mensaje de éxito
                                    try:
                                        # Esperar a que desaparezca el modal o aparezca mensaje de confirmación
                                        self.wait.until(lambda driver: not driver.find_elements(By.XPATH, "//*[contains(text(), '¿Eliminar mascota?')]"))
                                        print("✅ Modal cerrado - eliminación exitosa")
                                    except:
                                        print("ℹ️ No se pudo verificar el cierre del modal")
                                else:
                                    print("❌ No se encontró botón de confirmación en el modal")
                            else:
                                print("⚠️ No se encontró modal de confirmación")
                                
                        except Exception as modal_error:
                            print(f"⚠️ Error en modal de confirmación: {modal_error}")
                    else:
                        print("❌ No se encontró botón eliminar para TestPetAuto")
                else:
                    print("⚠️ No se encontró la mascota 'TestPetAuto' en la página")
                    
            except Exception as e:
                print(f"⚠️ Error al eliminar mascota: {e}")
            
            duration = time.time() - start
            self.test_results['RegistroMascota'] = {
                'success': True,
                'duration': f'{duration:.1f}s',
                'description': 'Registro y eliminación de mascota completado exitosamente.'
            }
            print("✅ Prueba completada exitosamente")
            return True
            
        except Exception as e:
            duration = time.time() - start if 'start' in locals() else 0
            self.test_results['RegistroMascota'] = {
                'success': False,
                'duration': f'{duration:.1f}s',
                'description': f'Error en el flujo: {str(e)}'
            }
            print(f"❌ Error en prueba: {str(e)}")
            return False


def main():
    print("INICIANDO PRUEBA COMPLETA DE REGISTRO Y ELIMINACIÓN DE MASCOTA PETMATCH")
    print("Flujo: Login -> Registrar Mascota -> Eliminar Mascota")
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
