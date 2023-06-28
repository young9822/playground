# Young's Playground
Here is Young's playground for testing with automation. Please refer to the following for the detail.

## Case 1: Page Object Model
A page object is an object-oriented class that serves as an interface to a page of your AUT. The tests then use the methods of this page object class whenever they need to interact with the UI of that page. The benefit is that if the UI changes for the page, the tests themselves don’t need to change, only the code within the page object needs to change. 

:octocat: Python, Pytest, Selenium, POM

## Case 2: Playwright vs. Selenium
This [website](http://www.uitestingplayground.com/home) (not from me) is specially designed to exercise the special cases such as dynamic ID, hidden button, hidden layers, load delay, which has difficult cases to handle with. I developped the sample test scripts with both Playwright and Selenium to compare. I was able to handle them by both Playwright and Selenium but the way to handle were a bit different from each other. And you can find pros and cons of each framework via these samples. Do you think which is better?

:octocat: Python, Pytest, Playwright, Selenium, Docker, Docker-Compose

## Case 3: Playwright Exercises
I found another [website](https://the-internet.herokuapp.com) (thank you), which is specially designed to exercise the special cases similar to Case 2. It has lots of interesting cases which will be helpful to increase your understanding for Playwright.

:octocat: Python, Pytest, Playwright