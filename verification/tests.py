"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [4, [1, 2, 1, 2]],
            "answer": "S"
        },
        {
            "input": [5, [1, 2, 1.5, 1, 2]],
            "answer": "S"
        },
        {
            "input": [4, [1, 2, 2, 1]],
            "answer": "N"
        }
    ],
    "Extra": [
        {
            "input": [5, [1, 2, 3, 2, 1]],
            "answer": "N"
        },
    ]
}
