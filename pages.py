from locators import *
import time

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def click_login_button(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()

    def input_email(self, email):
        element = self.driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        element.send_keys(email)

    def input_password(self, password):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        element.send_keys(password)

    def login(self, account_data):
        '''
        :param account_data: dict('email', 'password') email and password of the account.
        :return: True = success, False = fail
        '''

        try:
            email = account_data['email']
            password = account_data['password']

            self.input_email(email)
            self.input_password(password)
            self.click_login_button()
            time.sleep(3)

            return True
        except Exception as e:
            print(e)
            return False


class ProjectsPage(BasePage):

    def click_new_project(self):
        self.driver.get("http://d3a.io/projects")
        time.sleep(1)
        element = self.driver.find_element(*ProjectsPageLocators.NEW)
        element.click()

    def input_project_name(self, name):
        time.sleep(1)
        element = self.driver.find_element(*ProjectsPageLocators.NEW_NAME_INPUT)

        element.clear()
        time.sleep(3)
        element.send_keys(name)

    def input_project_description(self, description):
        element = self.driver.find_element(*ProjectsPageLocators.NEW_DESCRIPTION_INPUT)
        element.clear()
        time.sleep(3)
        element.send_keys(description)

    def add_new_project(self):
        element = self.driver.find_element(*ProjectsPageLocators.ADD_NEW)
        element.click()
        time.sleep(1)

    def project_on_list(self, project_name, output='status'):
        '''
        Function checks if a project is listed. Must be excecuted after a succesful login on the projects page.
        :param project_name: name of the project.
        :param output: determines wether it returns a boolean or the index of the project in the list.
                        output = 'status', returns bool.
                        output = 'index', returns index
        :return: bool, index, None
        '''

        saved_projects = self.driver.find_element(*ProjectsPageLocators.SAVED_PROJECTS)

        projects = saved_projects.find_elements_by_tag_name("div")

        for i in range(1, len(projects)):
            locators_temp = ProjectsPageLocators()
            name = self.driver.find_element(*locators_temp.get_name(index=i))
            #print(name.text)

            if name.text == project_name:
                if output == 'status':
                    return True
                elif output == 'index':
                    return i
            else:
                continue

        if output == 'status':
            return False
        elif output == 'index':
            return None

    def new_proyect(self, project_details):
        '''
        Function creates a new project given a name and a description. It should be run
        in the projects page after a succesful login.
        :project_details: dict('name', description'), project name and description.
        :return: True = succesful project creation, False = project creation failed
        '''

        #click on new project
        self.click_new_project()
        time.sleep(1)

        #fill project data
        self.input_project_name(project_details['name'])
        self.input_project_description(project_details['description'])

        #add new project
        self.add_new_project()

        if self.project_on_list(project_details['name'], output='status'):
            #print('New project is listed correctly.')
            return True
        else:
            #print('New project is not on list.')
            return False

class ProjectMenuPage(ProjectsPage, BasePage):


    def open_project_menu(self, index):
        self.driver.get("https://www.d3a.io/projects")
        self.locators_temp = ProjectMenuLocators()
        time.sleep(3)
        element = self.driver.find_element(*self.locators_temp.open(index))
        element.click()

    def click_new_simulation(self, index):
        time.sleep(1)
        element = self.driver.find_element(*self.locators_temp.new_simulation(index))
        element.click()

    def click_next_setup(self):
        time.sleep(1)
        element = self.driver.find_element(*ProjectMenuLocators.NEXT)
        element.click()

    def input_simulations_name(self, name):
        element = self.driver.find_element(*ProjectMenuLocators.INPUT_SIMULATION_NAME)
        time.sleep(1)
        element.clear()
        time.sleep(2)
        element.send_keys(name)


    def new_simulation(self, project_name, simulation_setup):
        '''
        Function creates a new simulation given a user and project specs.
        Execution must start on project page.
        :param project_name:
        :param simulation_setup:
        :return:
        '''


        if self.project_on_list(project_name, 'status'):  # checks if requested project is on the list. If so, enters conditional.

            i = self.project_on_list(project_name, 'index')  # retrieves the index which occupies on the list.

            self.open_project_menu(i)

            self.click_new_simulation(i)
            time.sleep(1)

            self.setup(simulation_setup)  # adds a particular setup (optional)

            self.click_next_setup()
            time.sleep(3)

            self.add_node()  # add a node is an optional feature configuration.

            self.driver.get("https://www.d3a.io/projects")  # goes to project page to validate listed simulation

            # once the simulation has been created, it validates it appears on the list.
            #print('is it on list?')
            stat = self.simulation_on_list( simulation_setup, i, 'status')

            if stat:
                #print('New simulation is listed correctly.')
                return True
            else:
                #print('New simulation is not on list.')
                return False

        else:
            print('Project does not exist')

    def simulation_on_list(self, simulation_setup, project_index, output='status'):
        '''
        Function checks if a simulation is listed within a given project. Should be excecuted after a succesful login.
        :param simulation_setup: simulations setup.
        :param project_index: information about project.
        :param output: determines wether it returns a boolean or the index of the project in the list.
        :return: bool.
        '''

        i = project_index

        self.driver.get("https://www.d3a.io/projects")
        self.open_project_menu(i)

        for j in range(0, 1):
            name_simulation = self.driver.find_element_by_xpath(
                '''//*[@id="root"]/div/div[2]/div[2]/div/div/section/div[{}]/div[2]/div/div[{}]/div/div[1]/div[1]/div/p'''.format(
                    i, j + 1))
            #print(name_simulation.text)
            if name_simulation.text == simulation_setup['name']:
                if output == 'status':
                    return True
                elif output == 'index':
                    return i
            else:
                continue

        if output == 'status':
            return False
        elif output == 'index':
            return None

    def setup(self, simulation_setup):
        name = simulation_setup['name']
        self.input_simulations_name(name)


    def add_node(self):
        pass



