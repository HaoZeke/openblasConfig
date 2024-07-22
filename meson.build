project('OpenBLAS_Config', ['c', 'fortran'],
        default_options: ['c_std=c99'],
        version: '0.3.26.dev')

cc = meson.get_compiler('c')
fc = meson.get_compiler('fortran')
fc_id = fc.get_id()

build_without_lapack = get_option('build_without_lapack')
use_perl = get_option('use_perl')

# TODO(rg): Use options more carefully
fs = import('fs')

ctest_files = ['ctest.c', 'ctest1.c', 'ctest2.c']
ftest_files = ['ftest.f', 'ftest2.f', 'ftest3.f']

foreach testf : ctest_files + ftest_files
  fs.copyfile(testf)
endforeach

cchk=custom_target(
  'c_checks',
  output: ['Makefile_c.conf', 'config_c.h'],
  input: ctest_files,
  command: [find_program('python'), '../scripts/run_check.py',
            find_program('c_check'), 'c', 'gcc'],
)
fchk=custom_target(
  'f_checks',
  output: ['Makefile_f.conf', 'config_f.h'],
  input: ftest_files,
  command: [find_program('python'), '../scripts/run_check.py',
            find_program('f_check'), 'f', 'gfortran'],
)

basic_config = custom_target(
  'basic_config',
  output: ['config.h'],
  depends: [cchk, fchk],
  command: [find_program('python'),
            '../scripts/write_file.py', 'config.h',
            fs.read('config_c.h'),
            fs.read('config_f.h')]
)

getarch = executable('getarch',
          ['getarch.c', 'cpuid.S', basic_config,])
getarch_two = executable('getarch_2nd',
                         ['getarch_2nd.c', basic_config,])
