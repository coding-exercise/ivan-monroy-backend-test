## Python 3.9.0

The app needs **Python 3.9.0**. We use the new dictionary *union
operators*. See:

  - <https://www.python.org/downloads/release/python-390/>

  - <https://www.python.org/dev/peps/pep-0584/>

If it's not possible to have 3.9.0 on your system, please apply the
following patch to the `main.py` file:

``` example
-        # ☢☢ This needs Python 3.9.0 ☢☢
-        return build_statistics_dictionary(text_split) | {'vocabulary_list': vocabulary_list(text_split)}
-        # ☢☢ This needs Python 3.9.0 ☢☢
+        a = build_statistics_dictionary(text_split)
+        b = {'vocabulary_list': vocabulary_list(text_split)}
+        return {**a, **b}
```

For convenience, we include a `main-patched.py` file.

## Dependencies

We can use `pip` to install the dependencies:

``` bash
pip install -r requirements.txt
```

## Run locally

The app can be run locally with the following command:

``` bash
uvicorn main:app --reload
```

Once the app is up, `curl` invocations could look like the following:

``` bash
curl -H 'Accept: application/json' -H "Content-Type:application/json" -d '{ "text" : "shoce pq podciy nfwh phfer epgdc" }' http://localhost:8000/parse
```

## Tests

We use `pytest` for testing. To run the tests, issue the `pytest` command from the root directory:

``` bash
pytest
```

We propose 2 types of tests:

1.  [test\_utils.py](test_utils.py) This file contains unit tests
    for the functions in the `utils.py`. For instance, we can test the
    function that decides whether or not a word is a preposition.

2.  [test\_endpoint.py](test_endpoint.py) This file tests the
    `parse` endpoint. Our testsuite includes *Test Case A* and *Test Case B*
    from the provided PDF instructions.
