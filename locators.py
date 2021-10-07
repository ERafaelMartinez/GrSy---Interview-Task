from selenium.webdriver.common.by import By

class LoginPageLocators(object):

     EMAIL_INPUT = (By.ID, "email")
     PASSWORD_INPUT = (By.ID, "password")
     LOGIN_BUTTON = (By.CLASS_NAME, "button.button.button--accent")

class ProjectsPageLocators(object):

    NEW = (By.CLASS_NAME, "button.button.button--accent.button-icon")
    NEW_NAME_INPUT = (By.ID, "input-field-name")
    NEW_DESCRIPTION_INPUT = (By.ID, "textarea-field-nameTextArea")
    ADD_NEW = (By.XPATH, '/html/body/div[5]/div/div/div[2]/button')

    SAVED_PROJECTS = (By.XPATH, '''//*[@id='root']/div/div[2]/div[2]/div/div/section''')

    def get_name(self, index):
        i = index
        return (By.XPATH, '''//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[{}]/div/div[1]/span/span'''.format(i))

class ProjectMenuLocators(object):

    def open(self, index):
        return (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div/section/div[{}]/div/div[1]/span".format(index))

    def new_simulation(self, index):
        return (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div/section/div[{}]/div[2]/button".format(index))

    INPUT_SIMULATION_NAME = (By.ID, "input-field-name")

    def saved_simulations(self, index):
        return (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/section/div[{}]/div[2]/div".format(i))

    NEXT = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div/div/div[2]/button")










