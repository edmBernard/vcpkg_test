import subprocess
from path import Path


with open("vcpkg_status.md", 'w') as outfile:
    outfile.write("| Library | x64-linux |\n")
    outfile.write("| :-- | -- |\n")
    for lib in sorted(Path("vcpkg/ports").dirs("*")):
        ret = subprocess.run(["docker", "run", "base_vcpk", "./vcpkg", "install", lib.basename()])
        print(ret.args)
        outfile.write("| %s | %s |\n" % (lib.basename(), ["Failed", "Success"][ret.returncode == 0]))