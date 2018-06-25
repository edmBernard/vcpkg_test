import subprocess
from path import Path

def main(folder="status"):

    Path(folder).mkdir_p()

    with open("vcpkg_%s.md" % folder, 'w') as outfile:
        outfile.write("| Library | x64-linux |\n")
        outfile.write("| :-- | -- |\n")

    for lib in sorted(Path("vcpkg/ports").dirs("*")):
        with open("vcpkg_%s.md" % folder, 'a') as outfile:
            ret = subprocess.run(["docker", "run", "--name", lib.basename(), "--rm", "base_vcpkg", "./vcpkg", "install", lib.basename()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            outfile.write("| %s | %s |\n" % (lib.basename(), ["Failed", "Success"][ret.returncode == 0]))

            with open("%s/%s_stderr.log" % (folder, lib.basename()), 'wb') as stderrfile:
                stderrfile.write(ret.stderr)
            with open("%s/%s_stdout.log" %  (folder, lib.basename()), 'wb') as stdoutfile:
                stdoutfile.write(ret.stdout)

if __name__ == '__main__':
    from fire import Fire
    Fire(main)
