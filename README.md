# VCPKG Test

Script to test vcpkg compilation libraries on ubuntu.
It will build all libraries available in vcpkg. All build are isolated in a new container. Build outpur message are saved.

# Build Docker base

```bash
docker build -t base_vcpkg -f Dockerfile .
```

# launch test

```bash
python3 test.py status_YYYYMMDD
```
