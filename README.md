# DIO-Desafio-Ransomware-e-Keylogger
Este repositório foi criado para atender ao desafio proposto:
Optei por focar em:
- Estudar o funcionamento de ransomware e keyloggers;
- Entender os riscos e impactos dessas ameaças;
- Investigar boas práticas de prevenção, detecção e resposta;
- Registrar aqui minhas reflexões, anotações e aprendizados.


O que é um Ransomware?
Ransomware é um tipo de malware que:
1. Geralmente infecta o sistema por:
- Phishing (e-mails com anexos ou links maliciosos),
- Downloads de sites inseguros,
- Exploração de vulnerabilidades.

2. Busca e criptografa arquivos importantes da vítima.

3. Exibe uma mensagem de resgate, pedindo pagamento (frequentemente em criptomoedas) para supostamente restaurar o acesso.

Pontos que estudei
- Ransomware “simples” (criptografa com chave fixa ou fraca),
- Ransomware mais avançado (uso de chaves únicas por vítima, C2 etc.).
- Estratégias de propagação (por rede, pendrives, RDP vulnerável, etc.).
- Impactos em: usuários domésticos e empresas.


O que é um Keylogger?
Um keylogger é um software (ou até hardware) que registra tudo o que o usuário digita:
- Pode ser usado com finalidade legítima (ex.: auditoria corporativa, testes de usabilidade);
- Mas é mais conhecido pelo uso malicioso:
- Roubo de senhas,
- Dados bancários,
- Informações pessoais sensíveis.

Pontos que estudei
- Tipos de keylogger:
- baseado em sistema operacional (hooks de teclado, APIs de input),
- baseado em navegador (injeção de scripts),
- baseado em hardware (dispositivos entre teclado e computador).
- Como malware costuma usar keyloggers:
- como módulo dentro de trojans;
- como parte de campanhas de phishing.
- Riscos de privacidade e segurança.


Defesa: Como se Proteger
Como parte do desafio, estudei medidas de prevenção e mitigação, incluindo:
- Manter sistema operacional e softwares sempre atualizados;
- Usar antivírus/antimalware confiáveis;
- Fazer backup regular dos dados (e testar a restauração!);
Cuidados com:
- Anexos de e-mail não solicitados,
- Links encurtados ou suspeitos,
- Downloads de fontes desconhecidas.

Medidas específicas contra Ransomware
- Uso de backup offline ou em soluções imutáveis;
- Restringir permissões de usuário (não usar admin no dia a dia);
- Segmentação de rede em ambientes corporativos;
- Monitoramento de comportamentos suspeitos (muitos arquivos sendo alterados rapidamente, por exemplo).

Medidas específicas contra Keyloggers
- Utilizar ferramentas de segurança com **detecção de keylogger**;
- Verificar regularmente processos e programas em execução;
- Evitar instalar softwares de origem duvidosa;
- Ativar autenticação em duas etapas (2FA) para reduzir impacto do roubo de senhas.


Reflexões
Algumas percepções que tive durante o estudo:
- Todos estamos sujeitos a ataques de ransomware e keyloggers;
- Segurança não é só ferramenta, é hábito;
- Devemos desconfiar de anexos enviados de remetentes desconhecidos;
- Manter uma rotina de backup;
- É importante manter o sistema operacional e antivírus sempre atualizados;
- Entender como funciona um malware nos ajude a evitar e nos defender.
