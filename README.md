# MTranServer (Simplified)

> Mini Translation Server Beta Version with
>
> 1. Remove dummy files (the `core` folder is not open sourced yet)
> 2. Add download scripts

Original READMEs: [中文](readme/README_zh.md) | [日本語](readme/README_ja.md) | [English](readme/README_en.md)

## Getting Started

> NOTE: currently no pre-build image for M-series macOS
>
> `no matching manifest for linux/arm64/v8 in the manifest list entries`

```bash
$ python download_model.py --help
NAME
    download_model.py - Download and extract a model asset.

SYNOPSIS
    download_model.py <flags>

DESCRIPTION
    Download and extract a model asset.

FLAGS
    -a, --asset=ASSET
        Type: Literal
        Default: 'enzh'
        The key of the asset to download. Options are: enzh, enja, zhen, jaen.
    -o, --output_dir=OUTPUT_DIR
        Type: str
        Default: './models'
        The directory where the zip contents should be extracted.

$ python download_model.py enzh
```

## Note

Seems this project use same model as [firefox-translations-models/registry.json](https://github.com/mozilla/firefox-translations-models/blob/250530e63f82e032e2aad483ce23f8b1a7635c08/registry.json#L1419-L1441) / [firefox-translations-models/models/dev/enzh at main · mozilla/firefox-translations-models](https://github.com/mozilla/firefox-translations-models/tree/main/models/dev/enzh)

```bash
cd submodules/marian
mkdir build && cd build
# This will clone its dependencies as submodules
# Compile CPU version
cmake .. -DCOMPILE_CUDA=off
make -j4

# BUG: having some compilation error
# /Library/Developer/CommandLineTools/usr/lib/clang/16/include/immintrin.h:14:2: error: "This header is only meant to be used on x86 and x64 architecture"
```

```bash
# GPU (with CUDA) version
# Currently, I am working on my M-series Mac, so leave this part in the future
$ cmake ..

CMake Deprecation Warning at CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.10 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value.  Or, use the <min>...<max> syntax
  to tell CMake that the project requires at least <min> but has been updated
  to work with policies introduced by <max> or earlier.


-- The CXX compiler identification is AppleClang 16.0.0.16000026
-- The C compiler identification is AppleClang 16.0.0.16000026
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Library/Developer/CommandLineTools/usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Library/Developer/CommandLineTools/usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Project name: marian
-- Project version: v1.12.31+a6ab8af8
Submodule 'examples' (https://github.com/marian-nmt/marian-examples) registered for path 'examples'
Submodule 'regression-tests' (https://github.com/marian-nmt/marian-regression-tests) registered for path 'regression-tests'
Submodule 'src/3rd_party/fbgemm' (https://github.com/marian-nmt/FBGEMM) registered for path 'src/3rd_party/fbgemm'
Submodule 'src/3rd_party/intgemm' (https://github.com/marian-nmt/intgemm/) registered for path 'src/3rd_party/intgemm'
Submodule 'src/3rd_party/nccl' (https://github.com/marian-nmt/nccl) registered for path 'src/3rd_party/nccl'
Submodule 'src/3rd_party/pybind11' (https://github.com/pybind/pybind11.git) registered for path 'src/3rd_party/pybind11'
Submodule 'src/3rd_party/ruy' (https://github.com/marian-nmt/ruy.git) registered for path 'src/3rd_party/ruy'
Submodule 'src/3rd_party/sentencepiece' (https://github.com/marian-nmt/sentencepiece) registered for path 'src/3rd_party/sentencepiece'
Submodule 'src/3rd_party/simd_utils' (https://github.com/marian-nmt/simd_utils.git) registered for path 'src/3rd_party/simd_utils'
Submodule 'src/3rd_party/simple-websocket-server' (https://github.com/marian-nmt/Simple-WebSocket-Server) registered for path 'src/3rd_party/simple-websocket-server'
Cloning into '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/examples'...
Cloning into '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/regression-tests'...
Cloning into '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/src/3rd_party/fbgemm'...
Cloning into '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/src/3rd_party/intgemm'...
Cloning into '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/src/3rd_party/nccl'...
Cloning into '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/src/3rd_party/pybind11'...
Cloning into '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/src/3rd_party/ruy'...
Cloning into '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/src/3rd_party/sentencepiece'...
error: RPC failed; curl 92 HTTP/2 stream 5 was not closed cleanly: CANCEL (err 8)
error: 4627 bytes of body are still expected
fetch-pack: unexpected disconnect while reading sideband packet
fatal: early EOF
fatal: fetch-pack: invalid index-pack output
fatal: clone of 'https://github.com/marian-nmt/sentencepiece' into submodule path '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/src/3rd_party/sentencepiece' failed
Failed to clone 'src/3rd_party/sentencepiece'. Retry scheduled
Cloning into '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/src/3rd_party/simd_utils'...
Cloning into '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/src/3rd_party/simple-websocket-server'...
Cloning into '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/src/3rd_party/sentencepiece'...
error: RPC failed; curl 92 HTTP/2 stream 5 was not closed cleanly: CANCEL (err 8)
error: 5112 bytes of body are still expected
fetch-pack: unexpected disconnect while reading sideband packet
fatal: early EOF
fatal: fetch-pack: invalid index-pack output
fatal: clone of 'https://github.com/marian-nmt/sentencepiece' into submodule path '/Users/daviddwlee84/Documents/Program/Personal/MTranServerSimplify/submodules/marian/src/3rd_party/sentencepiece' failed
Failed to clone 'src/3rd_party/sentencepiece' a second time, aborting
CMake Warning at CMakeLists.txt:82 (message):
  CMAKE_BUILD_TYPE not set; setting to Release


-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- Building with -march=native and intrinsics will be chosen automatically by the compiler to match the current machine.
-- Checking support for CPU intrinsics
CMake Warning (dev) at cmake/FindSSE.cmake:77 (EXEC_PROGRAM):
  Policy CMP0153 is not set: The exec_program command should not be called.
  Run "cmake --help-policy CMP0153" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  Use execute_process() instead.
Call Stack (most recent call first):
  CMakeLists.txt:207 (include)
This warning is for project developers.  Use -Wno-dev to suppress it.

-- Could not find hardware support for SSE2 on this machine.
-- Could not find hardware support for SSE3 on this machine.
-- Could not find hardware support for SSSE3 on this machine.
-- Could not find hardware support for SSE4.1 on this machine.
-- Could not find hardware support for AVX on this machine.
-- Could not find hardware support for AVX2 on this machine.
-- Could not find hardware support for AVX512 on this machine.
CMake Warning (dev) at CMakeLists.txt:368 (find_package):
  Policy CMP0146 is not set: The FindCUDA module is removed.  Run "cmake
  --help-policy CMP0146" for policy details.  Use the cmake_policy command to
  set the policy and suppress this warning.

This warning is for project developers.  Use -Wno-dev to suppress it.

CUDA_TOOLKIT_ROOT_DIR not found or specified
-- Could NOT find CUDA (missing: CUDA_TOOLKIT_ROOT_DIR CUDA_NVCC_EXECUTABLE CUDA_INCLUDE_DIRS CUDA_CUDART_LIBRARY) (Required is at least version "9.0")

Cannot find suitable CUDA libraries. Specify the path explicitly with
  -DCUDA_TOOLKIT_ROOT_DIR=/path/to/appropriate/cuda/installation
   (hint: try /usr/local/$(readlink /usr/local/cuda))
OR compile the CPU-only version of Marian with
  -DCOMPILE_CUDA=off

CMake Error at CMakeLists.txt:521 (message):
  FATAL ERROR: No suitable CUDA library found.


-- Configuring incomplete, errors occurred!
```

## Resources

- [OpenNMT/CTranslate2: Fast inference engine for Transformer models](https://github.com/OpenNMT/CTranslate2)
- [mozilla/translations: The code, training pipeline, and models that power Firefox Translations](https://github.com/mozilla/translations)
  - [mozilla/firefox-translations-models: CPU-optimized Neural Machine Translation models for Firefox Translations](https://github.com/mozilla/firefox-translations-models) => Based on browsermt/students?!
- [browsermt/students: Efficient teacher-student models and scripts to make them](https://github.com/browsermt/students) => Based on Marian
  - [students/train-student at master · browsermt/students](https://github.com/browsermt/students/tree/master/train-student)
- [marian-nmt/marian-dev: Fast Neural Machine Translation in C++ - development repository](https://github.com/marian-nmt/marian-dev)
  - [Marian :: Home](https://marian-nmt.github.io/)
