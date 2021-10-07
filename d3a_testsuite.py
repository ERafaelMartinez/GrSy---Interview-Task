import unittest
import pages
from selenium import webdriver


class d3a_basic_testsuite(unittest.TestCase):

    def setUp(self):
        PATH = "/Users/rafael/Applications/WebScraping/chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("http://www.d3a.io/login")

    def test_login(self):

        # GIVEN - login data
        email = "rafamartinez@live.com.mx"
        kennwort = "GridSingularity_04.10.21"
        account_data = {'email': email, 'password': kennwort}

        # WHEN - login performed
        loginPage = pages.LoginPage(self.driver)

        # THEN
        successLogin = loginPage.login(account_data)
        assert successLogin

    def test_new_project(self):

        # GIVEN - a successful login and project name & description
        self.test_login()
            # project data
        project_name = "TestProject_Rafael"
        project_description = "This is a test project created to test the website's functionalities."
        project_details = {'name': project_name, 'description': project_description}

        # WHEN - in projects page, create project
        projectsPage = pages.ProjectsPage(self.driver)
        successNewProject = projectsPage.new_proyect(project_details)

        # THEN - True = Project Created Successfuly, listed on page.

        assert successNewProject

    def test_new_simulation(self):

        # GIVEN - a logeed account, project details and simulation setup specs
        self.test_new_project()

            # simulation data
        simulations_name = 'Test Simulation'
        simulation_setup = {'name': simulations_name}

        # project data
        project_name = "TestProject_Rafael"
        project_description = "This is a test project created to test the website's functionalities."
        project_details = {'name': project_name, 'description': project_description}

        # WHEN - login performed
        projectMenuPage = pages.ProjectMenuPage(self.driver)

        # THEN
        successSimulation = projectMenuPage.new_simulation(project_details['name'], simulation_setup)

        assert successSimulation

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
