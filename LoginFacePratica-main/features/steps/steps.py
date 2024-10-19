from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot
import os

CHROMEDRIVER_PATH = 'chromedriver.exe'

@given('que o usuário está na página de login do Facebook')
def step_given_usuario_na_pagina_de_login(context):
    service = Service(CHROMEDRIVER_PATH)
    context.driver = webdriver.Chrome(service=service)
    context.driver.get("https://www.facebook.com")

@when('o usuário insere um e-mail válido "{email}"')
def step_when_usuario_insere_email(context, email):
    email_field = context.driver.find_element(By.ID, "email")
    email_field.send_keys(email)

@when('o usuário insere uma senha válida "{senha}"')
def step_when_usuario_insere_senha(context, senha):
    senha_field = context.driver.find_element(By.ID, "pass")
    senha_field.send_keys(senha)

@when('o usuário clica no botão "Entrar"')
def step_when_usuario_clica_entrar(context):
    entrar_button = context.driver.find_element(By.NAME, "login")
    context.driver.execute_script("arguments[0].click();", entrar_button)

@then('o usuário deve ser redirecionado para a página inicial do Facebook')
def step_then_usuario_redirecionado_pagina_inicial(context):
    try:
        print("Verificando título da página...")
        WebDriverWait(context.driver, 50).until(EC.title_contains("Facebook"))
        assert "Facebook" in context.driver.title
        print("Título verificado com sucesso.")
        take_screenshot(context.driver, "login_sucesso")
    except Exception as e:
        print(f"Erro ao verificar o título: {e}")
        take_screenshot(context.driver, "login_falha")
        raise e
    finally:
        context.driver.quit()


@when('o usuário insere um e-mail inválido "{email}"')
def step_when_usuario_insere_email_invalido(context, email):
    email_field = context.driver.find_element(By.ID, "email")
    email_field.send_keys(email)

@when('o usuário insere uma senha inválida "{senha}"')
def step_when_usuario_insere_senha_invalida(context, senha):
    senha_field = context.driver.find_element(By.ID, "pass")
    senha_field.send_keys(senha)

@then('uma mensagem de erro deve ser exibida')
def step_then_mensagem_erro_exibida(context):
    try:
        error_message = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="email_container"]/div[2]'))
        )
        assert error_message.is_displayed()
        take_screenshot(context.driver, "erro_login")
    except Exception as e:
        take_screenshot(context.driver, "erro_login_falha")
        raise e
    finally:
        context.driver.quit()
