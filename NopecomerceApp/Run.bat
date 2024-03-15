pytest -v -m "sanity" --html=Reports\report.html testCases --browser chrome
pytest -v -m "regression" --html=Reports\report.html testCases --browser chrome
pytest -v -m "Edit" --html=Reports\report.html testCases --browser chrome
pytest -v -m "Delete" --html=Reports\report.html testCases --browser chrome