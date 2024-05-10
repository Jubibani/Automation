from seleniumbase import BaseCase
from seleniumbase import Driver
import time

github_driver = Driver(uc=True)
BaseCase.main(__name__, __file__, "--uc", "-s", "--incognito")
class UndetectedGitHubLogin(BaseCase):
    def login_to_github_using_quickie(self):
        # # Open a new browser window
        # github_driver.execute_script("window.open();")
        # #Switch to the newly opened window
        # github_driver.switch_to.window(github_driver.window_handles[1])

        # #Navigate to Github
        url = "https://github.com/"
        github_driver.open_new_window(url)
        github_driver.uc_open_with_reconnect(url, 3)
        # Implement delay to wait for booting process
        time.sleep(2)

        # Click the "Sign in" button
        github_driver.wait_for_element('a.HeaderMenu-link[href="/login"]')
        github_driver.click('a.HeaderMenu-link[href="/login"]')
        print("Sign-in Button Clicked")

    # Username and password for GitHub
        #Enter your Username
        github_driver.wait_for_element("#login_field")
        github_driver.type("#login_field", "...")

        #Enter your Password
        github_driver.wait_for_element("#password")
        github_driver.type("#password", "...")

        print("Username and password successfully entered!")

        # Click the Sign-in button
        github_driver.wait_for_element('input[value="Sign in"]')
        github_driver.click('input[value="Sign in"]')
        print("Sign-in Button Clicked")

        # Implement delay
        time.sleep(2)

        # Find the link by its data-test-selector attribute
        github_driver.wait_for_element('a[data-test-selector="gh-mobile-link"]')
        # Click the link
        github_driver.click('a[data-test-selector="gh-mobile-link"]')
        print("You should be logged in to your GitHub By Now!")


if __name__ == "__main__":
    # Call the function to log in to GitHub
    UndetectedGitHubLogin().login_to_github_using_quickie()
