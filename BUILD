load("@rules_python//python:defs.bzl", "py_library", "py_binary", "py_test")

# Main library
py_library(
    name = "smarthex",
    srcs = glob(["smarthex/**/*.py"]),
    imports = ["."],
    visibility = ["//visibility:public"],
)

py_binary(
    name = "smhex",
    srcs = ["smarthex/cli.py"],
    main = "smarthex/cli.py",
    deps = [":smarthex"],
    imports = ["."],
)

py_test(
    name = "smarthex_test",
    srcs = ["tests/test_smarthex.py"],
    main = "tests/test_smarthex.py",
    deps = [":smarthex"],
    imports = ["."],
) 