load("@rules_python//python:defs.bzl", "py_library", "py_binary", "py_test")

# Main library
py_library(
    name = "smarthex",
    srcs = glob(["smarthex/smarthex/**/*.py"]),
    imports = ["smarthex"],
    visibility = ["//visibility:public"],
)

py_binary(
    name = "smhex",
    srcs = ["smarthex/smarthex/cli.py"],
    main = "smarthex/smarthex/cli.py",
    deps = [":smarthex"],
    imports = ["smarthex"],
)

py_test(
    name = "tests",
    srcs = ["smarthex/tests/test_smarthex.py"],
    main = "smarthex/tests/test_smarthex.py",
    deps = [":smarthex"],
    imports = ["smarthex"],
) 