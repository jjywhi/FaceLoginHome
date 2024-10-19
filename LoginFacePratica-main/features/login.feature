Feature: Login no Facebook

  Scenario: Login com credenciais corretas
    Given que o usuário está na página de login do Facebook
    When o usuário insere um e-mail válido "bddtestesvalidos@outlook.com"
    And o usuário insere uma senha válida "testesvalidos1"
    And o usuário clica no botão "Entrar"
    Then o usuário deve ser redirecionado para a página inicial do Facebook
    
  Scenario: Login com credenciais inválidas
    Given que o usuário está na página de login do Facebook
    When o usuário insere um e-mail inválido "invalido@exemplo.com"
    And o usuário insere uma senha inválida "senhaInvalida"
    And o usuário clica no botão "Entrar"
    Then uma mensagem de erro deve ser exibida
