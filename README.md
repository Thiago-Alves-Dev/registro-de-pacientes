# registro-de-pacientes

Um programa de registro de pacientes desenvolvido em Python, que utiliza o terminal como
interface para entrada de dados. Este código simples permite que os usuários adicionem
informações de pacientes de forma conveniente, armazenando esses dados em um arquivo de
texto para fácil acesso e gerenciamento. Ao executar o programa, você será guiado
passo a passo para inserir os dados relevantes de cada paciente, os detalhes do paciente
serão automaticamente registrados no arquivo .txt, garantindo uma organização eficiente
e uma maneira simplificada de acompanhar e atualizar os registros médicos.

O código também possui uma função embutida que automatiza o cálculo da idade atual do
paciente com base na data de nascimento fornecida durante o cadastro. Isso significa
que, ao inserir a data de nascimento de um paciente, o programa imediatamente
determina sua idade atual, eliminando a necessidade de cálculos manuais ou inserção
adicional de dados. 

Além disso, o código inclui uma lógica adicional para identificar pacientes idosos com
65 anos ou mais e automaticamente classificá-los em um grupo de risco. Quando um 
paciente é cadastrado e sua idade é verificada, o programa utiliza uma estrutura de
controle condicional (if-else) para direcionar os pacientes elegíveis para o grupo de
risco para um arquivo de texto separado. Essa funcionalidade é crucial para fornecer
uma resposta específica às necessidades dos pacientes idosos, garantindo que sua
saúde e segurança sejam priorizadas.
