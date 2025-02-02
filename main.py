from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Objetivo: 

navegador = webdriver.Chrome()

produtos = []

def func_input(input):
    input.click()
    input.send_keys(elemento_pesquisado) 
    input.send_keys(Keys.ENTER)

def centro_de_tratamento(nome, preco):
    preco = preco.text.strip()
    preco_convertido = int(float(preco.replace("R$", "").strip().replace(".", "").replace(",", ".")))
    
    produto = {"nome": nome, "preco": preco_convertido}
    produtos.append(produto)

def mercado_livre():
    navegador.get("https://www.mercadolivre.com.br")
    navegador.maximize_window()
    input = navegador.find_element(By.CLASS_NAME, "nav-search-input")
    func_input(input)
    msg_de_nao_encontrado = navegador.find_element(By.CLASS_NAME, "ui-search-rescue__title")
    if msg_de_nao_encontrado:
        return "Nada aqui"
    else:
        item = navegador.find_element(By.CLASS_NAME, "poly-component__title-wrapper")
        item.click()
        item_preco_mercado = navegador.find_element(By.CLASS_NAME, "andes-money-amount__fraction")
        centro_de_tratamento("Mercado Livre", item_preco_mercado)

def mamazon():
    navegador.get("https://https://www.amazon.com.br")
    navegador.maximize_window()
    input = navegador.find_element(By.ID, "twotabsearchtextbox")
    func_input(input)
    msg_de_nao_encontrado = navegador.find_element(By.CLASS_NAME, "a-size-medium a-color-base")
    if msg_de_nao_encontrado:
        return "Nada aqui"
    else:
        item = navegador.find_element(By.CLASS_NAME, "a-section aok-relative s-image-square-aspect")
        item.click()
        item_preco_mamazon = navegador.find_element(By.CLASS_NAME, "a-price-whole")
        centro_de_tratamento("Amazon", item_preco_mamazon)

def ali_express():
    navegador.get("https://pt.aliexpress.com")
    navegador.maximize_window()
    input = navegador.find_element(By.CLASS_NAME, "search--keyword--15P08Ji")
    func_input(input)
    msg_de_nao_encontrado = navegador.find_element(By.CLASS_NAME, "main2023--sorry--1DAkjAv")
    if msg_de_nao_encontrado:
        return "Nada aqui"
    else:
        item = navegador.find_element(By.CLASS_NAME, "list--gallery--C2f2tvm search-item-card-wrapper-gallery")
        item.click()
        item_preco_ali = navegador.find_element(By.CLASS_NAME, "price--currentPriceText--V8_y_b5 pdp-comp-price-current product-price-value")
        centro_de_tratamento("Ali Express",item_preco_ali)
    
    
def americanas():
    navegador.get("https://www.americanas.com.br")
    navegador.maximize_window()
    input = navegador.find_element(By.CLASS_NAME, "search__InputUI-sc-1wvs0c1-2 dRQgOV")
    func_input(input)
    msg_de_nao_encontrado = navegador.find_element(By.CLASS_NAME, "src__HeroTitle-sc-1ucxfc6-2 huVety")
    if msg_de_nao_encontrado:
        return "Nada aqui"
    else:
        item = navegador.find_element(By.CLASS_NAME, "inStockCard__Wrapper-sc-1ngt5zo-0 iRvjrG")
        item.click()
        item_preco_americanas = navegador.find_element(By.CLASS_NAME, "styles__PriceText-sc-1o94vuj-0 kbIkrl priceSales")
        centro_de_tratamento("Americanas",item_preco_americanas)
    
def terabyte():
    navegador.get("https://www.terabyteshop.com.br")
    navegador.maximize_window()
    input = navegador.find_element(By.ID, "isearch")
    func_input(input)
    msg_de_nao_encontrado = navegador.find_element(By.CLASS_NAME, "busca-zerada")
    if msg_de_nao_encontrado:
        return "Nada aqui"
    else:
        item = navegador.find_element(By.CLASS_NAME, "product-item__grid")
        item.click()
        item_preco_terabyte = navegador.find_element(By.CLASS_NAME, "tit-prod")
        centro_de_tratamento("Terabyte", item_preco_terabyte)
    
    
def kabum():
    navegador.get("https://www.kabum.com.br")
    navegador.maximize_window()
    input = navegador.find_element(By.ID, "input-busca")
    func_input(input)
    msg_de_nao_encontrado = navegador.find_element(By.XPATH, "//*[@id='listingEmpty']/b")
    if msg_de_nao_encontrado:
        return "Nada aqui"
    else:
        item = navegador.find_element(By.CLASS_NAME, "p-[2px] rounded-4 group bg-white shadow-[0_0_1px_rgba(40,41,61,0.08),0_0.5px_2px_rgba(96,97,112,0.16)] hover:shadow-lg")
        item.click()
        item_preco_kabum = navegador.find_element(By.CLASS_NAME, "sc-5492faee-2 ipHrwP finalPrice")
        centro_de_tratamento("Kabum", item_preco_kabum)
        
    

def pichau():
    navegador.get("https://www.pichau.com.br")
    navegador.maximize_window()
    input = navegador.find_element(By.XPATH,"//*[@id='mui-95382']")
    func_input(input)
    
    msg_de_nao_encontrado = navegador.find_element(By.XPATH, "//*[@id='__next']/div[1]/main/div[2]/div/div/div[4]/div/p")
    if msg_de_nao_encontrado == "Nenhum produto encontrado.":
        return "Nada aqui"
    else:
        item = navegador.find_element(By.CLASS_NAME,  "MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-md-4 MuiGrid-grid-lg-3 MuiGrid-grid-xl-2")
        item.click()
        item_preco_pichau = navegador.find_element(By.CLASS_NAME, "jss983")
        centro_de_tratamento("Pichau", item_preco_pichau)
        
    
def mostrar_resultados():
    if not produtos:
        print("\nNenhum produto encontrado.")
        return
        
    # Ordena a lista de produtos pelo preço (crescente)
    produtos_ordenados = sorted(produtos, key=lambda x: x["preco"])
        
    print("\n========= RESULTADOS =========")
    for produto in produtos_ordenados:
        print(f"{produto['nome']}: R$ {produto['preco']}")


def tecnologia():
    kabum()
    pichau()
    ali_express()
    mamazon()
    mercado_livre()
    mostrar_resultados()
    
def geral():
    mamazon()
    ali_express()
    mercado_livre()
    mostrar_resultados()
    
    
    
menu = int(input("""
                 ----------------------- Preço finder -----------------------
                 
                 [1] Geral
                 [2] Tecnologia
                 """))

if menu:
    pass
else:
    menu = int(input("""
                 ----------------------- Preço finder -----------------------
                 
                 [1] Geral
                 [2] Tecnologia
                 """))

if menu == 1:
    elemento_pesquisado = input("Escolha o produto para economizar:")
    geral()
else:
    elemento_pesquisado = input("Escolha o produto para economizar:")
    tecnologia()