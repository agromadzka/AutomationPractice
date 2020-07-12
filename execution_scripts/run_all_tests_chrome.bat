cd ..
(
@echo base_url = "http://automationpractice.com/index.php"
@echo test_browser = "chrome"
@echo screenshot_path = "C:\\Screenshots\\AutomationPractice\\"
) > config.py
python -m pytest -v -s -n 2 --reruns 2 --html=C:\Reports\AutomationPractice\report.html --self-contained-html --capture=sys tests
