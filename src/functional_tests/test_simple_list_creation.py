from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from .base import FunctionalTest


class NewVisitorTest(FunctionalTest):
    def test_can_start_a_todo_list(self):

        # O jovem Marcos ouviu falar de um novo app online de tarefas
        # Ele foi saber mais acessando a pagina do app
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # A caixa de texto continua ali, convidando-o a inserir um novo item
        # Então ele insere um novo item "2: Decidir qual o tema do curso"
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        # A pagina é atualizada novamente, a agora exibe ambos os itens na lista dele
        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
  
        # Satisfeito, ele decide ir tirar um cochilo.

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy peacock feathers")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")

        # She notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, "/lists/.+")

        
        # Now a new user, Francis, comes along to the site.

        ## We delete all the browser's cookies
        ## as a way of simulating a brand new user session  
        self.browser.delete_all_cookies()

        # Francis visits the home page.  There is no sign of Edith's
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Buy peacock feathers", page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Buy milk")

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, "/lists/.+")
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element(By.TAG_NAME, "body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertIn("Buy milk", page_text)

        # Satisfied, they both go back to sleep