from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from database import *

warframes = {'атлас': 'atlas', 'банши': 'banshee', 'баруук': 'baruuk', 'валькирия': 'valkyr', 
'висп': 'wisp', 'вобан': 'vauban', 'вольт': 'volt', 'вуконг': 'wukong', 'гара': 'gara', 
'гаруда': 'garuda', 'гидроид': 'hydroid', 'грендель': 'grendel', 'зефир': 'zephyr', 'ивара': 'ivara', 
'инарос': 'inaros', 'кора': 'khora', 'лимбо': 'limbo', 'локи': 'loki', 'мираж': 'mirage', 'миса': 'mesa', 
'мэг': 'mag', 'некрос': 'nekros', 'нидус': 'nidus', 'никс': 'nyx', 'нова': 'nova', 'нэчжа': 'nezha', 
'оберон': 'oberon', 'октавия': 'octavia', 'ревенант': 'revenant', 'рино': 'rhino', 'сарина': 'saryn', 
'титания': 'titania', 'тринити': 'trinity', 'фрост': 'frost', 'харроу': 'harrow', 'хильдрин': 'hildryn', 
'хрома': 'chroma', 'эквинокс': 'equinox', 'эмбер': 'ember', 'эш': 'ash'}

def get_frame_name(frame):
    frame = frame.lower().split()[0]
    if frame in warframes.keys():
        return warframes[frame]
    if frame not in warframes.values():
        return "frame_missing"
    return frame

def find_prices(frame):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")  # Добавьте этот аргумент, если возникают проблемы с shared memory
    chrome_options.add_argument("--no-sandbox")  # И этот аргумент для безопасности
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    items = ["_prime_set","_prime_blueprint","_prime_neuroptics_blueprint","_prime_systems_blueprint","_prime_chassis_blueprint"]
    prices = []
    for item in items:
        url = "https://warframe.market/items/" + frame + item
        driver.get(url)
        prices.append(int(driver.find_element(By.CLASS_NAME, "price").text))
    update_database(frame, prices)
