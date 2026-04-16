from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_todo_list(self):

        # O jovem Marcos ouviu falar de um novo app online de tarefas
        # Ele foi saber mais acessando a pagina do app
        self.browser.get("http://localhost:8000")

        # Ele percebe que o titulo da pagina menciona a lista de tarefas
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text  
        self.assertIn("To-Do", header_text)

        # Ele é convidade a inserir um item na lista de forma imediata
        inputbox = self.browser.find_element(By.ID, "id_new_item")  
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # Calmamente ele digita "Comprar um novo curso" na caixa de texto
        # (Marcos tem um estranho vicio em comprar cursos)
        inputbox.send_keys("Buy peacock feathers")

        # Quanto ele aperta enter, a pagina atualiza, e agora ela lista
        # "1: Comprar um novo curso sobre desenvolvimento" como um item na lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table("1: Buy peacock feathers")

        # A caixa de texto continua ali, convidando-o a inserir um novo item
        # Então ele insere um novo item "2: Decidir qual o tema do curso"
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # A pagina é atualizada novamente, a agora exibe ambos os itens na lista dele
        self.check_for_row_in_list_table("2: Use peacock feathers to make a fly")
        self.check_for_row_in_list_table("1: Buy peacock feathers")
  
        # Satisfeito, ele decide ir tirar um cochilo.



if __name__ == "__main__":
    unittest.main()