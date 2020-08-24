 # 0x11 - Python - Network #1
Task # | Short Description
-------|------------
[Task 0](0-hbtn_status.py) | Fetch `https://intranet.hbtn.io/status` using `urllib`.
[Task 1](1-hbtn_header.py) | Takes in URL, sends request to URl and displays the value of the `X-Request-Id` variable found in the header of the response.
[Task 2](2-post_email.py) | Takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, & display body of response (decoded in `utf-8`)
[Task 3](3-error_code.py) | Takes in URL, sends request to the URL, displays body of response, decoded. Manage `urllib.error.HTTPError`.
[Task 4](4-hbtn_status.py) | Fetches `https://intranet.hbtn.io/status` using package `requests`.
[Task 5](5-hbtn_header.py) | Takes in a URL, sends request to the URL & displays the value of the variable `X-Request-Id` in the response header using `requests` and `sys`.
[Task 6](6-post_email.py) | Takes in a URL and an email address, sends a `POST` request with passed URL with email as parameter, and displays the body of the response using `requests` and `sys`. Sent in variable `email`
[Task 7](7-error_code.py) | Takes in a URL, sends a request to the URL and displays the body of the response using `requests` and `sys`. Handle HTTP status codes >= 400.
[Task 8](8-json_api.py) | Takes in a letter & sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.
[Task 9](10-my_github.py) | Takes your Github credentials & use Github API to display your `id`. Must use [Basic Authentication](https://intranet.hbtn.io/rltoken/y0JChY0j1qfjFVcQzsD3jw) with a [personal access token as password](https://intranet.hbtn.io/rltoken/1ziOM17p1uVxvEYSYlkG3Q) to access to your information using `requests` and `sys`.
 ## Lessons Learned
* How to fetch internet resources with the Python package `urllib`
* How to decode `urllib` body response
* How to use the Python package `requests` #requestsiswayssimplerthenurllib
* How to make HTTP `Get` request
* How to make HTTP `POST`/`PUT`/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service
