# renpy-maget

## Building

### Windows

```pwsh
$path_to_project = $env:USERPROFILE + "\projects\renpymaget"

$path_to_sdk = $env:USERPROFILE + "\projects\renpy-8.0.3-sdk"

cd $path_to_sdk

.\lib\py3-windows-x86_64\python.exe .\renpy.py .\ distribute $path_to_project --package win --no-update
```
