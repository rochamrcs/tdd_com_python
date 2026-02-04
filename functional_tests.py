import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):

        # O jovem Marcos ouviu falar de um novo app online de tarefas
        # Ele foi saber mais acessando a pagina do app
        self.browser.get("http://localhost:8000")

        # Ele percebe que o titulo da pagina menciona a lista de tarefas
        self.assertIn("To-Do", self.browser.title)

        # Ele é convidade a inserir um item na lista de forma imediata
        self.fail("Finish the test!")

        # Calmamente ele digita "Comprar um novo curso" na caixa de texto
        # (Marcos tem um estranho vicio em comprar cursos)

        # Quanto ele aperta enter, a pagina atualiza, e agora ela lista
        # "1: Comprar um novo curso sobre desenvolvimento" como um item na lista de tarefas

        # A caixa de texto continua ali, convidando-o a inserir um novo item
        # Então ele insere um novo item "2: Decidir qual o tema do curso"

        # A pagina é atualizada novamente, a agora exibe ambos os itens na lista dele

        # Satisfeito, ele decide ir tirar um cochilo.

if __name__ == "__main__":
    unittest.main()