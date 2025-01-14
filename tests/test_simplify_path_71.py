from leet_code.simplify_path_71 import Solution
from pytest import mark


@mark.parametrize("path, expected", [
    ("/home/", "/home"),
    ("/home//foo/", "/home/foo"),
    ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
    ("/home/user/../../Pictures", "/Pictures"),
    ("/../", "/"),
    ("/.../a/../b/c/../d/./", "/.../b/d"),
    ("/a/./b/../../c/", "/c"),
    ("/a//b////c/d//././/..", "/a/b/c")
])
def test_simplify_path(path, expected):
    solution = Solution()
    output = solution.simplify_path(path)
    assert output == expected
