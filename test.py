import subprocess
from path import Path

Path("status").mkdir_p()

with open("vcpkg_status.md", 'w') as outfile:
    outfile.write("| Library | x64-linux |\n")
    outfile.write("| :-- | -- |\n")

for lib in sorted(Path("vcpkg/ports").dirs("*")):
    with open("vcpkg_status.md", 'a') as outfile:
        ret = subprocess.run(["docker", "run", "--name", lib.basename(), "--rm", "base_vcpk", "./vcpkg", "install", lib.basename()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        outfile.write("| %s | %s |\n" % (lib.basename(), ["Failed", "Success"][ret.returncode == 0]))

        with open("status/%s_stderr.log" %  lib.basename(), 'wb') as stderrfile:
            stderrfile.write(ret.stderr)
        with open("status/%s_stdout.log" %  lib.basename(), 'wb') as stdoutfile:
            stdoutfile.write(ret.stdout)
